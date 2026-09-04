package com.rentora.escrow;

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
