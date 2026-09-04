package com.rentora.escrow;

import java.math.BigDecimal;
import java.math.RoundingMode;
import java.security.MessageDigest;
import java.time.Instant;
import java.util.*;
import java.util.concurrent.ConcurrentHashMap;
import java.util.concurrent.atomic.AtomicLong;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

/**
 * Enterprise Double-Entry Financial Journal Ledger for Rentora Escrow Accounts.
 * Implements strict debit/credit invariant validation, cryptographic SHA-256 block-chaining
 * across journal entries, and automated bank reconciliation hooks.
 */
public class DoubleEntryJournalLedger {
    private static final Logger log = LoggerFactory.getLogger(DoubleEntryJournalLedger.class);

    private final AtomicLong entrySequence = new AtomicLong(100000L);
    private final Map<Long, JournalEntry> journalEntries = new ConcurrentHashMap<>();
    private final Map<String, AccountBalance> accountBalances = new ConcurrentHashMap<>();
    private final List<LedgerEventListener> eventListeners = new ArrayList<>();
    private String latestBlockHash = "0000000000000000000000000000000000000000000000000000000000000000";

    public DoubleEntryJournalLedger() {
        initializeStandardChartOfAccounts();
        log.info("Initialized DoubleEntryJournalLedger with Genesis Block: {}", latestBlockHash);
    }

    private void initializeStandardChartOfAccounts() {
        registerAccount(new AccountBalance("1010", "CUSTOMER_ESCROW_HOLDING_ACCOUNT", AccountType.LIABILITY));
        registerAccount(new AccountBalance("1020", "ESCROW_CASH_IN_BANK_NODAL", AccountType.ASSET));
        registerAccount(new AccountBalance("2010", "RENTAL_REVENUE_CLEARING", AccountType.REVENUE));
        registerAccount(new AccountBalance("2020", "PLATFORM_COMMISSION_EARNED", AccountType.REVENUE));
        registerAccount(new AccountBalance("3010", "VENDOR_PAYOUT_PAYABLE", AccountType.LIABILITY));
        registerAccount(new AccountBalance("4010", "DAMAGE_RECOVERY_RECEIVABLE", AccountType.ASSET));
        registerAccount(new AccountBalance("5010", "GST_CGST_OUTPUT_LIABILITY", AccountType.LIABILITY));
        registerAccount(new AccountBalance("5020", "GST_SGST_OUTPUT_LIABILITY", AccountType.LIABILITY));
        registerAccount(new AccountBalance("5030", "GST_IGST_OUTPUT_LIABILITY", AccountType.LIABILITY));
    }

    public synchronized void registerAccount(AccountBalance account) {
        if (account != null && !accountBalances.containsKey(account.getAccountNumber())) {
            accountBalances.put(account.getAccountNumber(), account);
            log.debug("Registered Chart of Account: {} - {}", account.getAccountNumber(), account.getAccountName());
        }
    }

    public synchronized JournalEntry recordTransaction(
            String referenceCode,
            String description,
            List<LedgerPosting> postings,
            Map<String, String> metadata
    ) throws LedgerValidationException {
        if (postings == null || postings.size() < 2) {
            throw new LedgerValidationException("A valid double-entry transaction must contain at least two postings.");
        }

        BigDecimal totalDebit = BigDecimal.ZERO;
        BigDecimal totalCredit = BigDecimal.ZERO;

        for (LedgerPosting posting : postings) {
            if (posting.getAmount().compareTo(BigDecimal.ZERO) <= 0) {
                throw new LedgerValidationException("Posting amount must be strictly positive: " + posting.getAmount());
            }
            if (posting.getPostingType() == PostingType.DEBIT) {
                totalDebit = totalDebit.add(posting.getAmount());
            } else if (posting.getPostingType() == PostingType.CREDIT) {
                totalCredit = totalCredit.add(posting.getAmount());
            } else {
                throw new LedgerValidationException("Unrecognized posting type in transaction: " + posting.getPostingType());
            }

            if (!accountBalances.containsKey(posting.getAccountNumber())) {
                throw new LedgerValidationException("Account number not registered in Chart of Accounts: " + posting.getAccountNumber());
            }
        }

        // Validate Fundamental Accounting Invariant: SUM(Debits) == SUM(Credits)
        if (totalDebit.setScale(2, RoundingMode.HALF_UP).compareTo(totalCredit.setScale(2, RoundingMode.HALF_UP)) != 0) {
            throw new LedgerValidationException(String.format(
                "Debit and Credit totals are out of balance! Total Debits: %s, Total Credits: %s (Variance: %s)",
                totalDebit, totalCredit, totalDebit.subtract(totalCredit)
            ));
        }

        long entryId = entrySequence.incrementAndGet();
        Instant timestamp = Instant.now();

        // Calculate cryptographic hash chaining
        String currentHash = calculateEntryHash(entryId, referenceCode, totalDebit, timestamp, latestBlockHash);

        JournalEntry entry = new JournalEntry(
            entryId,
            referenceCode,
            description,
            postings,
            totalDebit,
            latestBlockHash,
            currentHash,
            timestamp,
            metadata != null ? metadata : Collections.emptyMap()
        );

        // Update Account Balances
        for (LedgerPosting posting : postings) {
            AccountBalance balance = accountBalances.get(posting.getAccountNumber());
            balance.applyPosting(posting);
        }

        journalEntries.put(entryId, entry);
        this.latestBlockHash = currentHash;

        log.info("Journal Entry #{} committed successfully. Reference: [{}], Amount: INR {}, Hash: {}",
            entryId, referenceCode, totalDebit, currentHash.substring(0, 12));

        notifyListeners(entry);
        return entry;
    }

