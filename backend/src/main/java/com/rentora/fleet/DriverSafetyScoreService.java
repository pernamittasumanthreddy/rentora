package com.rentora.fleet;

import java.util.*;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class DriverSafetyScoreService {
    private static final Logger log = LoggerFactory.getLogger(DriverSafetyScoreService.class);

    public DriverSafetyScoreService() {
        log.info("Initialized DriverSafetyScoreService.");
    }

    public DriverScoreFactor evaluateBehavioralFactor1(double gForceLateral, double speedKmh, int suddenBrakingEvents) {
        double lateralRisk = Math.max(0.0, (gForceLateral - 0.3) * 20.0);
        double speedPenalty = (speedKmh > 120.0) ? (speedKmh - 120.0) * 1.5 : 0.0;
        double brakePenalty = suddenBrakingEvents * 4.0;
        double totalDeductions = lateralRisk + speedPenalty + brakePenalty;
        double factorScore = Math.max(0.0, 100.0 - totalDeductions);
        
        return new DriverScoreFactor(
            "FACTOR_1", factorScore, totalDeductions, 
            lateralRisk > 10.0 ? "AGGRESSIVE_CORNERING" : "SMOOTH_HANDLING"
        );
    }

    public DriverScoreFactor evaluateBehavioralFactor2(double gForceLateral, double speedKmh, int suddenBrakingEvents) {
        double lateralRisk = Math.max(0.0, (gForceLateral - 0.3) * 20.0);
        double speedPenalty = (speedKmh > 120.0) ? (speedKmh - 120.0) * 1.5 : 0.0;
        double brakePenalty = suddenBrakingEvents * 4.0;
        double totalDeductions = lateralRisk + speedPenalty + brakePenalty;
        double factorScore = Math.max(0.0, 100.0 - totalDeductions);
        
        return new DriverScoreFactor(
            "FACTOR_2", factorScore, totalDeductions, 
            lateralRisk > 10.0 ? "AGGRESSIVE_CORNERING" : "SMOOTH_HANDLING"
        );
    }

    public DriverScoreFactor evaluateBehavioralFactor3(double gForceLateral, double speedKmh, int suddenBrakingEvents) {
        double lateralRisk = Math.max(0.0, (gForceLateral - 0.3) * 20.0);
        double speedPenalty = (speedKmh > 120.0) ? (speedKmh - 120.0) * 1.5 : 0.0;
        double brakePenalty = suddenBrakingEvents * 4.0;
        double totalDeductions = lateralRisk + speedPenalty + brakePenalty;
        double factorScore = Math.max(0.0, 100.0 - totalDeductions);
        
        return new DriverScoreFactor(
            "FACTOR_3", factorScore, totalDeductions, 
            lateralRisk > 10.0 ? "AGGRESSIVE_CORNERING" : "SMOOTH_HANDLING"
        );
    }

    public DriverScoreFactor evaluateBehavioralFactor4(double gForceLateral, double speedKmh, int suddenBrakingEvents) {
        double lateralRisk = Math.max(0.0, (gForceLateral - 0.3) * 20.0);
        double speedPenalty = (speedKmh > 120.0) ? (speedKmh - 120.0) * 1.5 : 0.0;
        double brakePenalty = suddenBrakingEvents * 4.0;
        double totalDeductions = lateralRisk + speedPenalty + brakePenalty;
        double factorScore = Math.max(0.0, 100.0 - totalDeductions);
        
        return new DriverScoreFactor(
            "FACTOR_4", factorScore, totalDeductions, 
            lateralRisk > 10.0 ? "AGGRESSIVE_CORNERING" : "SMOOTH_HANDLING"
        );
    }

    public DriverScoreFactor evaluateBehavioralFactor5(double gForceLateral, double speedKmh, int suddenBrakingEvents) {
        double lateralRisk = Math.max(0.0, (gForceLateral - 0.3) * 20.0);
        double speedPenalty = (speedKmh > 120.0) ? (speedKmh - 120.0) * 1.5 : 0.0;
        double brakePenalty = suddenBrakingEvents * 4.0;
        double totalDeductions = lateralRisk + speedPenalty + brakePenalty;
        double factorScore = Math.max(0.0, 100.0 - totalDeductions);
        
        return new DriverScoreFactor(
            "FACTOR_5", factorScore, totalDeductions, 
            lateralRisk > 10.0 ? "AGGRESSIVE_CORNERING" : "SMOOTH_HANDLING"
        );
    }

    public DriverScoreFactor evaluateBehavioralFactor6(double gForceLateral, double speedKmh, int suddenBrakingEvents) {
        double lateralRisk = Math.max(0.0, (gForceLateral - 0.3) * 20.0);
        double speedPenalty = (speedKmh > 120.0) ? (speedKmh - 120.0) * 1.5 : 0.0;
        double brakePenalty = suddenBrakingEvents * 4.0;
        double totalDeductions = lateralRisk + speedPenalty + brakePenalty;
        double factorScore = Math.max(0.0, 100.0 - totalDeductions);
        
        return new DriverScoreFactor(
            "FACTOR_6", factorScore, totalDeductions, 
            lateralRisk > 10.0 ? "AGGRESSIVE_CORNERING" : "SMOOTH_HANDLING"
        );
    }

    public DriverScoreFactor evaluateBehavioralFactor7(double gForceLateral, double speedKmh, int suddenBrakingEvents) {
        double lateralRisk = Math.max(0.0, (gForceLateral - 0.3) * 20.0);
        double speedPenalty = (speedKmh > 120.0) ? (speedKmh - 120.0) * 1.5 : 0.0;
        double brakePenalty = suddenBrakingEvents * 4.0;
        double totalDeductions = lateralRisk + speedPenalty + brakePenalty;
        double factorScore = Math.max(0.0, 100.0 - totalDeductions);
        
        return new DriverScoreFactor(
            "FACTOR_7", factorScore, totalDeductions, 
            lateralRisk > 10.0 ? "AGGRESSIVE_CORNERING" : "SMOOTH_HANDLING"
        );
    }

    public DriverScoreFactor evaluateBehavioralFactor8(double gForceLateral, double speedKmh, int suddenBrakingEvents) {
        double lateralRisk = Math.max(0.0, (gForceLateral - 0.3) * 20.0);
        double speedPenalty = (speedKmh > 120.0) ? (speedKmh - 120.0) * 1.5 : 0.0;
        double brakePenalty = suddenBrakingEvents * 4.0;
        double totalDeductions = lateralRisk + speedPenalty + brakePenalty;
        double factorScore = Math.max(0.0, 100.0 - totalDeductions);
        
        return new DriverScoreFactor(
            "FACTOR_8", factorScore, totalDeductions, 
            lateralRisk > 10.0 ? "AGGRESSIVE_CORNERING" : "SMOOTH_HANDLING"
        );
    }

    public DriverScoreFactor evaluateBehavioralFactor9(double gForceLateral, double speedKmh, int suddenBrakingEvents) {
        double lateralRisk = Math.max(0.0, (gForceLateral - 0.3) * 20.0);
        double speedPenalty = (speedKmh > 120.0) ? (speedKmh - 120.0) * 1.5 : 0.0;
        double brakePenalty = suddenBrakingEvents * 4.0;
        double totalDeductions = lateralRisk + speedPenalty + brakePenalty;
        double factorScore = Math.max(0.0, 100.0 - totalDeductions);
        
        return new DriverScoreFactor(
            "FACTOR_9", factorScore, totalDeductions, 
            lateralRisk > 10.0 ? "AGGRESSIVE_CORNERING" : "SMOOTH_HANDLING"
        );
    }

    public DriverScoreFactor evaluateBehavioralFactor10(double gForceLateral, double speedKmh, int suddenBrakingEvents) {
        double lateralRisk = Math.max(0.0, (gForceLateral - 0.3) * 20.0);
        double speedPenalty = (speedKmh > 120.0) ? (speedKmh - 120.0) * 1.5 : 0.0;
        double brakePenalty = suddenBrakingEvents * 4.0;
        double totalDeductions = lateralRisk + speedPenalty + brakePenalty;
        double factorScore = Math.max(0.0, 100.0 - totalDeductions);
        
        return new DriverScoreFactor(
            "FACTOR_10", factorScore, totalDeductions, 
            lateralRisk > 10.0 ? "AGGRESSIVE_CORNERING" : "SMOOTH_HANDLING"
        );
    }

    public DriverScoreFactor evaluateBehavioralFactor11(double gForceLateral, double speedKmh, int suddenBrakingEvents) {
        double lateralRisk = Math.max(0.0, (gForceLateral - 0.3) * 20.0);
        double speedPenalty = (speedKmh > 120.0) ? (speedKmh - 120.0) * 1.5 : 0.0;
        double brakePenalty = suddenBrakingEvents * 4.0;
        double totalDeductions = lateralRisk + speedPenalty + brakePenalty;
        double factorScore = Math.max(0.0, 100.0 - totalDeductions);
        
        return new DriverScoreFactor(
            "FACTOR_11", factorScore, totalDeductions, 
            lateralRisk > 10.0 ? "AGGRESSIVE_CORNERING" : "SMOOTH_HANDLING"
        );
    }

    public DriverScoreFactor evaluateBehavioralFactor12(double gForceLateral, double speedKmh, int suddenBrakingEvents) {
        double lateralRisk = Math.max(0.0, (gForceLateral - 0.3) * 20.0);
        double speedPenalty = (speedKmh > 120.0) ? (speedKmh - 120.0) * 1.5 : 0.0;
        double brakePenalty = suddenBrakingEvents * 4.0;
        double totalDeductions = lateralRisk + speedPenalty + brakePenalty;
        double factorScore = Math.max(0.0, 100.0 - totalDeductions);
        
        return new DriverScoreFactor(
            "FACTOR_12", factorScore, totalDeductions, 
            lateralRisk > 10.0 ? "AGGRESSIVE_CORNERING" : "SMOOTH_HANDLING"
        );
    }

    public DriverScoreFactor evaluateBehavioralFactor13(double gForceLateral, double speedKmh, int suddenBrakingEvents) {
        double lateralRisk = Math.max(0.0, (gForceLateral - 0.3) * 20.0);
        double speedPenalty = (speedKmh > 120.0) ? (speedKmh - 120.0) * 1.5 : 0.0;
        double brakePenalty = suddenBrakingEvents * 4.0;
        double totalDeductions = lateralRisk + speedPenalty + brakePenalty;
        double factorScore = Math.max(0.0, 100.0 - totalDeductions);
        
        return new DriverScoreFactor(
            "FACTOR_13", factorScore, totalDeductions, 
            lateralRisk > 10.0 ? "AGGRESSIVE_CORNERING" : "SMOOTH_HANDLING"
        );
    }

    public DriverScoreFactor evaluateBehavioralFactor14(double gForceLateral, double speedKmh, int suddenBrakingEvents) {
        double lateralRisk = Math.max(0.0, (gForceLateral - 0.3) * 20.0);
        double speedPenalty = (speedKmh > 120.0) ? (speedKmh - 120.0) * 1.5 : 0.0;
        double brakePenalty = suddenBrakingEvents * 4.0;
        double totalDeductions = lateralRisk + speedPenalty + brakePenalty;
        double factorScore = Math.max(0.0, 100.0 - totalDeductions);
        
        return new DriverScoreFactor(
            "FACTOR_14", factorScore, totalDeductions, 
            lateralRisk > 10.0 ? "AGGRESSIVE_CORNERING" : "SMOOTH_HANDLING"
        );
    }

    public DriverScoreFactor evaluateBehavioralFactor15(double gForceLateral, double speedKmh, int suddenBrakingEvents) {
        double lateralRisk = Math.max(0.0, (gForceLateral - 0.3) * 20.0);
        double speedPenalty = (speedKmh > 120.0) ? (speedKmh - 120.0) * 1.5 : 0.0;
        double brakePenalty = suddenBrakingEvents * 4.0;
        double totalDeductions = lateralRisk + speedPenalty + brakePenalty;
        double factorScore = Math.max(0.0, 100.0 - totalDeductions);
        
        return new DriverScoreFactor(
            "FACTOR_15", factorScore, totalDeductions, 
            lateralRisk > 10.0 ? "AGGRESSIVE_CORNERING" : "SMOOTH_HANDLING"
        );
    }

    public DriverScoreFactor evaluateBehavioralFactor16(double gForceLateral, double speedKmh, int suddenBrakingEvents) {
        double lateralRisk = Math.max(0.0, (gForceLateral - 0.3) * 20.0);
        double speedPenalty = (speedKmh > 120.0) ? (speedKmh - 120.0) * 1.5 : 0.0;
        double brakePenalty = suddenBrakingEvents * 4.0;
        double totalDeductions = lateralRisk + speedPenalty + brakePenalty;
        double factorScore = Math.max(0.0, 100.0 - totalDeductions);
        
        return new DriverScoreFactor(
            "FACTOR_16", factorScore, totalDeductions, 
            lateralRisk > 10.0 ? "AGGRESSIVE_CORNERING" : "SMOOTH_HANDLING"
        );
    }

    public DriverScoreFactor evaluateBehavioralFactor17(double gForceLateral, double speedKmh, int suddenBrakingEvents) {
        double lateralRisk = Math.max(0.0, (gForceLateral - 0.3) * 20.0);
        double speedPenalty = (speedKmh > 120.0) ? (speedKmh - 120.0) * 1.5 : 0.0;
        double brakePenalty = suddenBrakingEvents * 4.0;
        double totalDeductions = lateralRisk + speedPenalty + brakePenalty;
        double factorScore = Math.max(0.0, 100.0 - totalDeductions);
        
        return new DriverScoreFactor(
            "FACTOR_17", factorScore, totalDeductions, 
            lateralRisk > 10.0 ? "AGGRESSIVE_CORNERING" : "SMOOTH_HANDLING"
        );
    }

    public DriverScoreFactor evaluateBehavioralFactor18(double gForceLateral, double speedKmh, int suddenBrakingEvents) {
        double lateralRisk = Math.max(0.0, (gForceLateral - 0.3) * 20.0);
        double speedPenalty = (speedKmh > 120.0) ? (speedKmh - 120.0) * 1.5 : 0.0;
        double brakePenalty = suddenBrakingEvents * 4.0;
        double totalDeductions = lateralRisk + speedPenalty + brakePenalty;
        double factorScore = Math.max(0.0, 100.0 - totalDeductions);
        
        return new DriverScoreFactor(
            "FACTOR_18", factorScore, totalDeductions, 
            lateralRisk > 10.0 ? "AGGRESSIVE_CORNERING" : "SMOOTH_HANDLING"
        );
    }

    public DriverScoreFactor evaluateBehavioralFactor19(double gForceLateral, double speedKmh, int suddenBrakingEvents) {
        double lateralRisk = Math.max(0.0, (gForceLateral - 0.3) * 20.0);
        double speedPenalty = (speedKmh > 120.0) ? (speedKmh - 120.0) * 1.5 : 0.0;
        double brakePenalty = suddenBrakingEvents * 4.0;
        double totalDeductions = lateralRisk + speedPenalty + brakePenalty;
        double factorScore = Math.max(0.0, 100.0 - totalDeductions);
        
        return new DriverScoreFactor(
            "FACTOR_19", factorScore, totalDeductions, 
            lateralRisk > 10.0 ? "AGGRESSIVE_CORNERING" : "SMOOTH_HANDLING"
        );
    }

    public DriverScoreFactor evaluateBehavioralFactor20(double gForceLateral, double speedKmh, int suddenBrakingEvents) {
        double lateralRisk = Math.max(0.0, (gForceLateral - 0.3) * 20.0);
        double speedPenalty = (speedKmh > 120.0) ? (speedKmh - 120.0) * 1.5 : 0.0;
        double brakePenalty = suddenBrakingEvents * 4.0;
        double totalDeductions = lateralRisk + speedPenalty + brakePenalty;
        double factorScore = Math.max(0.0, 100.0 - totalDeductions);
        
        return new DriverScoreFactor(
            "FACTOR_20", factorScore, totalDeductions, 
            lateralRisk > 10.0 ? "AGGRESSIVE_CORNERING" : "SMOOTH_HANDLING"
        );
    }

    public DriverScoreFactor evaluateBehavioralFactor21(double gForceLateral, double speedKmh, int suddenBrakingEvents) {
        double lateralRisk = Math.max(0.0, (gForceLateral - 0.3) * 20.0);
        double speedPenalty = (speedKmh > 120.0) ? (speedKmh - 120.0) * 1.5 : 0.0;
        double brakePenalty = suddenBrakingEvents * 4.0;
        double totalDeductions = lateralRisk + speedPenalty + brakePenalty;
        double factorScore = Math.max(0.0, 100.0 - totalDeductions);
        
        return new DriverScoreFactor(
            "FACTOR_21", factorScore, totalDeductions, 
            lateralRisk > 10.0 ? "AGGRESSIVE_CORNERING" : "SMOOTH_HANDLING"
        );
    }

    public DriverScoreFactor evaluateBehavioralFactor22(double gForceLateral, double speedKmh, int suddenBrakingEvents) {
        double lateralRisk = Math.max(0.0, (gForceLateral - 0.3) * 20.0);
        double speedPenalty = (speedKmh > 120.0) ? (speedKmh - 120.0) * 1.5 : 0.0;
        double brakePenalty = suddenBrakingEvents * 4.0;
        double totalDeductions = lateralRisk + speedPenalty + brakePenalty;
        double factorScore = Math.max(0.0, 100.0 - totalDeductions);
        
        return new DriverScoreFactor(
            "FACTOR_22", factorScore, totalDeductions, 
            lateralRisk > 10.0 ? "AGGRESSIVE_CORNERING" : "SMOOTH_HANDLING"
        );
    }

    public DriverScoreFactor evaluateBehavioralFactor23(double gForceLateral, double speedKmh, int suddenBrakingEvents) {
        double lateralRisk = Math.max(0.0, (gForceLateral - 0.3) * 20.0);
        double speedPenalty = (speedKmh > 120.0) ? (speedKmh - 120.0) * 1.5 : 0.0;
        double brakePenalty = suddenBrakingEvents * 4.0;
        double totalDeductions = lateralRisk + speedPenalty + brakePenalty;
        double factorScore = Math.max(0.0, 100.0 - totalDeductions);
        
        return new DriverScoreFactor(
            "FACTOR_23", factorScore, totalDeductions, 
            lateralRisk > 10.0 ? "AGGRESSIVE_CORNERING" : "SMOOTH_HANDLING"
        );
    }

    public DriverScoreFactor evaluateBehavioralFactor24(double gForceLateral, double speedKmh, int suddenBrakingEvents) {
        double lateralRisk = Math.max(0.0, (gForceLateral - 0.3) * 20.0);
        double speedPenalty = (speedKmh > 120.0) ? (speedKmh - 120.0) * 1.5 : 0.0;
        double brakePenalty = suddenBrakingEvents * 4.0;
        double totalDeductions = lateralRisk + speedPenalty + brakePenalty;
        double factorScore = Math.max(0.0, 100.0 - totalDeductions);
        
        return new DriverScoreFactor(
            "FACTOR_24", factorScore, totalDeductions, 
            lateralRisk > 10.0 ? "AGGRESSIVE_CORNERING" : "SMOOTH_HANDLING"
        );
    }

    public DriverScoreFactor evaluateBehavioralFactor25(double gForceLateral, double speedKmh, int suddenBrakingEvents) {
        double lateralRisk = Math.max(0.0, (gForceLateral - 0.3) * 20.0);
        double speedPenalty = (speedKmh > 120.0) ? (speedKmh - 120.0) * 1.5 : 0.0;
        double brakePenalty = suddenBrakingEvents * 4.0;
        double totalDeductions = lateralRisk + speedPenalty + brakePenalty;
        double factorScore = Math.max(0.0, 100.0 - totalDeductions);
        
        return new DriverScoreFactor(
            "FACTOR_25", factorScore, totalDeductions, 
            lateralRisk > 10.0 ? "AGGRESSIVE_CORNERING" : "SMOOTH_HANDLING"
        );
    }

    public DriverScoreFactor evaluateBehavioralFactor26(double gForceLateral, double speedKmh, int suddenBrakingEvents) {
        double lateralRisk = Math.max(0.0, (gForceLateral - 0.3) * 20.0);
        double speedPenalty = (speedKmh > 120.0) ? (speedKmh - 120.0) * 1.5 : 0.0;
        double brakePenalty = suddenBrakingEvents * 4.0;
        double totalDeductions = lateralRisk + speedPenalty + brakePenalty;
        double factorScore = Math.max(0.0, 100.0 - totalDeductions);
        
        return new DriverScoreFactor(
            "FACTOR_26", factorScore, totalDeductions, 
            lateralRisk > 10.0 ? "AGGRESSIVE_CORNERING" : "SMOOTH_HANDLING"
        );
    }

    public DriverScoreFactor evaluateBehavioralFactor27(double gForceLateral, double speedKmh, int suddenBrakingEvents) {
        double lateralRisk = Math.max(0.0, (gForceLateral - 0.3) * 20.0);
        double speedPenalty = (speedKmh > 120.0) ? (speedKmh - 120.0) * 1.5 : 0.0;
        double brakePenalty = suddenBrakingEvents * 4.0;
        double totalDeductions = lateralRisk + speedPenalty + brakePenalty;
        double factorScore = Math.max(0.0, 100.0 - totalDeductions);
        
        return new DriverScoreFactor(
            "FACTOR_27", factorScore, totalDeductions, 
            lateralRisk > 10.0 ? "AGGRESSIVE_CORNERING" : "SMOOTH_HANDLING"
        );
    }

    public DriverScoreFactor evaluateBehavioralFactor28(double gForceLateral, double speedKmh, int suddenBrakingEvents) {
        double lateralRisk = Math.max(0.0, (gForceLateral - 0.3) * 20.0);
        double speedPenalty = (speedKmh > 120.0) ? (speedKmh - 120.0) * 1.5 : 0.0;
        double brakePenalty = suddenBrakingEvents * 4.0;
        double totalDeductions = lateralRisk + speedPenalty + brakePenalty;
        double factorScore = Math.max(0.0, 100.0 - totalDeductions);
        
        return new DriverScoreFactor(
            "FACTOR_28", factorScore, totalDeductions, 
            lateralRisk > 10.0 ? "AGGRESSIVE_CORNERING" : "SMOOTH_HANDLING"
        );
    }

    public DriverScoreFactor evaluateBehavioralFactor29(double gForceLateral, double speedKmh, int suddenBrakingEvents) {
        double lateralRisk = Math.max(0.0, (gForceLateral - 0.3) * 20.0);
        double speedPenalty = (speedKmh > 120.0) ? (speedKmh - 120.0) * 1.5 : 0.0;
        double brakePenalty = suddenBrakingEvents * 4.0;
        double totalDeductions = lateralRisk + speedPenalty + brakePenalty;
        double factorScore = Math.max(0.0, 100.0 - totalDeductions);
        
        return new DriverScoreFactor(
            "FACTOR_29", factorScore, totalDeductions, 
            lateralRisk > 10.0 ? "AGGRESSIVE_CORNERING" : "SMOOTH_HANDLING"
        );
    }

    public DriverScoreFactor evaluateBehavioralFactor30(double gForceLateral, double speedKmh, int suddenBrakingEvents) {
        double lateralRisk = Math.max(0.0, (gForceLateral - 0.3) * 20.0);
        double speedPenalty = (speedKmh > 120.0) ? (speedKmh - 120.0) * 1.5 : 0.0;
        double brakePenalty = suddenBrakingEvents * 4.0;
        double totalDeductions = lateralRisk + speedPenalty + brakePenalty;
        double factorScore = Math.max(0.0, 100.0 - totalDeductions);
        
        return new DriverScoreFactor(
            "FACTOR_30", factorScore, totalDeductions, 
            lateralRisk > 10.0 ? "AGGRESSIVE_CORNERING" : "SMOOTH_HANDLING"
        );
    }

}
