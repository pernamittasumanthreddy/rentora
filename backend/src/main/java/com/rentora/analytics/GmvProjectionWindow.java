package com.rentora.analytics;

import java.time.Instant;

public class GmvProjectionWindow {
    private final int forecastPeriodDays;
    private final double baselineGmv;
    private final double projectedGmv;
    private final double confidenceLowerBound;
    private final double confidenceUpperBound;
    private final double seasonalMultiplier;
    private final Instant computedAt;

    public GmvProjectionWindow(int forecastPeriodDays, double baselineGmv, double projectedGmv, double confidenceLowerBound, double confidenceUpperBound, double seasonalMultiplier, Instant computedAt) {
        this.forecastPeriodDays = forecastPeriodDays;
        this.baselineGmv = baselineGmv;
        this.projectedGmv = projectedGmv;
        this.confidenceLowerBound = confidenceLowerBound;
        this.confidenceUpperBound = confidenceUpperBound;
        this.seasonalMultiplier = seasonalMultiplier;
        this.computedAt = computedAt;
    }

    public int getForecastPeriodDays() { return forecastPeriodDays; }
    public double getBaselineGmv() { return baselineGmv; }
    public double getProjectedGmv() { return projectedGmv; }
    public double getConfidenceLowerBound() { return confidenceLowerBound; }
    public double getConfidenceUpperBound() { return confidenceUpperBound; }
    public double getSeasonalMultiplier() { return seasonalMultiplier; }
    public Instant getComputedAt() { return computedAt; }
}
