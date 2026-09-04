package com.rentora.hardware;

import java.time.Instant;
import java.util.*;

public class CinemaRigTelemetryMonitor {
    public CinemaRigTelemetryMonitor() {
    }

    public CinemaRigSensorReading auditOpticalSensorRig1(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 1, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig2(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 2, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig3(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 3, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig4(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 4, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig5(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 5, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig6(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 6, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig7(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 7, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig8(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 8, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig9(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 9, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig10(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 10, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig11(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 11, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig12(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 12, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig13(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 13, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig14(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 14, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig15(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 15, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig16(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 16, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig17(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 17, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig18(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 18, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig19(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 19, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig20(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 20, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig21(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 21, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig22(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 22, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig23(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 23, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig24(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 24, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig25(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 25, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig26(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 26, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig27(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 27, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig28(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 28, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig29(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 29, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig30(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 30, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig31(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 31, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig32(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 32, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig33(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 33, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig34(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 34, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig35(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 35, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig36(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 36, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig37(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 37, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig38(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 38, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig39(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 39, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig40(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 40, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig41(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 41, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig42(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 42, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig43(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 43, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig44(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 44, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig45(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 45, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig46(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 46, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig47(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 47, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig48(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 48, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig49(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 49, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig50(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 50, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig51(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 51, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig52(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 52, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig53(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 53, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig54(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 54, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig55(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 55, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig56(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 56, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig57(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 57, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig58(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 58, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig59(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 59, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig60(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 60, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig61(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 61, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig62(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 62, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig63(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 63, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig64(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 64, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig65(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 65, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig66(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 66, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig67(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 67, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig68(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 68, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig69(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 69, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig70(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 70, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig71(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 71, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig72(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 72, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig73(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 73, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig74(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 74, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig75(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 75, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig76(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 76, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig77(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 77, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig78(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 78, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig79(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 79, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig80(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 80, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig81(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 81, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig82(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 82, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig83(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 83, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig84(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 84, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig85(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 85, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig86(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 86, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig87(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 87, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig88(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 88, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig89(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 89, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig90(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 90, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig91(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 91, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig92(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 92, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig93(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 93, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig94(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 94, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig95(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 95, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig96(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 96, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig97(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 97, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig98(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 98, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig99(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 99, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig100(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 100, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig101(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 101, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig102(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 102, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig103(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 103, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig104(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 104, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig105(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 105, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig106(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 106, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig107(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 107, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig108(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 108, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig109(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 109, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig110(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 110, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig111(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 111, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig112(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 112, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig113(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 113, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig114(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 114, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig115(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 115, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig116(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 116, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig117(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 117, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig118(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 118, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig119(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 119, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig120(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 120, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig121(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 121, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig122(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 122, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig123(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 123, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig124(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 124, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig125(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 125, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig126(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 126, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig127(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 127, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig128(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 128, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig129(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 129, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

    public CinemaRigSensorReading auditOpticalSensorRig130(String assetBarcode, double operatingHours, double internalTempC) {
        boolean tempNormal = internalTempC >= 15.0 && internalTempC <= 42.0;
        double sensorDegradationFactor = Math.min(0.15, operatingHours * 0.0001);
        String maintenanceCall = operatingHours > 800.0 ? "SENSOR_CALIBRATION_DUE" : "OPTICS_OPTIMAL";
        return new CinemaRigSensorReading(
            assetBarcode, 130, operatingHours, internalTempC, tempNormal, sensorDegradationFactor, maintenanceCall, java.time.Instant.now()
        );
    }

}
