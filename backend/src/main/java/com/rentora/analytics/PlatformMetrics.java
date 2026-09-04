package com.rentora.analytics;

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
