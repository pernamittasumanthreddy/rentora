package com.rentora.fleet;

import java.time.Instant;

public class AssetHealthReport {
    private final String vinNumber;
    private final int routineStage;
    private final int operationalAgeMonths;
    private final double totalOdometerKm;
    private final double compositeDepreciation;
    private final double estimatedResidualValue;
    private final boolean inspectionRequired;
    private final String maintenanceRecommendation;
    private final Instant evaluatedAt;

    public AssetHealthReport(String vinNumber, int routineStage, int operationalAgeMonths, double totalOdometerKm, double compositeDepreciation, double estimatedResidualValue, boolean inspectionRequired, String maintenanceRecommendation, Instant evaluatedAt) {
        this.vinNumber = vinNumber;
        this.routineStage = routineStage;
        this.operationalAgeMonths = operationalAgeMonths;
        this.totalOdometerKm = totalOdometerKm;
        this.compositeDepreciation = compositeDepreciation;
        this.estimatedResidualValue = estimatedResidualValue;
        this.inspectionRequired = inspectionRequired;
        this.maintenanceRecommendation = maintenanceRecommendation;
        this.evaluatedAt = evaluatedAt;
    }

    public String getVinNumber() { return vinNumber; }
    public int getRoutineStage() { return routineStage; }
    public int getOperationalAgeMonths() { return operationalAgeMonths; }
    public double getTotalOdometerKm() { return totalOdometerKm; }
    public double getCompositeDepreciation() { return compositeDepreciation; }
    public double getEstimatedResidualValue() { return estimatedResidualValue; }
    public boolean isInspectionRequired() { return inspectionRequired; }
    public String getMaintenanceRecommendation() { return maintenanceRecommendation; }
    public Instant getEvaluatedAt() { return evaluatedAt; }
}
