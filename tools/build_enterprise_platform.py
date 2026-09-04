#!/usr/bin/env python3
"""
Rentora Enterprise Platform Expansion Generator
Generates comprehensive enterprise modules across Java Backend, Python Services, and React UI.
"""

import os
import sys

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
BACKEND_DIR = os.path.join(BASE_DIR, "backend", "src", "main", "java", "com", "rentora")
SERVICES_DIR = os.path.join(BASE_DIR, "services")
FRONTEND_DIR = os.path.join(BASE_DIR, "frontend", "src")

def ensure_dir(path):
    os.makedirs(path, exist_ok=True)

def write_file(path, content):
    ensure_dir(os.path.dirname(path))
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  + {os.path.relpath(path, BASE_DIR)} ({len(content.splitlines())} lines)")

# =============================================================================
# 1. JAVA MODULES GENERATOR
# =============================================================================

def build_java_modules():
    print("\n--> Building Enterprise Java Backend Modules...")

    # --- ESCROW PACKAGE ---
    escrow_dir = os.path.join(BACKEND_DIR, "escrow")
    
    # 1. DoubleEntryJournalLedger.java
    write_file(os.path.join(escrow_dir, "DoubleEntryJournalLedger.java"), """package com.rentora.escrow;

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
""")

    # 1.2 Supporting Escrow Classes
    write_file(os.path.join(escrow_dir, "AccountBalance.java"), """package com.rentora.escrow;

import java.math.BigDecimal;

public class AccountBalance {
    private final String accountNumber;
    private final String accountName;
    private final AccountType accountType;
    private BigDecimal currentBalance = BigDecimal.ZERO;
    private long totalPostings = 0;

    public AccountBalance(String accountNumber, String accountName, AccountType accountType) {
        this.accountNumber = accountNumber;
        this.accountName = accountName;
        this.accountType = accountType;
    }

    public synchronized void applyPosting(LedgerPosting posting) {
        if (accountType == AccountType.ASSET || accountType == AccountType.EXPENSE) {
            if (posting.getPostingType() == PostingType.DEBIT) {
                this.currentBalance = this.currentBalance.add(posting.getAmount());
            } else {
                this.currentBalance = this.currentBalance.subtract(posting.getAmount());
            }
        } else {
            // LIABILITY, EQUITY, REVENUE
            if (posting.getPostingType() == PostingType.CREDIT) {
                this.currentBalance = this.currentBalance.add(posting.getAmount());
            } else {
                this.currentBalance = this.currentBalance.subtract(posting.getAmount());
            }
        }
        this.totalPostings++;
    }

    public String getAccountNumber() { return accountNumber; }
    public String getAccountName() { return accountName; }
    public AccountType getAccountType() { return accountType; }
    public BigDecimal getCurrentBalance() { return currentBalance; }
    public long getTotalPostings() { return totalPostings; }
}
""")

    write_file(os.path.join(escrow_dir, "AccountType.java"), """package com.rentora.escrow;

public enum AccountType {
    ASSET,
    LIABILITY,
    EQUITY,
    REVENUE,
    EXPENSE
}
""")

    write_file(os.path.join(escrow_dir, "PostingType.java"), """package com.rentora.escrow;

public enum PostingType {
    DEBIT,
    CREDIT
}
""")

    write_file(os.path.join(escrow_dir, "LedgerPosting.java"), """package com.rentora.escrow;

import java.math.BigDecimal;

public class LedgerPosting {
    private final String accountNumber;
    private final PostingType postingType;
    private final BigDecimal amount;
    private final String memo;

    public LedgerPosting(String accountNumber, PostingType postingType, BigDecimal amount, String memo) {
        this.accountNumber = accountNumber;
        this.postingType = postingType;
        this.amount = amount;
        this.memo = memo;
    }

    public String getAccountNumber() { return accountNumber; }
    public PostingType getPostingType() { return postingType; }
    public BigDecimal getAmount() { return amount; }
    public String getMemo() { return memo; }
}
""")

    write_file(os.path.join(escrow_dir, "JournalEntry.java"), """package com.rentora.escrow;

import java.math.BigDecimal;
import java.time.Instant;
import java.util.List;
import java.util.Map;

public class JournalEntry {
    private final long entryId;
    private final String referenceCode;
    private final String description;
    private final List<LedgerPosting> postings;
    private final BigDecimal totalAmount;
    private final String previousBlockHash;
    private final String blockHash;
    private final Instant timestamp;
    private final Map<String, String> metadata;

    public JournalEntry(
        long entryId,
        String referenceCode,
        String description,
        List<LedgerPosting> postings,
        BigDecimal totalAmount,
        String previousBlockHash,
        String blockHash,
        Instant timestamp,
        Map<String, String> metadata
    ) {
        this.entryId = entryId;
        this.referenceCode = referenceCode;
        this.description = description;
        this.postings = postings;
        this.totalAmount = totalAmount;
        this.previousBlockHash = previousBlockHash;
        this.blockHash = blockHash;
        this.timestamp = timestamp;
        this.metadata = metadata;
    }

    public long getEntryId() { return entryId; }
    public String getReferenceCode() { return referenceCode; }
    public String getDescription() { return description; }
    public List<LedgerPosting> getPostings() { return postings; }
    public BigDecimal getTotalAmount() { return totalAmount; }
    public String getPreviousBlockHash() { return previousBlockHash; }
    public String getBlockHash() { return blockHash; }
    public Instant getTimestamp() { return timestamp; }
    public Map<String, String> getMetadata() { return metadata; }
}
""")

    write_file(os.path.join(escrow_dir, "LedgerValidationException.java"), """package com.rentora.escrow;

public class LedgerValidationException extends Exception {
    public LedgerValidationException(String message) {
        super(message);
    }
}
""")

    write_file(os.path.join(escrow_dir, "LedgerEventListener.java"), """package com.rentora.escrow;

public interface LedgerEventListener {
    void onJournalEntryCommitted(JournalEntry entry);
}
""")

    # 1.3 EscrowSettlementEngine.java
    write_file(os.path.join(escrow_dir, "EscrowSettlementEngine.java"), """package com.rentora.escrow;

import java.math.BigDecimal;
import java.time.Instant;
import java.util.*;
import java.util.concurrent.ConcurrentHashMap;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

/**
 * Escrow Settlement Engine managing automated deposit lockups, dispute holds,
 * damage fee transfers to vendors, and automated bank refunds for Rentora customers.
 */
public class EscrowSettlementEngine {
    private static final Logger log = LoggerFactory.getLogger(EscrowSettlementEngine.class);

    private final DoubleEntryJournalLedger ledger;
    private final Map<Long, EscrowDepositRecord> deposits = new ConcurrentHashMap<>();
    private final List<SettlementAuditHook> auditHooks = new ArrayList<>();

    public EscrowSettlementEngine(DoubleEntryJournalLedger ledger) {
        this.ledger = ledger;
        log.info("Initialized EscrowSettlementEngine with connected journal ledger.");
    }

    public synchronized EscrowDepositRecord lockDeposit(
            long rentalId,
            long customerId,
            long vendorId,
            BigDecimal depositAmount,
            String paymentGatewayRef
    ) throws LedgerValidationException {
        if (depositAmount.compareTo(BigDecimal.ZERO) <= 0) {
            throw new IllegalArgumentException("Deposit amount must be strictly greater than zero");
        }

        String ref = "ESCROW-LOCK-" + rentalId;
        List<LedgerPosting> postings = Arrays.asList(
            new LedgerPosting("1020", PostingType.DEBIT, depositAmount, "Bank Inflow for Escrow Deposit - Rental #" + rentalId),
            new LedgerPosting("1010", PostingType.CREDIT, depositAmount, "Holding Escrow Liability for Customer #" + customerId)
        );

        Map<String, String> meta = new HashMap<>();
        meta.put("rentalId", String.valueOf(rentalId));
        meta.put("customerId", String.valueOf(customerId));
        meta.put("gatewayRef", paymentGatewayRef);

        JournalEntry entry = ledger.recordTransaction(ref, "Lock Security Deposit in Regulated Escrow", postings, meta);

        EscrowDepositRecord record = new EscrowDepositRecord(
            rentalId, customerId, vendorId, depositAmount,
            EscrowStatus.HELD_LOCKED, entry.getEntryId(), paymentGatewayRef
        );
        deposits.put(rentalId, record);

        log.info("Deposit of INR {} securely locked in Escrow for Rental #{}. Journal Entry: {}",
            depositAmount, rentalId, entry.getEntryId());

        triggerAuditHooks(record, "DEPOSIT_LOCKED");
        return record;
    }

    public synchronized EscrowDepositRecord settleCleanReturn(long rentalId) throws LedgerValidationException {
        EscrowDepositRecord record = deposits.get(rentalId);
        if (record == null) {
            throw new NoSuchElementException("No escrow record found for rental ID: " + rentalId);
        }
        if (record.getStatus() != EscrowStatus.HELD_LOCKED) {
            throw new IllegalStateException("Deposit cannot be refunded in status: " + record.getStatus());
        }

        BigDecimal refundAmount = record.getHeldAmount();
        String ref = "ESCROW-REFUND-" + rentalId;

        List<LedgerPosting> postings = Arrays.asList(
            new LedgerPosting("1010", PostingType.DEBIT, refundAmount, "Release Holding Liability - 100% Clean Return #" + rentalId),
            new LedgerPosting("1020", PostingType.CREDIT, refundAmount, "Bank Outflow to Customer Account - Rental #" + rentalId)
        );

        JournalEntry entry = ledger.recordTransaction(ref, "100% Automated Escrow Deposit Refund", postings, null);

        record.setRefundedAmount(refundAmount);
        record.setDamageDeduction(BigDecimal.ZERO);
        record.setStatus(EscrowStatus.REFUNDED_COMPLETE);
        record.setSettledTimestamp(Instant.now());
        record.setSettlementJournalId(entry.getEntryId());

        log.info("100% Deposit Refund of INR {} disbursed for Rental #{}. SLA achieved < 4 hours.",
            refundAmount, rentalId);

        triggerAuditHooks(record, "CLEAN_REFUND_SETTLED");
        return record;
    }

    public synchronized EscrowDepositRecord settleDamagedReturn(long rentalId, BigDecimal damageFee, String incidentNotes) throws LedgerValidationException {
        EscrowDepositRecord record = deposits.get(rentalId);
        if (record == null) {
            throw new NoSuchElementException("No escrow record found for rental ID: " + rentalId);
        }
        if (damageFee.compareTo(record.getHeldAmount()) > 0) {
            throw new IllegalArgumentException("Damage assessment fee cannot exceed total locked escrow deposit: " + record.getHeldAmount());
        }

        BigDecimal refundAmount = record.getHeldAmount().subtract(damageFee);
        String ref = "ESCROW-DAMAGE-" + rentalId;

        List<LedgerPosting> postings = new ArrayList<>();
        postings.add(new LedgerPosting("1010", PostingType.DEBIT, record.getHeldAmount(), "Clear Customer Escrow Liability - Rental #" + rentalId));
        if (damageFee.compareTo(BigDecimal.ZERO) > 0) {
            postings.add(new LedgerPosting("3010", PostingType.CREDIT, damageFee, "Vendor Damage Compensation Payable - Rental #" + rentalId));
        }
        if (refundAmount.compareTo(BigDecimal.ZERO) > 0) {
            postings.add(new LedgerPosting("1020", PostingType.CREDIT, refundAmount, "Remaining Deposit Bank Outflow to Customer - Rental #" + rentalId));
        }

        JournalEntry entry = ledger.recordTransaction(ref, "Escrow Damage Settlement: " + incidentNotes, postings, null);

        record.setDamageDeduction(damageFee);
        record.setRefundedAmount(refundAmount);
        record.setStatus(EscrowStatus.SETTLED_WITH_DEDUCTION);
        record.setSettledTimestamp(Instant.now());
        record.setSettlementJournalId(entry.getEntryId());
        record.setIncidentReport(incidentNotes);

        log.info("Damage Settlement complete for Rental #{}: INR {} retained for vendor, INR {} refunded to customer.",
            rentalId, damageFee, refundAmount);

        triggerAuditHooks(record, "DAMAGE_SETTLED");
        return record;
    }

    public Optional<EscrowDepositRecord> getRecord(long rentalId) {
        return Optional.ofNullable(deposits.get(rentalId));
    }

    public Collection<EscrowDepositRecord> getAllDeposits() {
        return Collections.unmodifiableCollection(deposits.values());
    }

    private void triggerAuditHooks(EscrowDepositRecord record, String event) {
        for (SettlementAuditHook hook : auditHooks) {
            try {
                hook.onSettlementEvent(record, event);
            } catch (Exception ex) {
                log.error("Audit hook execution failure", ex);
            }
        }
    }

    public void addAuditHook(SettlementAuditHook hook) {
        if (hook != null && !auditHooks.contains(hook)) {
            auditHooks.add(hook);
        }
    }
}
""")

    write_file(os.path.join(escrow_dir, "EscrowDepositRecord.java"), """package com.rentora.escrow;

import java.math.BigDecimal;
import java.time.Instant;

public class EscrowDepositRecord {
    private final long rentalId;
    private final long customerId;
    private final long vendorId;
    private final BigDecimal heldAmount;
    private BigDecimal refundedAmount = BigDecimal.ZERO;
    private BigDecimal damageDeduction = BigDecimal.ZERO;
    private EscrowStatus status;
    private final long lockJournalId;
    private long settlementJournalId;
    private final String gatewayReference;
    private String incidentReport;
    private final Instant createdAt;
    private Instant settledTimestamp;

    public EscrowDepositRecord(
        long rentalId, long customerId, long vendorId, BigDecimal heldAmount,
        EscrowStatus status, long lockJournalId, String gatewayReference
    ) {
        this.rentalId = rentalId;
        this.customerId = customerId;
        this.vendorId = vendorId;
        this.heldAmount = heldAmount;
        this.status = status;
        this.lockJournalId = lockJournalId;
        this.gatewayReference = gatewayReference;
        this.createdAt = Instant.now();
    }

    public long getRentalId() { return rentalId; }
    public long getCustomerId() { return customerId; }
    public long getVendorId() { return vendorId; }
    public BigDecimal getHeldAmount() { return heldAmount; }
    public BigDecimal getRefundedAmount() { return refundedAmount; }
    public void setRefundedAmount(BigDecimal refundedAmount) { this.refundedAmount = refundedAmount; }
    public BigDecimal getDamageDeduction() { return damageDeduction; }
    public void setDamageDeduction(BigDecimal damageDeduction) { this.damageDeduction = damageDeduction; }
    public EscrowStatus getStatus() { return status; }
    public void setStatus(EscrowStatus status) { this.status = status; }
    public long getLockJournalId() { return lockJournalId; }
    public long getSettlementJournalId() { return settlementJournalId; }
    public void setSettlementJournalId(long id) { this.settlementJournalId = id; }
    public String getGatewayReference() { return gatewayReference; }
    public String getIncidentReport() { return incidentReport; }
    public void setIncidentReport(String r) { this.incidentReport = r; }
    public Instant getCreatedAt() { return createdAt; }
    public Instant getSettledTimestamp() { return settledTimestamp; }
    public void setSettledTimestamp(Instant t) { this.settledTimestamp = t; }
}
""")

    write_file(os.path.join(escrow_dir, "EscrowStatus.java"), """package com.rentora.escrow;

public enum EscrowStatus {
    PENDING_PAYMENT,
    HELD_LOCKED,
    DISPUTE_HOLD,
    REFUNDED_COMPLETE,
    SETTLED_WITH_DEDUCTION,
    FORFEITED
}
""")

    write_file(os.path.join(escrow_dir, "SettlementAuditHook.java"), """package com.rentora.escrow;

public interface SettlementAuditHook {
    void onSettlementEvent(EscrowDepositRecord record, String eventType);
}
""")

    # 1.4 DisputeArbitrationVault.java
    write_file(os.path.join(escrow_dir, "DisputeArbitrationVault.java"), """package com.rentora.escrow;

import java.math.BigDecimal;
import java.time.Instant;
import java.util.*;
import java.util.concurrent.ConcurrentHashMap;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class DisputeArbitrationVault {
    private static final Logger log = LoggerFactory.getLogger(DisputeArbitrationVault.class);
    private final Map<Long, DisputeCase> cases = new ConcurrentHashMap<>();

    public DisputeCase openDispute(long rentalId, long initiatedByUserId, String claimCategory, String statement, BigDecimal contestedAmount) {
        DisputeCase dispute = new DisputeCase(
            rentalId, initiatedByUserId, claimCategory, statement, contestedAmount, Instant.now()
        );
        cases.put(rentalId, dispute);
        log.warn("Opened Dispute Case for Rental #{}: [{}] Contested Amount: INR {}", rentalId, claimCategory, contestedAmount);
        return dispute;
    }

    public void assignMediator(long rentalId, String mediatorName) {
        DisputeCase dispute = cases.get(rentalId);
        if (dispute != null) {
            dispute.setAssignedMediator(mediatorName);
            dispute.setStatus("UNDER_ARBITRATION");
            log.info("Assigned mediator {} to Rental #{} dispute.", mediatorName, rentalId);
        }
    }

    public void resolveCase(long rentalId, String resolutionSummary, BigDecimal approvedCustomerRefund, BigDecimal approvedVendorAward) {
        DisputeCase dispute = cases.get(rentalId);
        if (dispute != null) {
            dispute.setResolution(resolutionSummary);
            dispute.setApprovedCustomerRefund(approvedCustomerRefund);
            dispute.setApprovedVendorAward(approvedVendorAward);
            dispute.setStatus("RESOLVED");
            dispute.setResolvedAt(Instant.now());
            log.info("Dispute resolved for Rental #{}. Customer Award: INR {}, Vendor Award: INR {}",
                rentalId, approvedCustomerRefund, approvedVendorAward);
        }
    }

    public Optional<DisputeCase> getDispute(long rentalId) {
        return Optional.ofNullable(cases.get(rentalId));
    }
}
""")

    write_file(os.path.join(escrow_dir, "DisputeCase.java"), """package com.rentora.escrow;

import java.math.BigDecimal;
import java.time.Instant;

public class DisputeCase {
    private final long rentalId;
    private final long initiatedByUserId;
    private final String claimCategory;
    private final String statement;
    private final BigDecimal contestedAmount;
    private String assignedMediator;
    private String status = "OPEN";
    private String resolution;
    private BigDecimal approvedCustomerRefund = BigDecimal.ZERO;
    private BigDecimal approvedVendorAward = BigDecimal.ZERO;
    private final Instant createdAt;
    private Instant resolvedAt;

    public DisputeCase(long rentalId, long initiatedByUserId, String claimCategory, String statement, BigDecimal contestedAmount, Instant createdAt) {
        this.rentalId = rentalId;
        this.initiatedByUserId = initiatedByUserId;
        this.claimCategory = claimCategory;
        this.statement = statement;
        this.contestedAmount = contestedAmount;
        this.createdAt = createdAt;
    }

    public long getRentalId() { return rentalId; }
    public long getInitiatedByUserId() { return initiatedByUserId; }
    public String getClaimCategory() { return claimCategory; }
    public String getStatement() { return statement; }
    public BigDecimal getContestedAmount() { return contestedAmount; }
    public String getAssignedMediator() { return assignedMediator; }
    public void setAssignedMediator(String m) { this.assignedMediator = m; }
    public String getStatus() { return status; }
    public void setStatus(String status) { this.status = status; }
    public String getResolution() { return resolution; }
    public void setResolution(String resolution) { this.resolution = resolution; }
    public BigDecimal getApprovedCustomerRefund() { return approvedCustomerRefund; }
    public void setApprovedCustomerRefund(BigDecimal val) { this.approvedCustomerRefund = val; }
    public BigDecimal getApprovedVendorAward() { return approvedVendorAward; }
    public void setApprovedVendorAward(BigDecimal val) { this.approvedVendorAward = val; }
    public Instant getCreatedAt() { return createdAt; }
    public Instant getResolvedAt() { return resolvedAt; }
    public void setResolvedAt(Instant resolvedAt) { this.resolvedAt = resolvedAt; }
}
""")

    # --- PRICING PACKAGE ---
    pricing_dir = os.path.join(BACKEND_DIR, "pricing")
    
    write_file(os.path.join(pricing_dir, "DynamicPricingAlgorithm.java"), """package com.rentora.pricing;

import java.math.BigDecimal;
import java.math.RoundingMode;
import java.time.DayOfWeek;
import java.time.LocalDate;
import java.util.*;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

/**
 * Enterprise Dynamic Pricing Optimizer.
 * Computes base rate scaling based on duration tiers, fleet demand saturation,
 * seasonal surge calendar, and renter trust score safety credits.
 */
public class DynamicPricingAlgorithm {
    private static final Logger log = LoggerFactory.getLogger(DynamicPricingAlgorithm.class);

    private final SurgeMultiplierCalculator surgeCalc = new SurgeMultiplierCalculator();
    private final VolumeDiscountTierMatrix volumeMatrix = new VolumeDiscountTierMatrix();
    private final CustomerRiskDepositCalculator depositCalc = new CustomerRiskDepositCalculator();

    public PriceQuote calculateQuote(
            long productId,
            BigDecimal baseDailyRate,
            BigDecimal baseDeposit,
            LocalDate startDate,
            LocalDate endDate,
            int customerTrustScore,
            double fleetUtilizationRatio
    ) {
        int durationDays = (int) java.time.temporal.ChronoUnit.DAYS.between(startDate, endDate);
        if (durationDays <= 0) durationDays = 1;

        // 1. Calculate duration volume discount
        double durationDiscountFactor = volumeMatrix.getDiscountFactor(durationDays);
        BigDecimal dailyRateAfterVolume = baseDailyRate.multiply(BigDecimal.valueOf(1.0 - durationDiscountFactor))
            .setScale(2, RoundingMode.HALF_UP);

        // 2. Calculate seasonal and weekend surge multipliers
        double surgeMultiplier = surgeCalc.calculateCompositeSurge(startDate, endDate, fleetUtilizationRatio);
        BigDecimal finalDailyRate = dailyRateAfterVolume.multiply(BigDecimal.valueOf(surgeMultiplier))
            .setScale(2, RoundingMode.HALF_UP);

        // 3. Compute base rental subtotal
        BigDecimal rentalSubtotal = finalDailyRate.multiply(BigDecimal.valueOf(durationDays))
            .setScale(2, RoundingMode.HALF_UP);

        // 4. Calculate Risk-Adjusted Deposit based on Customer Trust Score (0 - 100)
        BigDecimal finalDeposit = depositCalc.computeAdjustedDeposit(baseDeposit, customerTrustScore);

        // 5. GST (18% Total: 9% CGST + 9% SGST)
        BigDecimal cgst = rentalSubtotal.multiply(new BigDecimal("0.09")).setScale(2, RoundingMode.HALF_UP);
        BigDecimal sgst = rentalSubtotal.multiply(new BigDecimal("0.09")).setScale(2, RoundingMode.HALF_UP);
        BigDecimal taxTotal = cgst.add(sgst);

        BigDecimal grandTotal = rentalSubtotal.add(taxTotal).add(finalDeposit);

        log.debug("Quote for Product #{}: {} days @ INR {}/day (Surge {}x). Subtotal: {}, Deposit: {}, Grand: {}",
            productId, durationDays, finalDailyRate, surgeMultiplier, rentalSubtotal, finalDeposit, grandTotal);

        return new PriceQuote(
            productId, durationDays, baseDailyRate, finalDailyRate, durationDiscountFactor,
            surgeMultiplier, rentalSubtotal, cgst, sgst, taxTotal, finalDeposit, grandTotal
        );
    }
}
""")

    write_file(os.path.join(pricing_dir, "PriceQuote.java"), """package com.rentora.pricing;

import java.math.BigDecimal;

public class PriceQuote {
    private final long productId;
    private final int durationDays;
    private final BigDecimal baseDailyRate;
    private final BigDecimal finalDailyRate;
    private final double durationDiscountPercent;
    private final double surgeMultiplier;
    private final BigDecimal rentalSubtotal;
    private final BigDecimal cgst;
    private final BigDecimal sgst;
    private final BigDecimal taxTotal;
    private final BigDecimal refundableDeposit;
    private final BigDecimal grandTotalPayable;

    public PriceQuote(
        long productId, int durationDays, BigDecimal baseDailyRate, BigDecimal finalDailyRate,
        double durationDiscountPercent, double surgeMultiplier, BigDecimal rentalSubtotal,
        BigDecimal cgst, BigDecimal sgst, BigDecimal taxTotal, BigDecimal refundableDeposit,
        BigDecimal grandTotalPayable
    ) {
        this.productId = productId;
        this.durationDays = durationDays;
        this.baseDailyRate = baseDailyRate;
        this.finalDailyRate = finalDailyRate;
        this.durationDiscountPercent = durationDiscountPercent;
        this.surgeMultiplier = surgeMultiplier;
        this.rentalSubtotal = rentalSubtotal;
        this.cgst = cgst;
        this.sgst = sgst;
        this.taxTotal = taxTotal;
        this.refundableDeposit = refundableDeposit;
        this.grandTotalPayable = grandTotalPayable;
    }

    public long getProductId() { return productId; }
    public int getDurationDays() { return durationDays; }
    public BigDecimal getBaseDailyRate() { return baseDailyRate; }
    public BigDecimal getFinalDailyRate() { return finalDailyRate; }
    public double getDurationDiscountPercent() { return durationDiscountPercent; }
    public double getSurgeMultiplier() { return surgeMultiplier; }
    public BigDecimal getRentalSubtotal() { return rentalSubtotal; }
    public BigDecimal getCgst() { return cgst; }
    public BigDecimal getSgst() { return sgst; }
    public BigDecimal getTaxTotal() { return taxTotal; }
    public BigDecimal getRefundableDeposit() { return refundableDeposit; }
    public BigDecimal getGrandTotalPayable() { return grandTotalPayable; }
}
""")

    write_file(os.path.join(pricing_dir, "SurgeMultiplierCalculator.java"), """package com.rentora.pricing;

import java.time.DayOfWeek;
import java.time.LocalDate;

public class SurgeMultiplierCalculator {

    public double calculateCompositeSurge(LocalDate start, LocalDate end, double fleetUtilizationRatio) {
        double multiplier = 1.0;

        // Weekend surge factor
        long weekendDays = 0;
        long totalDays = java.time.temporal.ChronoUnit.DAYS.between(start, end);
        if (totalDays <= 0) totalDays = 1;

        LocalDate curr = start;
        while (!curr.isAfter(end)) {
            if (curr.getDayOfWeek() == DayOfWeek.SATURDAY || curr.getDayOfWeek() == DayOfWeek.SUNDAY) {
                weekendDays++;
            }
            curr = curr.plusDays(1);
        }

        double weekendRatio = (double) weekendDays / totalDays;
        if (weekendRatio > 0.4) {
            multiplier += 0.12; // 12% weekend demand surge
        }

        // Fleet utilization surge factor
        if (fleetUtilizationRatio >= 0.90) {
            multiplier += 0.25; // 25% peak capacity surge
        } else if (fleetUtilizationRatio >= 0.75) {
            multiplier += 0.10; // 10% high demand surge
        }

        return Math.round(multiplier * 100.0) / 100.0;
    }
}
""")

    write_file(os.path.join(pricing_dir, "VolumeDiscountTierMatrix.java"), """package com.rentora.pricing;

public class VolumeDiscountTierMatrix {

    public double getDiscountFactor(int days) {
        if (days >= 30) {
            return 0.30; // 30% monthly volume discount
        } else if (days >= 14) {
            return 0.20; // 20% bi-weekly volume discount
        } else if (days >= 7) {
            return 0.15; // 15% weekly discount
        } else if (days >= 3) {
            return 0.05; // 5% extended weekend discount
        }
        return 0.0;
    }
}
""")

    write_file(os.path.join(pricing_dir, "CustomerRiskDepositCalculator.java"), """package com.rentora.pricing;

import java.math.BigDecimal;
import java.math.RoundingMode;

public class CustomerRiskDepositCalculator {

    public BigDecimal computeAdjustedDeposit(BigDecimal baseDeposit, int customerTrustScore) {
        if (baseDeposit == null || baseDeposit.compareTo(BigDecimal.ZERO) <= 0) {
            return BigDecimal.ZERO;
        }

        // Trust score ranges from 0 to 100
        // Score 95 - 100: 20% discount on required deposit
        // Score 85 - 94: 10% discount
        // Score 60 - 84: Standard deposit (100%)
        // Score < 60: High risk +25% deposit requirement
        double multiplier = 1.0;
        if (customerTrustScore >= 95) {
            multiplier = 0.80;
        } else if (customerTrustScore >= 85) {
            multiplier = 0.90;
        } else if (customerTrustScore < 60) {
            multiplier = 1.25;
        }

        return baseDeposit.multiply(BigDecimal.valueOf(multiplier)).setScale(2, RoundingMode.HALF_UP);
    }
}
""")

    # --- INSPECTION PACKAGE ---
    inspection_dir = os.path.join(BACKEND_DIR, "inspection")
    
    write_file(os.path.join(inspection_dir, "DigitalInspectionProtocol.java"), """package com.rentora.inspection;

import java.math.BigDecimal;
import java.time.Instant;
import java.util.*;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

/**
 * 5-Point Return Inspection Protocol Protocol Engine.
 * Formally evaluates physical condition across Chassis, Optics/Glass, Electronics,
 * Accessories Checklist, and Operational Functional Tests.
 */
public class DigitalInspectionProtocol {
    private static final Logger log = LoggerFactory.getLogger(DigitalInspectionProtocol.class);

    public InspectionEvaluation assessCondition(InspectionReportInput input) {
        List<ChecklistItemResult> results = new ArrayList<>();
        BigDecimal totalDamageAssessment = BigDecimal.ZERO;

        // 1. Physical & Chassis
        results.add(new ChecklistItemResult("CHASSIS_BODY", input.isChassisClean(), input.getChassisNotes(), input.getChassisDamageFee()));
        totalDamageAssessment = totalDamageAssessment.add(input.getChassisDamageFee());

        // 2. Optics / Glass / Sensor
        results.add(new ChecklistItemResult("OPTICS_GLASS", input.isOpticsFlawless(), input.getOpticsNotes(), input.getOpticsDamageFee()));
        totalDamageAssessment = totalDamageAssessment.add(input.getOpticsDamageFee());

        // 3. Electronic Diagnostics
        results.add(new ChecklistItemResult("ELECTRONICS", input.isElectronicsSound(), input.getElectronicsNotes(), input.getElectronicsDamageFee()));
        totalDamageAssessment = totalDamageAssessment.add(input.getElectronicsDamageFee());

        // 4. Kit Accessories Inclusions
        results.add(new ChecklistItemResult("ACCESSORIES_KIT", input.isAllAccessoriesPresent(), input.getAccessoriesNotes(), input.getAccessoriesMissingFee()));
        totalDamageAssessment = totalDamageAssessment.add(input.getAccessoriesMissingFee());

        // 5. Functional Operational Test
        results.add(new ChecklistItemResult("OPERATIONAL_TEST", input.isOperationalPass(), input.getOperationalNotes(), input.getOperationalDamageFee()));
        totalDamageAssessment = totalDamageAssessment.add(input.getOperationalDamageFee());

        boolean isCleanReturn = totalDamageAssessment.compareTo(BigDecimal.ZERO) == 0;
        ConditionGrade grade = isCleanReturn ? ConditionGrade.GRADE_A_PRISTINE : ConditionGrade.GRADE_C_DAMAGED;

        log.info("Inspection evaluated for Rental #{}: Grade {}, Total Damages: INR {}",
            input.getRentalId(), grade, totalDamageAssessment);

        return new InspectionEvaluation(
            input.getRentalId(),
            input.getInspectorName(),
            grade,
            isCleanReturn,
            totalDamageAssessment,
            results,
            input.getPhotographicProofs(),
            Instant.now()
        );
    }
}
""")

    write_file(os.path.join(inspection_dir, "InspectionReportInput.java"), """package com.rentora.inspection;

import java.math.BigDecimal;
import java.util.List;

public class InspectionReportInput {
    private long rentalId;
    private String inspectorName;
    private boolean chassisClean = true;
    private String chassisNotes = "No scratches or dents";
    private BigDecimal chassisDamageFee = BigDecimal.ZERO;

    private boolean opticsFlawless = true;
    private String opticsNotes = "Optics & glass spotless";
    private BigDecimal opticsDamageFee = BigDecimal.ZERO;

    private boolean electronicsSound = true;
    private String electronicsNotes = "No error codes";
    private BigDecimal electronicsDamageFee = BigDecimal.ZERO;

    private boolean allAccessoriesPresent = true;
    private String accessoriesNotes = "All chargers and cases present";
    private BigDecimal accessoriesMissingFee = BigDecimal.ZERO;

    private boolean operationalPass = true;
    private String operationalNotes = "Field tested 100% operational";
    private BigDecimal operationalDamageFee = BigDecimal.ZERO;

    private List<String> photographicProofs;

    public long getRentalId() { return rentalId; }
    public void setRentalId(long rentalId) { this.rentalId = rentalId; }
    public String getInspectorName() { return inspectorName; }
    public void setInspectorName(String n) { this.inspectorName = n; }
    public boolean isChassisClean() { return chassisClean; }
    public void setChassisClean(boolean b) { this.chassisClean = b; }
    public String getChassisNotes() { return chassisNotes; }
    public void setChassisNotes(String s) { this.chassisNotes = s; }
    public BigDecimal getChassisDamageFee() { return chassisDamageFee; }
    public void setChassisDamageFee(BigDecimal f) { this.chassisDamageFee = f; }
    public boolean isOpticsFlawless() { return opticsFlawless; }
    public void setOpticsFlawless(boolean b) { this.opticsFlawless = b; }
    public String getOpticsNotes() { return opticsNotes; }
    public void setOpticsNotes(String s) { this.opticsNotes = s; }
    public BigDecimal getOpticsDamageFee() { return opticsDamageFee; }
    public void setOpticsDamageFee(BigDecimal f) { this.opticsDamageFee = f; }
    public boolean isElectronicsSound() { return electronicsSound; }
    public void setElectronicsSound(boolean b) { this.electronicsSound = b; }
    public String getElectronicsNotes() { return electronicsNotes; }
    public void setElectronicsNotes(String s) { this.electronicsNotes = s; }
    public BigDecimal getElectronicsDamageFee() { return electronicsDamageFee; }
    public void setElectronicsDamageFee(BigDecimal f) { this.electronicsDamageFee = f; }
    public boolean isAllAccessoriesPresent() { return allAccessoriesPresent; }
    public void setAllAccessoriesPresent(boolean b) { this.allAccessoriesPresent = b; }
    public String getAccessoriesNotes() { return accessoriesNotes; }
    public void setAccessoriesNotes(String s) { this.accessoriesNotes = s; }
    public BigDecimal getAccessoriesMissingFee() { return accessoriesMissingFee; }
    public void setAccessoriesMissingFee(BigDecimal f) { this.accessoriesMissingFee = f; }
    public boolean isOperationalPass() { return operationalPass; }
    public void setOperationalPass(boolean b) { this.operationalPass = b; }
    public String getOperationalNotes() { return operationalNotes; }
    public void setOperationalNotes(String s) { this.operationalNotes = s; }
    public BigDecimal getOperationalDamageFee() { return operationalDamageFee; }
    public void setOperationalDamageFee(BigDecimal f) { this.operationalDamageFee = f; }
    public List<String> getPhotographicProofs() { return photographicProofs; }
    public void setPhotographicProofs(List<String> proofs) { this.photographicProofs = proofs; }
}
""")

    write_file(os.path.join(inspection_dir, "InspectionEvaluation.java"), """package com.rentora.inspection;

import java.math.BigDecimal;
import java.time.Instant;
import java.util.List;

public class InspectionEvaluation {
    private final long rentalId;
    private final String inspectorName;
    private final ConditionGrade grade;
    private final boolean cleanReturn;
    private final BigDecimal totalDamageFee;
    private final List<ChecklistItemResult> itemResults;
    private final List<String> photoUrls;
    private final Instant inspectedAt;

    public InspectionEvaluation(
        long rentalId, String inspectorName, ConditionGrade grade, boolean cleanReturn,
        BigDecimal totalDamageFee, List<ChecklistItemResult> itemResults,
        List<String> photoUrls, Instant inspectedAt
    ) {
        this.rentalId = rentalId;
        this.inspectorName = inspectorName;
        this.grade = grade;
        this.cleanReturn = cleanReturn;
        this.totalDamageFee = totalDamageFee;
        this.itemResults = itemResults;
        this.photoUrls = photoUrls;
        this.inspectedAt = inspectedAt;
    }

    public long getRentalId() { return rentalId; }
    public String getInspectorName() { return inspectorName; }
    public ConditionGrade getGrade() { return grade; }
    public boolean isCleanReturn() { return cleanReturn; }
    public BigDecimal getTotalDamageFee() { return totalDamageFee; }
    public List<ChecklistItemResult> getItemResults() { return itemResults; }
    public List<String> getPhotoUrls() { return photoUrls; }
    public Instant getInspectedAt() { return inspectedAt; }
}
""")

    write_file(os.path.join(inspection_dir, "ChecklistItemResult.java"), """package com.rentora.inspection;

import java.math.BigDecimal;

public class ChecklistItemResult {
    private final String category;
    private final boolean passed;
    private final String observations;
    private final BigDecimal assessedPenalty;

    public ChecklistItemResult(String category, boolean passed, String observations, BigDecimal assessedPenalty) {
        this.category = category;
        this.passed = passed;
        this.observations = observations;
        this.assessedPenalty = assessedPenalty;
    }

    public String getCategory() { return category; }
    public boolean isPassed() { return passed; }
    public String getObservations() { return observations; }
    public BigDecimal getAssessedPenalty() { return assessedPenalty; }
}
""")

    write_file(os.path.join(inspection_dir, "ConditionGrade.java"), """package com.rentora.inspection;

public enum ConditionGrade {
    GRADE_A_PRISTINE,
    GRADE_B_NORMAL_WEAR,
    GRADE_C_DAMAGED,
    GRADE_D_UNUSABLE,
    GRADE_E_TOTAL_LOSS
}
""")

    # --- TAX & GST COMPLIANCE PACKAGE ---
    tax_dir = os.path.join(BACKEND_DIR, "tax")
    
    write_file(os.path.join(tax_dir, "GstComplianceEngine.java"), """package com.rentora.tax;

import java.math.BigDecimal;
import java.math.RoundingMode;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

/**
 * Indian Goods and Services Tax (GST) Automated Determination Engine.
 * Evaluates Intra-State vs. Inter-State commercial leasing transactions under SAC Code 9973.
 */
public class GstComplianceEngine {
    private static final Logger log = LoggerFactory.getLogger(GstComplianceEngine.class);
    public static final String SAC_EQUIPMENT_LEASING = "997314";
    public static final String SAC_VEHICLE_RENTAL = "996601";

    public GstTaxBreakdown calculateTaxes(
            String supplierStateCode,
            String customerStateCode,
            BigDecimal taxableAmount,
            boolean isVehicleRental
    ) {
        if (taxableAmount == null || taxableAmount.compareTo(BigDecimal.ZERO) <= 0) {
            return new GstTaxBreakdown(BigDecimal.ZERO, BigDecimal.ZERO, BigDecimal.ZERO, BigDecimal.ZERO, false);
        }

        boolean isIntraState = supplierStateCode != null && supplierStateCode.equalsIgnoreCase(customerStateCode);
        String sacCode = isVehicleRental ? SAC_VEHICLE_RENTAL : SAC_EQUIPMENT_LEASING;

        BigDecimal cgst = BigDecimal.ZERO;
        BigDecimal sgst = BigDecimal.ZERO;
        BigDecimal igst = BigDecimal.ZERO;

        if (isIntraState) {
            // 9% CGST + 9% SGST = 18%
            cgst = taxableAmount.multiply(new BigDecimal("0.09")).setScale(2, RoundingMode.HALF_UP);
            sgst = taxableAmount.multiply(new BigDecimal("0.09")).setScale(2, RoundingMode.HALF_UP);
        } else {
            // 18% IGST
            igst = taxableAmount.multiply(new BigDecimal("0.18")).setScale(2, RoundingMode.HALF_UP);
        }

        BigDecimal totalTax = cgst.add(sgst).add(igst);
        log.debug("GST computed: Taxable INR {}, IntraState: {}, CGST: {}, SGST: {}, IGST: {}, SAC: {}",
            taxableAmount, isIntraState, cgst, sgst, igst, sacCode);

        return new GstTaxBreakdown(cgst, sgst, igst, totalTax, isIntraState);
    }
}
""")

    write_file(os.path.join(tax_dir, "GstTaxBreakdown.java"), """package com.rentora.tax;

import java.math.BigDecimal;

public class GstTaxBreakdown {
    private final BigDecimal cgst;
    private final BigDecimal sgst;
    private final BigDecimal igst;
    private final BigDecimal totalTax;
    private final boolean intraState;

    public GstTaxBreakdown(BigDecimal cgst, BigDecimal sgst, BigDecimal igst, BigDecimal totalTax, boolean intraState) {
        this.cgst = cgst;
        this.sgst = sgst;
        this.igst = igst;
        this.totalTax = totalTax;
        this.intraState = intraState;
    }

    public BigDecimal getCgst() { return cgst; }
    public BigDecimal getSgst() { return sgst; }
    public BigDecimal getIgst() { return igst; }
    public BigDecimal getTotalTax() { return totalTax; }
    public boolean isIntraState() { return intraState; }
}
""")

    write_file(os.path.join(tax_dir, "CommercialInvoiceGenerator.java"), """package com.rentora.tax;

import java.math.BigDecimal;
import java.time.LocalDate;
import java.util.UUID;

public class CommercialInvoiceGenerator {

    public CommercialInvoice generateInvoice(
            long rentalId,
            String customerName,
            String customerGstin,
            String vendorBusinessName,
            String vendorGstin,
            BigDecimal rentAmount,
            GstTaxBreakdown tax
    ) {
        String invoiceNumber = "INV-RENT-" + LocalDate.now().getYear() + "-" + (10000 + (rentalId % 90000));
        BigDecimal totalPayable = rentAmount.add(tax.getTotalTax());

        return new CommercialInvoice(
            invoiceNumber,
            rentalId,
            LocalDate.now(),
            customerName,
            customerGstin,
            vendorBusinessName,
            vendorGstin,
            rentAmount,
            tax.getCgst(),
            tax.getSgst(),
            tax.getIgst(),
            tax.getTotalTax(),
            totalPayable
        );
    }
}
""")

    write_file(os.path.join(tax_dir, "CommercialInvoice.java"), """package com.rentora.tax;

import java.math.BigDecimal;
import java.time.LocalDate;

public class CommercialInvoice {
    private final String invoiceNumber;
    private final long rentalId;
    private final LocalDate invoiceDate;
    private final String customerName;
    private final String customerGstin;
    private final String vendorBusinessName;
    private final String vendorGstin;
    private final BigDecimal taxableRent;
    private final BigDecimal cgst;
    private final BigDecimal sgst;
    private final BigDecimal igst;
    private final BigDecimal totalGst;
    private final BigDecimal totalAmount;

    public CommercialInvoice(
        String invoiceNumber, long rentalId, LocalDate invoiceDate, String customerName,
        String customerGstin, String vendorBusinessName, String vendorGstin,
        BigDecimal taxableRent, BigDecimal cgst, BigDecimal sgst, BigDecimal igst,
        BigDecimal totalGst, BigDecimal totalAmount
    ) {
        this.invoiceNumber = invoiceNumber;
        this.rentalId = rentalId;
        this.invoiceDate = invoiceDate;
        this.customerName = customerName;
        this.customerGstin = customerGstin;
        this.vendorBusinessName = vendorBusinessName;
        this.vendorGstin = vendorGstin;
        this.taxableRent = taxableRent;
        this.cgst = cgst;
        this.sgst = sgst;
        this.igst = igst;
        this.totalGst = totalGst;
        this.totalAmount = totalAmount;
    }

    public String getInvoiceNumber() { return invoiceNumber; }
    public long getRentalId() { return rentalId; }
    public LocalDate getInvoiceDate() { return invoiceDate; }
    public String getCustomerName() { return customerName; }
    public String getCustomerGstin() { return customerGstin; }
    public String getVendorBusinessName() { return vendorBusinessName; }
    public String getVendorGstin() { return vendorGstin; }
    public BigDecimal getTaxableRent() { return taxableRent; }
    public BigDecimal getCgst() { return cgst; }
    public BigDecimal getSgst() { return sgst; }
    public BigDecimal getIgst() { return igst; }
    public BigDecimal getTotalGst() { return totalGst; }
    public BigDecimal getTotalAmount() { return totalAmount; }
}
""")

    # --- ANALYTICS PACKAGE ---
    analytics_dir = os.path.join(BACKEND_DIR, "analytics")

    write_file(os.path.join(analytics_dir, "BusinessIntelligenceAggregator.java"), """package com.rentora.analytics;

import java.math.BigDecimal;
import java.math.RoundingMode;
import java.util.*;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class BusinessIntelligenceAggregator {
    private static final Logger log = LoggerFactory.getLogger(BusinessIntelligenceAggregator.class);

    public PlatformMetrics computePlatformHealth(List<OrderMetricSample> samples) {
        if (samples == null || samples.isEmpty()) {
            return new PlatformMetrics(BigDecimal.ZERO, 0, BigDecimal.ZERO, 100.0, 0.0);
        }

        BigDecimal totalGmv = BigDecimal.ZERO;
        int totalBookings = samples.size();
        int disputeCount = 0;

        for (OrderMetricSample sample : samples) {
            totalGmv = totalGmv.add(sample.getOrderAmount());
            if (sample.isDisputed()) {
                disputeCount++;
            }
        }

        BigDecimal avgOrderValue = totalGmv.divide(BigDecimal.valueOf(totalBookings), 2, RoundingMode.HALF_UP);
        double disputeFreeRate = 100.0 - (((double) disputeCount / totalBookings) * 100.0);
        double takeRateCommission = 10.0; // 10% platform take rate

        log.info("Platform Health aggregated: GMV INR {}, Bookings {}, Dispute-free: {}%",
            totalGmv, totalBookings, disputeFreeRate);

        return new PlatformMetrics(totalGmv, totalBookings, avgOrderValue, disputeFreeRate, takeRateCommission);
    }
}
""")

    write_file(os.path.join(analytics_dir, "PlatformMetrics.java"), """package com.rentora.analytics;

import java.math.BigDecimal;

public class PlatformMetrics {
    private final BigDecimal totalGmv;
    private final int totalBookings;
    private final BigDecimal averageOrderValue;
    private final double disputeFreePercent;
    private final double platformTakeRatePercent;

    public PlatformMetrics(BigDecimal totalGmv, int totalBookings, BigDecimal averageOrderValue, double disputeFreePercent, double platformTakeRatePercent) {
        this.totalGmv = totalGmv;
        this.totalBookings = totalBookings;
        this.averageOrderValue = averageOrderValue;
        this.disputeFreePercent = disputeFreePercent;
        this.platformTakeRatePercent = platformTakeRatePercent;
    }

    public BigDecimal getTotalGmv() { return totalGmv; }
    public int getTotalBookings() { return totalBookings; }
    public BigDecimal getAverageOrderValue() { return averageOrderValue; }
    public double getDisputeFreePercent() { return disputeFreePercent; }
    public double getPlatformTakeRatePercent() { return platformTakeRatePercent; }
}
""")

    write_file(os.path.join(analytics_dir, "OrderMetricSample.java"), """package com.rentora.analytics;

import java.math.BigDecimal;

public class OrderMetricSample {
    private final long orderId;
    private final BigDecimal orderAmount;
    private final boolean disputed;

    public OrderMetricSample(long orderId, BigDecimal orderAmount, boolean disputed) {
        this.orderId = orderId;
        this.orderAmount = orderAmount;
        this.disputed = disputed;
    }

    public long getOrderId() { return orderId; }
    public BigDecimal getOrderAmount() { return orderAmount; }
    public boolean isDisputed() { return disputed; }
}
""")

    print("--> Java enterprise packages successfully generated.")

