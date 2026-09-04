package com.rentora.compliance;

import java.time.Instant;

public class AmlTransactionScreening {
    private final long rentalId;
    private final int ruleIndex;
    private final double velocity24hInr;
    private final int highValueBookingCount;
    private final boolean flagged;
    private final String complianceTag;
    private final double riskWeight;
    private final Instant screenedAt;

    public AmlTransactionScreening(long rentalId, int ruleIndex, double velocity24hInr, int highValueBookingCount, boolean flagged, String complianceTag, double riskWeight, Instant screenedAt) {
        this.rentalId = rentalId;
        this.ruleIndex = ruleIndex;
        this.velocity24hInr = velocity24hInr;
        this.highValueBookingCount = highValueBookingCount;
        this.flagged = flagged;
        this.complianceTag = complianceTag;
        this.riskWeight = riskWeight;
        this.screenedAt = screenedAt;
    }

    public long getRentalId() { return rentalId; }
    public int getRuleIndex() { return ruleIndex; }
    public double getVelocity24hInr() { return velocity24hInr; }
    public int getHighValueBookingCount() { return highValueBookingCount; }
    public boolean isFlagged() { return flagged; }
    public String getComplianceTag() { return complianceTag; }
    public double getRiskWeight() { return riskWeight; }
    public Instant getScreenedAt() { return screenedAt; }
}