    private String calculateEntryHash(long id, String ref, BigDecimal amount, Instant time, String prevHash) {
        try {
            MessageDigest digest = MessageDigest.getInstance("SHA-256");
            String payload = String.format("%d|%s|%s|%s|%s", id, ref, amount.toPlainString(), time.toString(), prevHash);
            byte[] hashBytes = digest.digest(payload.getBytes("UTF-8"));
            StringBuilder sb = new StringBuilder();
            for (byte b : hashBytes) {
                sb.append(String.format("%02x", b));
            }
            return sb.toString();
        } catch (Exception ex) {
            log.error("Error computing cryptographic hash for entry {}", id, ex);
            return UUID.randomUUID().toString();
        }
    }

    public boolean verifyLedgerIntegrity() {
        log.info("Verifying cryptographic hash chain integrity across {} journal entries...", journalEntries.size());
        List<JournalEntry> sorted = new ArrayList<>(journalEntries.values());
        sorted.sort(Comparator.comparingLong(JournalEntry::getEntryId));

        String expectedPrev = "0000000000000000000000000000000000000000000000000000000000000000";
        for (JournalEntry entry : sorted) {
            if (!entry.getPreviousBlockHash().equals(expectedPrev)) {
                log.error("Integrity breach at Entry #{}: Previous hash mismatch. Expected {}, found {}",
                    entry.getEntryId(), expectedPrev, entry.getPreviousBlockHash());
                return false;
            }
            String calculated = calculateEntryHash(
                entry.getEntryId(), entry.getReferenceCode(), entry.getTotalAmount(),
                entry.getTimestamp(), entry.getPreviousBlockHash()
            );
            if (!calculated.equals(entry.getBlockHash())) {
                log.error("Integrity breach at Entry #{}: Block hash mismatch. Expected {}, found {}",
                    entry.getEntryId(), calculated, entry.getBlockHash());
                return false;
            }
            expectedPrev = entry.getBlockHash();
        }
        log.info("Ledger cryptographic integrity audit PASSED. All block chains valid.");
        return true;
    }

    public AccountBalance getAccountBalance(String accountNumber) {
        return accountBalances.get(accountNumber);
    }

    public Collection<AccountBalance> getAllAccountBalances() {
        return accountBalances.values();
    }

    public Optional<JournalEntry> findEntryById(long entryId) {
        return Optional.ofNullable(journalEntries.get(entryId));
    }

    public List<JournalEntry> findEntriesByReference(String referenceCode) {
        List<JournalEntry> results = new ArrayList<>();
        for (JournalEntry entry : journalEntries.values()) {
            if (entry.getReferenceCode().equalsIgnoreCase(referenceCode)) {
                results.add(entry);
            }
        }
        return results;
    }

    private void notifyListeners(JournalEntry entry) {
        for (LedgerEventListener listener : eventListeners) {
            try {
                listener.onJournalEntryCommitted(entry);
            } catch (Exception ex) {
                log.error("Error executing ledger listener", ex);
            }
        }
    }

    public synchronized void addEventListener(LedgerEventListener listener) {
        if (listener != null && !eventListeners.contains(listener)) {
            eventListeners.add(listener);
        }
    }
}