# =============================================================================
# 2. PYTHON MICROSERVICES GENERATOR
# =============================================================================

def build_python_services():
    print("\n--> Building Enterprise Python Services...")

    # 2.1 Telematics Engine Microservice
    telematics_engine_dir = os.path.join(SERVICES_DIR, "telematics_engine")
    
    write_file(os.path.join(telematics_engine_dir, "telematics_stream_parser.py"), '''"""
Rentora High-Frequency Telematics Data Stream Parser
Processes binary/JSON CAN bus telemetry packets from OBD-II vehicle transponders.
"""

import json
import math
import logging
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Dict, List, Optional, Tuple

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] [TelematicsStream] %(message)s")
logger = logging.getLogger("telematics-stream")

@dataclass
class TelematicsPacket:
    vin: str
    latitude: float
    longitude: float
    speed_kmh: float
    heading_deg: float
    odometer_km: float
    fuel_level_pct: float
    engine_temp_c: float
    engine_rpm: float
    battery_v: float
    ignition_on: bool
    timestamp: datetime = field(default_factory=lambda: datetime.now(timezone.utc))

class TelematicsStreamParser:
    """Decodes live vehicle telemetry streams and performs anomaly threshold detection."""

    def __init__(self, max_speed_kmh: float = 120.0, severe_temp_c: float = 105.0):
        self.max_speed_kmh = max_speed_kmh
        self.severe_temp_c = severe_temp_c
        self.recent_breadcrumbs: Dict[str, List[Tuple[float, float, datetime]]] = {}

    def parse_raw_payload(self, raw_data: bytes) -> Optional[TelematicsPacket]:
        try:
            payload = json.loads(raw_data.decode("utf-8"))
            packet = TelematicsPacket(
                vin=payload["vin"],
                latitude=float(payload["lat"]),
                longitude=float(payload["lon"]),
                speed_kmh=float(payload["speed"]),
                heading_deg=float(payload.get("heading", 0.0)),
                odometer_km=float(payload.get("odometer", 0.0)),
                fuel_level_pct=float(payload.get("fuel", 100.0)),
                engine_temp_c=float(payload.get("temp", 90.0)),
                engine_rpm=float(payload.get("rpm", 1500.0)),
                battery_v=float(payload.get("battery", 13.6)),
                ignition_on=bool(payload.get("ignition", True)),
                timestamp=datetime.fromisoformat(payload["time"]) if "time" in payload else datetime.now(timezone.utc)
            )
            self._record_breadcrumb(packet)
            return packet
        except Exception as ex:
            logger.error(f"Failed to parse incoming telematics payload: {ex}")
            return None

    def _record_breadcrumb(self, packet: TelematicsPacket):
        if packet.vin not in self.recent_breadcrumbs:
            self.recent_breadcrumbs[packet.vin] = []
        history = self.recent_breadcrumbs[packet.vin]
        history.append((packet.latitude, packet.longitude, packet.timestamp))
        if len(history) > 1000:
            history.pop(0)

    def detect_violations(self, packet: TelematicsPacket) -> List[Dict[str, any]]:
        violations = []
        if packet.speed_kmh > self.max_speed_kmh:
            violations.append({
                "type": "SPEED_LIMIT_BREACH",
                "severity": "CRITICAL" if packet.speed_kmh > 140 else "WARNING",
                "message": f"Vehicle exceeding max speed: {packet.speed_kmh:.1f} km/h (Limit: {self.max_speed_kmh:.1f})"
            })
        if packet.engine_temp_c > self.severe_temp_c:
            violations.append({
                "type": "ENGINE_OVERHEAT",
                "severity": "HIGH",
                "message": f"Engine coolant temperature high: {packet.engine_temp_c:.1f} C"
            })
        if packet.battery_v < 11.5:
            violations.append({
                "type": "LOW_BATTERY",
                "severity": "WARNING",
                "message": f"12V battery discharged: {packet.battery_v:.2f} V"
            })
        return violations

    def compute_travel_distance_km(self, vin: str) -> float:
        points = self.recent_breadcrumbs.get(vin, [])
        if len(points) < 2:
            return 0.0
        total_km = 0.0
        for i in range(1, len(points)):
            lat1, lon1, _ = points[i - 1]
            lat2, lon2, _ = points[i]
            total_km += self._haversine(lat1, lon1, lat2, lon2)
        return round(total_km, 2)

    @staticmethod
    def _haversine(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
        r = 6371.0  # Earth radius km
        d_lat = math.radians(lat2 - lat1)
        d_lon = math.radians(lon2 - lon1)
        a = math.sin(d_lat / 2.0) ** 2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(d_lon / 2.0) ** 2
        c = 2.0 * math.atan2(math.sqrt(a), math.sqrt(1.0 - a))
        return r * c
''')

    write_file(os.path.join(telematics_engine_dir, "geofence_spatial_engine.py"), '''"""
Rentora Geofencing & Spatial Zone Compliance Engine
Monitors vehicle location against allowed operating boundaries (e.g. state border restrictions).
"""

import math
from typing import List, Tuple

class GeofencePolygon:
    def __init__(self, zone_id: str, name: str, vertices: List[Tuple[float, float]]):
        self.zone_id = zone_id
        self.name = name
        self.vertices = vertices

    def contains(self, lat: float, lon: float) -> bool:
        """Ray-casting algorithm to determine if (lat, lon) is inside polygon boundary."""
        n = len(self.vertices)
        inside = False
        p1x, p1y = self.vertices[0]
        for i in range(n + 1):
            p2x, p2y = self.vertices[i % n]
            if lat > min(p1x, p2x):
                if lat <= max(p1x, p2x):
                    if lon <= max(p1y, p2y):
                        if p1x != p2x:
                            xinters = (lat - p1x) * (p2y - p1y) / (p2x - p1x) + p1y
                        if p1y == p2y or lon <= xinters:
                            inside = not inside
            p1x, p1y = p2x, p2y
        return inside

class GeofenceSpatialEngine:
    def __init__(self):
        self.registered_zones: List[GeofencePolygon] = []
        self._init_default_zones()

    def _init_default_zones(self):
        # Default Karnataka State perimeter zone approx
        karnataka_bounds = [
            (11.5, 75.0), (15.5, 74.0), (18.5, 77.0), (16.0, 78.5), (12.0, 77.5)
        ]
        self.registered_zones.append(GeofencePolygon("KA-STATE", "Karnataka State Zone", karnataka_bounds))

    def check_position(self, lat: float, lon: float) -> Tuple[bool, str]:
        for zone in self.registered_zones:
            if zone.contains(lat, lon):
                return True, zone.name
        return False, "OUT_OF_BOUNDS"
''')

    write_file(os.path.join(telematics_engine_dir, "telematics_api_server.py"), '''"""
FastAPI / Python Entry Point for Telematics Microservice
"""

from telematics_stream_parser import TelematicsStreamParser
from geofence_spatial_engine import GeofenceSpatialEngine

class TelematicsEngineService:
    def __init__(self):
        self.parser = TelematicsStreamParser()
        self.geofence = GeofenceSpatialEngine()

    def get_service_status(self):
        return {
            "service": "rentora-telematics-engine",
            "status": "HEALTHY",
            "active_monitored_vin_count": len(self.parser.recent_breadcrumbs)
        }

if __name__ == "__main__":
    svc = TelematicsEngineService()
    print("Telematics Engine Service initialized:", svc.get_service_status())
''')

    # 2.2 Pricing AI Engine Microservice
    pricing_engine_dir = os.path.join(SERVICES_DIR, "pricing_engine")

    write_file(os.path.join(pricing_engine_dir, "pricing_optimizer.py"), '''"""
Rentora Real-Time Pricing Intelligence & Elasticity Optimizer
Calculates dynamic rental yields, competitor adjustments, and seasonal elasticity.
"""

from datetime import date, timedelta
from typing import Dict, List, Optional

class PricingOptimizer:
    def __init__(self):
        self.base_elasticity_curve = {
            "luxury_car": 0.85,
            "superbike": 0.90,
            "cinema_camera": 0.70,
            "drone": 0.75,
            "power_tool": 0.95
        }

    def compute_optimized_rate(
        self,
        base_rate: float,
        category: str,
        days: int,
        lead_time_days: int,
        fleet_utilization_pct: float
    ) -> Dict[str, float]:
        elasticity = self.base_elasticity_curve.get(category, 0.80)
        
        # Duration factor
        if days >= 30:
            duration_mult = 0.70  # 30% discount
        elif days >= 14:
            duration_mult = 0.80  # 20% discount
        elif days >= 7:
            duration_mult = 0.85  # 15% discount
        elif days >= 3:
            duration_mult = 0.95  # 5% discount
        else:
            duration_mult = 1.0

        # Demand pressure multiplier
        if fleet_utilization_pct >= 90.0:
            demand_mult = 1.25
        elif fleet_utilization_pct >= 75.0:
            demand_mult = 1.10
        elif fleet_utilization_pct <= 30.0:
            demand_mult = 0.90  # Stimulate low-demand periods
        else:
            demand_mult = 1.0

        # Last-minute booking surcharge
        lead_time_mult = 1.08 if lead_time_days <= 1 else 1.0

        daily_rate = round(base_rate * duration_mult * demand_mult * lead_time_mult, 2)
        total_rent = round(daily_rate * days, 2)

        return {
            "base_rate": base_rate,
            "optimized_daily_rate": daily_rate,
            "duration_multiplier": duration_mult,
            "demand_multiplier": demand_mult,
            "lead_time_multiplier": lead_time_mult,
            "total_rent": total_rent
        }
''')

    write_file(os.path.join(pricing_engine_dir, "pricing_api_server.py"), '''"""
Rentora Pricing API Entry point
"""

from pricing_optimizer import PricingOptimizer

if __name__ == "__main__":
    optimizer = PricingOptimizer()
    sample = optimizer.compute_optimized_rate(
        base_rate=3800.0, category="luxury_car", days=4, lead_time_days=2, fleet_utilization_pct=85.0
    )
    print("Sample Pricing Optimization Quote:", sample)
''')

    # 2.3 Inspection AI Microservice
    inspection_ai_dir = os.path.join(SERVICES_DIR, "inspection_ai")

    write_file(os.path.join(inspection_ai_dir, "damage_vision_comparator.py"), '''"""
Rentora Computer Vision Photographic Inspection Comparator
Simulates optical surface difference detection, scratch detection, and dent appraisal.
"""

from dataclasses import dataclass
from typing import List, Dict, Optional

@dataclass
class DetectedAnomaly:
    region_label: str
    severity: str
    confidence: float
    estimated_repair_cost: float
    description: str

class DamageVisionComparator:
    def __init__(self):
        self.standard_repair_matrix = {
            "bumper_scratch": 1800.0,
            "door_dent": 3500.0,
            "windshield_chip": 2500.0,
            "wheel_rim_curb_scuff": 1200.0,
            "camera_sensor_dust": 800.0,
            "lens_element_scratch": 6500.0
        }

    def compare_inspection_images(self, pre_rental_photo_url: str, post_rental_photo_url: str) -> List[DetectedAnomaly]:
        # Simulates image diff analysis and optical difference verification
        if "damage" in post_rental_photo_url.lower():
            return [
                DetectedAnomaly(
                    region_label="REAR_BUMPER",
                    severity="MODERATE",
                    confidence=0.94,
                    estimated_repair_cost=self.standard_repair_matrix["bumper_scratch"],
                    description="Surface scuff mark detected on lower rear bumper diffuser"
                )
            ]
        return []
''')

    write_file(os.path.join(inspection_ai_dir, "inspection_api_server.py"), '''"""
Inspection AI microservice entry point
"""

from damage_vision_comparator import DamageVisionComparator

if __name__ == "__main__":
    comparator = DamageVisionComparator()
    print("Inspection AI Comparator initialized successfully.")
''')

    # 2.4 Escrow Ledger Microservice
    escrow_ledger_dir = os.path.join(SERVICES_DIR, "escrow_ledger")

    write_file(os.path.join(escrow_ledger_dir, "cryptographic_audit_chain.py"), '''"""
Cryptographic Tamper-Evident Ledger Audit Chain for Escrow Security Deposits
"""

import hashlib
import json
from datetime import datetime, timezone
from typing import List, Dict

class AuditBlock:
    def __init__(self, index: int, data: Dict, previous_hash: str):
        self.index = index
        self.timestamp = datetime.now(timezone.utc).isoformat()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.compute_hash()

    def compute_hash(self) -> str:
        block_content = f"{self.index}|{self.timestamp}|{json.dumps(self.data, sort_keys=True)}|{self.previous_hash}"
        return hashlib.sha256(block_content.encode("utf-8")).hexdigest()

class CryptographicAuditChain:
    def __init__(self):
        self.chain: List[AuditBlock] = []
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis = AuditBlock(0, {"event": "GENESIS_ESCROW_LEDGER"}, "0" * 64)
        self.chain.append(genesis)

    def append_event(self, event_data: Dict) -> AuditBlock:
        prev_hash = self.chain[-1].hash
        new_block = AuditBlock(len(self.chain), event_data, prev_hash)
        self.chain.append(new_block)
        return new_block

    def verify_chain_validity(self) -> bool:
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            prev = self.chain[i - 1]
            if current.previous_hash != prev.hash:
                return False
            if current.hash != current.compute_hash():
                return False
        return True
''')

    print("--> Python microservices generated.")

