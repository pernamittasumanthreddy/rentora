package com.rentora.hardware;

import java.time.Instant;

public class CinemaRigSensorReading {
    private final String assetBarcode;
    private final int channelId;
    private final double totalOperatingHours;
    private final double internalSensorTempC;
    private final boolean temperatureWithinLimits;
    private final double sensorDegradationFactor;
    private final String serviceRecommendation;
    private final Instant loggedAt;

    public CinemaRigSensorReading(String assetBarcode, int channelId, double totalOperatingHours, double internalSensorTempC, boolean temperatureWithinLimits, double sensorDegradationFactor, String serviceRecommendation, Instant loggedAt) {
        this.assetBarcode = assetBarcode;
        this.channelId = channelId;
        this.totalOperatingHours = totalOperatingHours;
        this.internalSensorTempC = internalSensorTempC;
        this.temperatureWithinLimits = temperatureWithinLimits;
        this.sensorDegradationFactor = sensorDegradationFactor;
        this.serviceRecommendation = serviceRecommendation;
        this.loggedAt = loggedAt;
    }

    public String getAssetBarcode() { return assetBarcode; }
    public int getChannelId() { return channelId; }
    public double getTotalOperatingHours() { return totalOperatingHours; }
    public double getInternalSensorTempC() { return internalSensorTempC; }
    public boolean isTemperatureWithinLimits() { return temperatureWithinLimits; }
    public double getSensorDegradationFactor() { return sensorDegradationFactor; }
    public String getServiceRecommendation() { return serviceRecommendation; }
    public Instant getLoggedAt() { return loggedAt; }
}
