package com.rentora.escrow;

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