# =============================================================================
# 3. REACT FRONTEND ENTERPRISE MODULES GENERATOR
# =============================================================================

def build_react_modules():
    print("\n--> Building Enterprise React Modules...")

    # 3.1 Fleet Telematics UI Components
    fleet_dir = os.path.join(FRONTEND_DIR, "components", "fleet")
    
    write_file(os.path.join(fleet_dir, "LiveFleetTelematicsMap.jsx"), """import React, { useState, useEffect } from 'react';
import { Navigation, MapPin, Gauge, Battery, ShieldAlert, CheckCircle, RefreshCw, Car, Bike } from 'lucide-react';
import { motion } from 'framer-motion';

export default function LiveFleetTelematicsMap({ selectedVehicleVin }) {
  const [vehicles, setVehicles] = useState([
    {
      vin: 'VIN-THAR-4X4-8821',
      model: 'Mahindra Thar 4x4 Hard-Top',
      type: 'CAR',
      driver: 'Arjun Namboodiri',
      lat: 12.9716,
      lon: 77.5946,
      speedKmh: 64,
      fuelPct: 82,
      batteryV: 13.8,
      status: 'ON_TRIP',
      zone: 'Bengaluru Metro Permitted'
    },
    {
      vin: 'VIN-BMW-330I-1049',
      model: 'BMW 330i M-Sport',
      type: 'CAR',
      driver: 'Kavita Menon',
      lat: 19.0760,
      lon: 72.8777,
      speedKmh: 48,
      fuelPct: 94,
      batteryV: 14.1,
      status: 'ON_TRIP',
      zone: 'Mumbai Coastal Corridor'
    },
    {
      vin: 'VIN-HIMALAYAN-450-993',
      model: 'Royal Enfield Himalayan 450',
      type: 'BIKE',
      driver: 'Rahul Sharma',
      lat: 11.4102,
      lon: 76.6950,
      speedKmh: 58,
      fuelPct: 76,
      batteryV: 13.5,
      status: 'ON_TRIP',
      zone: 'Nilgiris Adventure Loop'
    },
    {
      vin: 'VIN-NINJA-ZX6R-441',
      model: 'Kawasaki Ninja ZX-6R',
      type: 'BIKE',
      driver: 'Devansh Kulkarni',
      lat: 13.0827,
      lon: 80.2707,
      speedKmh: 0,
      fuelPct: 65,
      batteryV: 13.2,
      status: 'PARKED_SAFE',
      zone: 'Irungattukottai Track Paddock'
    }
  ]);

  const [activeVin, setActiveVin] = useState(selectedVehicleVin || 'VIN-THAR-4X4-8821');
  const activeVehicle = vehicles.find(v => v.vin === activeVin) || vehicles[0];

  return (
    <div className="bg-white rounded-3xl border border-gray-200/80 shadow-card p-6 space-y-6">
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 pb-4 border-b border-gray-100">
        <div>
          <span className="text-xs font-bold uppercase tracking-wider text-emerald-700 flex items-center space-x-1.5">
            <Navigation className="w-3.5 h-3.5" />
            <span>IoT CAN-Bus Telemetry</span>
          </span>
          <h3 className="text-xl font-bold font-display text-gray-900 mt-0.5">
            Live Fleet Radar &amp; Geofence Watchdog
          </h3>
        </div>

        <div className="flex items-center space-x-2">
          <span className="inline-flex items-center space-x-1.5 px-3 py-1 rounded-full bg-emerald-50 text-emerald-800 text-xs font-semibold">
            <span className="w-2 h-2 rounded-full bg-emerald-500 animate-ping"></span>
            <span>4 Vehicles Streaming</span>
          </span>
        </div>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        {/* Vehicle Selection List */}
        <div className="space-y-2.5">
          <label className="text-xs font-bold text-gray-600 uppercase tracking-wider block">
            Active Monitored Fleet
          </label>
          {vehicles.map(v => (
            <button
              key={v.vin}
              onClick={() => setActiveVin(v.vin)}
              className={`w-full p-4 rounded-2xl text-left border transition-all flex items-center justify-between ${
                activeVin === v.vin
                  ? 'border-forest-900 bg-forest-50/50 shadow-sm ring-1 ring-forest-900/10'
                  : 'border-gray-100 hover:border-gray-200 bg-white'
              }`}
            >
              <div className="flex items-center space-x-3">
                <div className="w-10 h-10 rounded-xl bg-forest-900 text-white flex items-center justify-center shrink-0">
                  {v.type === 'CAR' ? <Car className="w-5 h-5" /> : <Bike className="w-5 h-5" />}
                </div>
                <div>
                  <h4 className="text-xs font-bold text-gray-900">{v.model}</h4>
                  <p className="text-[11px] text-gray-500">Renter: {v.driver}</p>
                </div>
              </div>
              <div className="text-right">
                <span className="text-xs font-extrabold text-forest-900">{v.speedKmh} km/h</span>
                <p className="text-[10px] text-emerald-600 font-semibold">{v.status}</p>
              </div>
            </button>
          ))}
        </div>

        {/* Live Gauges & Telemetry Detail */}
        <div className="lg:col-span-2 bg-sand-100/60 p-6 rounded-2xl border border-gray-200/80 space-y-6">
          <div className="flex items-center justify-between">
            <div>
              <h4 className="text-sm font-bold text-gray-900">{activeVehicle.model}</h4>
              <p className="text-xs text-gray-500 font-mono mt-0.5">VIN: {activeVehicle.vin}</p>
            </div>
            <div className="flex items-center space-x-1.5 px-3 py-1 rounded-full bg-white border border-gray-200 text-xs font-semibold text-gray-700">
              <MapPin className="w-3.5 h-3.5 text-emerald-600" />
              <span>{activeVehicle.zone}</span>
            </div>
          </div>

          <div className="grid grid-cols-2 sm:grid-cols-4 gap-4">
            <div className="bg-white p-4 rounded-xl border border-gray-100 shadow-sm text-center">
              <Gauge className="w-5 h-5 text-emerald-600 mx-auto mb-1" />
              <p className="text-2xl font-black font-display text-gray-900">{activeVehicle.speedKmh}</p>
              <p className="text-[10px] font-semibold text-gray-400 uppercase">Current Speed</p>
            </div>

            <div className="bg-white p-4 rounded-xl border border-gray-100 shadow-sm text-center">
              <span className="text-emerald-600 font-bold text-lg block mb-1">⛽</span>
              <p className="text-2xl font-black font-display text-gray-900">{activeVehicle.fuelPct}%</p>
              <p className="text-[10px] font-semibold text-gray-400 uppercase">Fuel Level</p>
            </div>

            <div className="bg-white p-4 rounded-xl border border-gray-100 shadow-sm text-center">
              <Battery className="w-5 h-5 text-emerald-600 mx-auto mb-1" />
              <p className="text-2xl font-black font-display text-gray-900">{activeVehicle.batteryV} V</p>
              <p className="text-[10px] font-semibold text-gray-400 uppercase">Aux Battery</p>
            </div>

            <div className="bg-white p-4 rounded-xl border border-gray-100 shadow-sm text-center">
              <CheckCircle className="w-5 h-5 text-gold-500 mx-auto mb-1" />
              <p className="text-2xl font-black font-display text-gray-900">0</p>
              <p className="text-[10px] font-semibold text-gray-400 uppercase">Active Faults</p>
            </div>
          </div>

          {/* Simulated Map Coordinates Radar Box */}
          <div className="h-44 rounded-xl bg-forest-950 text-white flex flex-col items-center justify-center relative overflow-hidden p-4 text-center">
            <div className="absolute inset-0 opacity-20 bg-[radial-gradient(#10B981_1px,transparent_1px)] [background-size:16px_16px]"></div>
            <Navigation className="w-8 h-8 text-emerald-400 animate-pulse mb-2 z-10" />
            <p className="text-xs font-semibold z-10 text-emerald-300">Live Satellite GPS Fix Locked</p>
            <p className="text-[11px] font-mono text-gray-400 z-10 mt-1">
              Latitude: {activeVehicle.lat.toFixed(4)}° N • Longitude: {activeVehicle.lon.toFixed(4)}° E
            </p>
          </div>
        </div>
      </div>
    </div>
  );
}
""")

    # 3.2 Interactive Damage Annotation Canvas
    inspection_ui_dir = os.path.join(FRONTEND_DIR, "components", "inspection")

    write_file(os.path.join(inspection_ui_dir, "InteractiveDamageAnnotationCanvas.jsx"), """import React, { useState } from 'react';
import { Camera, AlertCircle, CheckCircle2, ShieldCheck, Tag, Trash2, Plus } from 'lucide-react';

export default function InteractiveDamageAnnotationCanvas({ rentalId = 1001, onAssessmentComplete }) {
  const [annotations, setAnnotations] = useState([
    { id: 1, x: 38, y: 52, part: 'Front Bumper Diffuser', note: 'Minor surface stone-chip', severity: 'MILD', fee: 0 }
  ]);

  const [selectedPart, setSelectedPart] = useState('Front Bumper');
  const [noteText, setNoteText] = useState('');
  const [damageFee, setDamageFee] = useState(0);

  const handleCanvasClick = (e) => {
    const rect = e.currentTarget.getBoundingClientRect();
    const x = Math.round(((e.clientX - rect.left) / rect.width) * 100);
    const y = Math.round(((e.clientY - rect.top) / rect.height) * 100);

    const newMarker = {
      id: Date.now(),
      x,
      y,
      part: selectedPart,
      note: noteText || 'Inspected checkpoint',
      severity: damageFee > 0 ? 'NEEDS_REPAIR' : 'MILD',
      fee: Number(damageFee) || 0
    };

    setAnnotations([...annotations, newMarker]);
    setNoteText('');
    setDamageFee(0);
  };

  const removeMarker = (id) => {
    setAnnotations(annotations.filter(a => a.id !== id));
  };

  const totalDamageFee = annotations.reduce((sum, a) => sum + a.fee, 0);

  return (
    <div className="bg-white rounded-3xl border border-gray-200/80 shadow-card p-6 space-y-6">
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 pb-4 border-b border-gray-100">
        <div>
          <span className="text-xs font-bold uppercase tracking-wider text-emerald-700 flex items-center space-x-1.5">
            <ShieldCheck className="w-3.5 h-3.5" />
            <span>Digital 5-Point Check</span>
          </span>
          <h3 className="text-xl font-bold font-display text-gray-900 mt-0.5">
            Vehicle &amp; Gear Damage Annotation Canvas
          </h3>
        </div>

        <div className="flex items-center space-x-3">
          <span className="text-xs font-bold text-gray-500">Total Deduction:</span>
          <span className="text-base font-extrabold text-forest-900">₹{totalDamageFee.toLocaleString('en-IN')}</span>
        </div>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        {/* Interactive Coordinate Canvas */}
        <div className="lg:col-span-2 space-y-3">
          <p className="text-xs text-gray-500">
            Click anywhere on the schematic canvas to pin an inspection observation tag:
          </p>

          <div
            onClick={handleCanvasClick}
            className="w-full h-80 rounded-2xl bg-gradient-to-b from-gray-100 to-gray-200 border-2 border-dashed border-gray-300 relative overflow-hidden cursor-crosshair flex items-center justify-center group"
          >
            {/* Blueprint Wireframe Grid */}
            <div className="absolute inset-0 opacity-15 bg-[radial-gradient(#000_1px,transparent_1px)] [background-size:20px_20px]"></div>

            <div className="text-center pointer-events-none opacity-40">
              <Camera className="w-12 h-12 mx-auto mb-2 text-gray-600" />
              <p className="text-xs font-bold uppercase tracking-widest text-gray-700">Vehicle / Rig 360° Schematic</p>
            </div>

            {/* Render Pinned Damage Annotations */}
            {annotations.map(a => (
              <div
                key={a.id}
                style={{ left: `${a.x}%`, top: `${a.y}%` }}
                className="absolute -translate-x-1/2 -translate-y-1/2 group/marker z-10"
              >
                <span className={`w-6 h-6 rounded-full flex items-center justify-center text-white text-[10px] font-bold shadow-md cursor-pointer ${
                  a.fee > 0 ? 'bg-red-500 animate-bounce' : 'bg-emerald-600'
                }`}>
                  !
                </span>
                <div className="hidden group-hover/marker:block absolute bottom-8 left-1/2 -translate-x-1/2 bg-gray-900 text-white text-[11px] p-2 rounded-xl whitespace-nowrap z-20 shadow-lg">
                  <p className="font-bold">{a.part}</p>
                  <p className="text-gray-300">{a.note}</p>
                  {a.fee > 0 && <p className="text-red-400 font-bold">Penalty: ₹{a.fee}</p>}
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* Observation Tagging Form */}
        <div className="bg-sand-100/60 p-5 rounded-2xl border border-gray-200/80 space-y-4">
          <h4 className="text-xs font-bold uppercase tracking-wider text-gray-700">
            Observation Details
          </h4>

          <div>
            <label className="text-xs font-semibold text-gray-700 block mb-1">Inspected Part</label>
            <select
              value={selectedPart}
              onChange={(e) => setSelectedPart(e.target.value)}
              className="w-full text-xs p-2.5 rounded-xl border border-gray-200 bg-white font-medium focus:outline-none"
            >
              <option value="Front Bumper">Front Bumper &amp; Grill</option>
              <option value="Windshield">Windshield &amp; Wipers</option>
              <option value="Alloy Wheels">Alloy Wheels &amp; Tyres</option>
              <option value="Side Doors">Side Doors &amp; Paint</option>
              <option value="Rear Diffuser">Rear Diffuser &amp; Boot</option>
              <option value="Interior Cabin">Interior Seats &amp; Infotainment</option>
            </select>
          </div>

          <div>
            <label className="text-xs font-semibold text-gray-700 block mb-1">Notes / Description</label>
            <input
              type="text"
              placeholder="e.g. Scratch on clear-coat..."
              value={noteText}
              onChange={(e) => setNoteText(e.target.value)}
              className="w-full text-xs p-2.5 rounded-xl border border-gray-200 bg-white focus:outline-none"
            />
          </div>

          <div>
            <label className="text-xs font-semibold text-gray-700 block mb-1">Assessed Penalty Fee (₹)</label>
            <input
              type="number"
              min="0"
              step="100"
              placeholder="0 for normal wear"
              value={damageFee}
              onChange={(e) => setDamageFee(e.target.value)}
              className="w-full text-xs p-2.5 rounded-xl border border-gray-200 bg-white focus:outline-none font-bold"
            />
          </div>

          {/* List of Marked Annotations */}
          <div className="pt-2 border-t border-gray-200 space-y-2">
            <span className="text-[11px] font-bold text-gray-500 uppercase">Logged Points ({annotations.length})</span>
            <div className="max-h-36 overflow-y-auto space-y-1.5">
              {annotations.map(a => (
                <div key={a.id} className="flex items-center justify-between p-2 rounded-lg bg-white text-xs border border-gray-100">
                  <div>
                    <span className="font-bold text-gray-800">{a.part}</span>
                    <p className="text-[10px] text-gray-500">{a.note}</p>
                  </div>
                  <button onClick={() => removeMarker(a.id)} className="text-red-500 hover:text-red-700 p-1">
                    <Trash2 className="w-3.5 h-3.5" />
                  </button>
                </div>
              ))}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
""")

    print("--> React enterprise modules generated.")

def main():
    print("=" * 80)
    print("Rentora Enterprise Platform Expansion Builder")
    print("=" * 80)
    build_java_modules()
    build_python_services()
    build_react_modules()
    print("\nAll enterprise modules built successfully!")

if __name__ == "__main__":
    main()
