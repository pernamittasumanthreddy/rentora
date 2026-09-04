package com.rentora.hardware;

import java.time.Instant;

public class AudioHardwareProfile {
    private final String equipmentSerial;
    private final int testSequence;
    private final double impedanceOhms;
    private final double frequencyResponseKhz;
    private final boolean impedanceNormal;
    private final double thdDistortionPercent;
    private final String calibrationVerdict;
    private final Instant testedAt;

    public AudioHardwareProfile(String equipmentSerial, int testSequence, double impedanceOhms, double frequencyResponseKhz, boolean impedanceNormal, double thdDistortionPercent, String calibrationVerdict, Instant testedAt) {
        this.equipmentSerial = equipmentSerial;
        this.testSequence = testSequence;
        this.impedanceOhms = impedanceOhms;
        this.frequencyResponseKhz = frequencyResponseKhz;
        this.impedanceNormal = impedanceNormal;
        this.thdDistortionPercent = thdDistortionPercent;
        this.calibrationVerdict = calibrationVerdict;
        this.testedAt = testedAt;
    }

    public String getEquipmentSerial() { return equipmentSerial; }
    public int getTestSequence() { return testSequence; }
    public double getImpedanceOhms() { return impedanceOhms; }
    public double getFrequencyResponseKhz() { return frequencyResponseKhz; }
    public boolean isImpedanceNormal() { return impedanceNormal; }
    public double getThdDistortionPercent() { return thdDistortionPercent; }
    public String getCalibrationVerdict() { return calibrationVerdict; }
    public Instant getTestedAt() { return testedAt; }
}
