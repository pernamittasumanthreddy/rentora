package com.rentora.compliance;

import java.time.Instant;

public class NodalAccountAuditRule {
    private final long rentalId;
    private final int auditCheckpoint;
    private final double nodalPoolBalance;
    private final double liabilityReserve;
    private final boolean reserveAdequate;
    private final double coverageRatio;
    private final String complianceStatus;
    private final Instant verifiedAt;

    public NodalAccountAuditRule(long rentalId, int auditCheckpoint, double nodalPoolBalance, double liabilityReserve, boolean reserveAdequate, double coverageRatio, String complianceStatus, Instant verifiedAt) {
        this.rentalId = rentalId;
        this.auditCheckpoint = auditCheckpoint;
        this.nodalPoolBalance = nodalPoolBalance;
        this.liabilityReserve = liabilityReserve;
        this.reserveAdequate = reserveAdequate;
        this.coverageRatio = coverageRatio;
        this.complianceStatus = complianceStatus;
        this.verifiedAt = verifiedAt;
    }

    public long getRentalId() { return rentalId; }
    public int getAuditCheckpoint() { return auditCheckpoint; }
    public double getNodalPoolBalance() { return nodalPoolBalance; }
    public double getLiabilityReserve() { return liabilityReserve; }
    public boolean isReserveAdequate() { return reserveAdequate; }
    public double getCoverageRatio() { return coverageRatio; }
    public String getComplianceStatus() { return complianceStatus; }
    public Instant getVerifiedAt() { return verifiedAt; }
}
