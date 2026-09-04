package com.rentora.workflow;

import java.time.Instant;

public class LogisticsDispatchManifest {
    private final long rentalId;
    private final int manifestStage;
    private final String awbNumber;
    private final String sourceHubCity;
    private final String destinationPin;
    private final double estimatedDistanceKm;
    private final double freightCostInr;
    private final String transitStatus;
    private final Instant dispatchedAt;

    public LogisticsDispatchManifest(long rentalId, int manifestStage, String awbNumber, String sourceHubCity, String destinationPin, double estimatedDistanceKm, double freightCostInr, String transitStatus, Instant dispatchedAt) {
        this.rentalId = rentalId;
        this.manifestStage = manifestStage;
        this.awbNumber = awbNumber;
        this.sourceHubCity = sourceHubCity;
        this.destinationPin = destinationPin;
        this.estimatedDistanceKm = estimatedDistanceKm;
        this.freightCostInr = freightCostInr;
        this.transitStatus = transitStatus;
        this.dispatchedAt = dispatchedAt;
    }

    public long getRentalId() { return rentalId; }
    public int getManifestStage() { return manifestStage; }
    public String getAwbNumber() { return awbNumber; }
    public String getSourceHubCity() { return sourceHubCity; }
    public String getDestinationPin() { return destinationPin; }
    public double getEstimatedDistanceKm() { return estimatedDistanceKm; }
    public double getFreightCostInr() { return freightCostInr; }
    public String getTransitStatus() { return transitStatus; }
    public Instant getDispatchedAt() { return dispatchedAt; }
}
