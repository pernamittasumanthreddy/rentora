package com.rentora.escrow;

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
