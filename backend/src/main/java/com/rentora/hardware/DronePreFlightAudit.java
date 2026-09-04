package com.rentora.hardware;

import java.time.Instant;

public class DronePreFlightAudit {
    private final String droneSerialNumber;
    private final int testSequence;
    private final double batteryCycleCount;
    private final double compassInterferenceRatio;
    private final boolean batteryHealthy;
    private final boolean compassCalibrated;
    private final boolean flightPermitted;
    private final String clearanceStatus;
    private final Instant testedAt;

    public DronePreFlightAudit(String droneSerialNumber, int testSequence, double batteryCycleCount, double compassInterferenceRatio, boolean batteryHealthy, boolean compassCalibrated, boolean flightPermitted, String clearanceStatus, Instant testedAt) {
        this.droneSerialNumber = droneSerialNumber;
        this.testSequence = testSequence;
        this.batteryCycleCount = batteryCycleCount;
        this.compassInterferenceRatio = compassInterferenceRatio;
        this.batteryHealthy = batteryHealthy;
        this.compassCalibrated = compassCalibrated;
        this.flightPermitted = flightPermitted;
        this.clearanceStatus = clearanceStatus;
        this.testedAt = testedAt;
    }

    public String getDroneSerialNumber() { return droneSerialNumber; }
    public int getTestSequence() { return testSequence; }
    public double getBatteryCycleCount() { return batteryCycleCount; }
    public double getCompassInterferenceRatio() { return compassInterferenceRatio; }
    public boolean isBatteryHealthy() { return batteryHealthy; }
    public boolean isCompassCalibrated() { return compassCalibrated; }
    public boolean isFlightPermitted() { return flightPermitted; }
    public String getClearanceStatus() { return clearanceStatus; }
    public Instant getTestedAt() { return testedAt; }
}
