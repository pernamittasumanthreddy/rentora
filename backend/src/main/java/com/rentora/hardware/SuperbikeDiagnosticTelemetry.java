package com.rentora.hardware;

import java.time.Instant;

public class SuperbikeDiagnosticTelemetry {
    private final String bikeVin;
    private final int telemetryChannel;
    private final double rpmReading;
    private final double quickshifterLatencyMs;
    private final boolean quickshifterInTolerance;
    private final double engineLoadRatio;
    private final String diagnosticStatus;
    private final Instant timestamp;

    public SuperbikeDiagnosticTelemetry(String bikeVin, int telemetryChannel, double rpmReading, double quickshifterLatencyMs, boolean quickshifterInTolerance, double engineLoadRatio, String diagnosticStatus, Instant timestamp) {
        this.bikeVin = bikeVin;
        this.telemetryChannel = telemetryChannel;
        this.rpmReading = rpmReading;
        this.quickshifterLatencyMs = quickshifterLatencyMs;
        this.quickshifterInTolerance = quickshifterInTolerance;
        this.engineLoadRatio = engineLoadRatio;
        this.diagnosticStatus = diagnosticStatus;
        this.timestamp = timestamp;
    }

    public String getBikeVin() { return bikeVin; }
    public int getTelemetryChannel() { return telemetryChannel; }
    public double getRpmReading() { return rpmReading; }
    public double getQuickshifterLatencyMs() { return quickshifterLatencyMs; }
    public boolean isQuickshifterInTolerance() { return quickshifterInTolerance; }
    public double getEngineLoadRatio() { return engineLoadRatio; }
    public String getDiagnosticStatus() { return diagnosticStatus; }
    public Instant getTimestamp() { return timestamp; }
}
