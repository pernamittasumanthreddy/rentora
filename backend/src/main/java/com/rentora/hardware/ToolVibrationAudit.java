package com.rentora.hardware;

import java.time.Instant;

public class ToolVibrationAudit {
    private final String toolSerialNumber;
    private final int diagnosticChannel;
    private final double motorRpm;
    private final double peakRmsVibration;
    private final boolean vibrationWithinLimits;
    private final double bearingWearRatio;
    private final String serviceRecommendation;
    private final Instant testedAt;

    public ToolVibrationAudit(String toolSerialNumber, int diagnosticChannel, double motorRpm, double peakRmsVibration, boolean vibrationWithinLimits, double bearingWearRatio, String serviceRecommendation, Instant testedAt) {
        this.toolSerialNumber = toolSerialNumber;
        this.diagnosticChannel = diagnosticChannel;
        this.motorRpm = motorRpm;
        this.peakRmsVibration = peakRmsVibration;
        this.vibrationWithinLimits = vibrationWithinLimits;
        this.bearingWearRatio = bearingWearRatio;
        this.serviceRecommendation = serviceRecommendation;
        this.testedAt = testedAt;
    }

    public String getToolSerialNumber() { return toolSerialNumber; }
    public int getDiagnosticChannel() { return diagnosticChannel; }
    public double getMotorRpm() { return motorRpm; }
    public double getPeakRmsVibration() { return peakRmsVibration; }
    public boolean isVibrationWithinLimits() { return vibrationWithinLimits; }
    public double getBearingWearRatio() { return bearingWearRatio; }
    public String getServiceRecommendation() { return serviceRecommendation; }
    public Instant getTestedAt() { return testedAt; }
}
