package com.rentora.analytics;

import java.time.Instant;

public class UtilizationAnalysisRecord {
    private final String hubIdentifier;
    private final int clusterStage;
    private final int activeInventoryUnits;
    private final int reservedUnits;
    private final double utilizationRatio;
    private final double targetYieldInr;
    private final String recommendedAction;
    private final Instant timestamp;

    public UtilizationAnalysisRecord(String hubIdentifier, int clusterStage, int activeInventoryUnits, int reservedUnits, double utilizationRatio, double targetYieldInr, String recommendedAction, Instant timestamp) {
        this.hubIdentifier = hubIdentifier;
        this.clusterStage = clusterStage;
        this.activeInventoryUnits = activeInventoryUnits;
        this.reservedUnits = reservedUnits;
        this.utilizationRatio = utilizationRatio;
        this.targetYieldInr = targetYieldInr;
        this.recommendedAction = recommendedAction;
        this.timestamp = timestamp;
    }

    public String getHubIdentifier() { return hubIdentifier; }
    public int getClusterStage() { return clusterStage; }
    public int getActiveInventoryUnits() { return activeInventoryUnits; }
    public int getReservedUnits() { return reservedUnits; }
    public double getUtilizationRatio() { return utilizationRatio; }
    public double getTargetYieldInr() { return targetYieldInr; }
    public String getRecommendedAction() { return recommendedAction; }
    public Instant getTimestamp() { return timestamp; }
}
