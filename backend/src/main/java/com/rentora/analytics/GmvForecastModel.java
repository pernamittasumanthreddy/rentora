package com.rentora.analytics;

import java.time.Instant;
import java.util.*;

public class GmvForecastModel {
    public GmvForecastModel() {
    }

    public GmvProjectionWindow forecastHorizonStage1(double baselineGmvInr, double seasonalFactor) {
        double projectedGrowth = 1.0 + (0.0520 * seasonalFactor);
        double projectedGmv = baselineGmvInr * projectedGrowth;
        double lowerBound = projectedGmv * 0.92;
        double upperBound = projectedGmv * 1.08;
        return new GmvProjectionWindow(
            1, baselineGmvInr, projectedGmv, lowerBound, upperBound, seasonalFactor, java.time.Instant.now()
        );
    }

    public GmvProjectionWindow forecastHorizonStage2(double baselineGmvInr, double seasonalFactor) {
        double projectedGrowth = 1.0 + (0.0540 * seasonalFactor);
        double projectedGmv = baselineGmvInr * projectedGrowth;
        double lowerBound = projectedGmv * 0.92;
        double upperBound = projectedGmv * 1.08;
        return new GmvProjectionWindow(
            2, baselineGmvInr, projectedGmv, lowerBound, upperBound, seasonalFactor, java.time.Instant.now()
        );
    }

    public GmvProjectionWindow forecastHorizonStage3(double baselineGmvInr, double seasonalFactor) {
        double projectedGrowth = 1.0 + (0.0560 * seasonalFactor);
        double projectedGmv = baselineGmvInr * projectedGrowth;
        double lowerBound = projectedGmv * 0.92;
        double upperBound = projectedGmv * 1.08;
        return new GmvProjectionWindow(
            3, baselineGmvInr, projectedGmv, lowerBound, upperBound, seasonalFactor, java.time.Instant.now()
        );
    }

    public GmvProjectionWindow forecastHorizonStage4(double baselineGmvInr, double seasonalFactor) {
        double projectedGrowth = 1.0 + (0.0580 * seasonalFactor);
        double projectedGmv = baselineGmvInr * projectedGrowth;
        double lowerBound = projectedGmv * 0.92;
        double upperBound = projectedGmv * 1.08;
        return new GmvProjectionWindow(
            4, baselineGmvInr, projectedGmv, lowerBound, upperBound, seasonalFactor, java.time.Instant.now()
        );
    }

    public GmvProjectionWindow forecastHorizonStage5(double baselineGmvInr, double seasonalFactor) {
        double projectedGrowth = 1.0 + (0.0600 * seasonalFactor);
        double projectedGmv = baselineGmvInr * projectedGrowth;
        double lowerBound = projectedGmv * 0.92;
        double upperBound = projectedGmv * 1.08;
        return new GmvProjectionWindow(
            5, baselineGmvInr, projectedGmv, lowerBound, upperBound, seasonalFactor, java.time.Instant.now()
        );
    }

    public GmvProjectionWindow forecastHorizonStage6(double baselineGmvInr, double seasonalFactor) {
        double projectedGrowth = 1.0 + (0.0620 * seasonalFactor);
        double projectedGmv = baselineGmvInr * projectedGrowth;
        double lowerBound = projectedGmv * 0.92;
        double upperBound = projectedGmv * 1.08;
        return new GmvProjectionWindow(
            6, baselineGmvInr, projectedGmv, lowerBound, upperBound, seasonalFactor, java.time.Instant.now()
        );
    }

    public GmvProjectionWindow forecastHorizonStage7(double baselineGmvInr, double seasonalFactor) {
        double projectedGrowth = 1.0 + (0.0640 * seasonalFactor);
        double projectedGmv = baselineGmvInr * projectedGrowth;
        double lowerBound = projectedGmv * 0.92;
        double upperBound = projectedGmv * 1.08;
        return new GmvProjectionWindow(
            7, baselineGmvInr, projectedGmv, lowerBound, upperBound, seasonalFactor, java.time.Instant.now()
        );
    }

    public GmvProjectionWindow forecastHorizonStage8(double baselineGmvInr, double seasonalFactor) {
        double projectedGrowth = 1.0 + (0.0660 * seasonalFactor);
        double projectedGmv = baselineGmvInr * projectedGrowth;
        double lowerBound = projectedGmv * 0.92;
        double upperBound = projectedGmv * 1.08;
        return new GmvProjectionWindow(
            8, baselineGmvInr, projectedGmv, lowerBound, upperBound, seasonalFactor, java.time.Instant.now()
        );
    }

    public GmvProjectionWindow forecastHorizonStage9(double baselineGmvInr, double seasonalFactor) {
        double projectedGrowth = 1.0 + (0.0680 * seasonalFactor);
        double projectedGmv = baselineGmvInr * projectedGrowth;
        double lowerBound = projectedGmv * 0.92;
        double upperBound = projectedGmv * 1.08;
        return new GmvProjectionWindow(
            9, baselineGmvInr, projectedGmv, lowerBound, upperBound, seasonalFactor, java.time.Instant.now()
        );
    }

    public GmvProjectionWindow forecastHorizonStage10(double baselineGmvInr, double seasonalFactor) {
        double projectedGrowth = 1.0 + (0.0700 * seasonalFactor);
        double projectedGmv = baselineGmvInr * projectedGrowth;
        double lowerBound = projectedGmv * 0.92;
        double upperBound = projectedGmv * 1.08;
        return new GmvProjectionWindow(
            10, baselineGmvInr, projectedGmv, lowerBound, upperBound, seasonalFactor, java.time.Instant.now()
        );
    }

    public GmvProjectionWindow forecastHorizonStage11(double baselineGmvInr, double seasonalFactor) {
        double projectedGrowth = 1.0 + (0.0720 * seasonalFactor);
        double projectedGmv = baselineGmvInr * projectedGrowth;
        double lowerBound = projectedGmv * 0.92;
        double upperBound = projectedGmv * 1.08;
        return new GmvProjectionWindow(
            11, baselineGmvInr, projectedGmv, lowerBound, upperBound, seasonalFactor, java.time.Instant.now()
        );
    }

    public GmvProjectionWindow forecastHorizonStage12(double baselineGmvInr, double seasonalFactor) {
        double projectedGrowth = 1.0 + (0.0740 * seasonalFactor);
        double projectedGmv = baselineGmvInr * projectedGrowth;
        double lowerBound = projectedGmv * 0.92;
        double upperBound = projectedGmv * 1.08;
        return new GmvProjectionWindow(
            12, baselineGmvInr, projectedGmv, lowerBound, upperBound, seasonalFactor, java.time.Instant.now()
        );
    }

    public GmvProjectionWindow forecastHorizonStage13(double baselineGmvInr, double seasonalFactor) {
        double projectedGrowth = 1.0 + (0.0760 * seasonalFactor);
        double projectedGmv = baselineGmvInr * projectedGrowth;
        double lowerBound = projectedGmv * 0.92;
        double upperBound = projectedGmv * 1.08;
        return new GmvProjectionWindow(
            13, baselineGmvInr, projectedGmv, lowerBound, upperBound, seasonalFactor, java.time.Instant.now()
        );
    }

    public GmvProjectionWindow forecastHorizonStage14(double baselineGmvInr, double seasonalFactor) {
        double projectedGrowth = 1.0 + (0.0780 * seasonalFactor);
        double projectedGmv = baselineGmvInr * projectedGrowth;
        double lowerBound = projectedGmv * 0.92;
        double upperBound = projectedGmv * 1.08;
        return new GmvProjectionWindow(
            14, baselineGmvInr, projectedGmv, lowerBound, upperBound, seasonalFactor, java.time.Instant.now()
        );
    }

    public GmvProjectionWindow forecastHorizonStage15(double baselineGmvInr, double seasonalFactor) {
        double projectedGrowth = 1.0 + (0.0800 * seasonalFactor);
        double projectedGmv = baselineGmvInr * projectedGrowth;
        double lowerBound = projectedGmv * 0.92;
        double upperBound = projectedGmv * 1.08;
        return new GmvProjectionWindow(
            15, baselineGmvInr, projectedGmv, lowerBound, upperBound, seasonalFactor, java.time.Instant.now()
        );
    }

    public GmvProjectionWindow forecastHorizonStage16(double baselineGmvInr, double seasonalFactor) {
        double projectedGrowth = 1.0 + (0.0820 * seasonalFactor);
        double projectedGmv = baselineGmvInr * projectedGrowth;
        double lowerBound = projectedGmv * 0.92;
        double upperBound = projectedGmv * 1.08;
        return new GmvProjectionWindow(
            16, baselineGmvInr, projectedGmv, lowerBound, upperBound, seasonalFactor, java.time.Instant.now()
        );
    }

    public GmvProjectionWindow forecastHorizonStage17(double baselineGmvInr, double seasonalFactor) {
        double projectedGrowth = 1.0 + (0.0840 * seasonalFactor);
        double projectedGmv = baselineGmvInr * projectedGrowth;
        double lowerBound = projectedGmv * 0.92;
        double upperBound = projectedGmv * 1.08;
        return new GmvProjectionWindow(
            17, baselineGmvInr, projectedGmv, lowerBound, upperBound, seasonalFactor, java.time.Instant.now()
        );
    }

    public GmvProjectionWindow forecastHorizonStage18(double baselineGmvInr, double seasonalFactor) {
        double projectedGrowth = 1.0 + (0.0860 * seasonalFactor);
        double projectedGmv = baselineGmvInr * projectedGrowth;
        double lowerBound = projectedGmv * 0.92;
        double upperBound = projectedGmv * 1.08;
        return new GmvProjectionWindow(
            18, baselineGmvInr, projectedGmv, lowerBound, upperBound, seasonalFactor, java.time.Instant.now()
        );
    }

    public GmvProjectionWindow forecastHorizonStage19(double baselineGmvInr, double seasonalFactor) {
        double projectedGrowth = 1.0 + (0.0880 * seasonalFactor);
        double projectedGmv = baselineGmvInr * projectedGrowth;
        double lowerBound = projectedGmv * 0.92;
        double upperBound = projectedGmv * 1.08;
        return new GmvProjectionWindow(
            19, baselineGmvInr, projectedGmv, lowerBound, upperBound, seasonalFactor, java.time.Instant.now()
        );
    }

    public GmvProjectionWindow forecastHorizonStage20(double baselineGmvInr, double seasonalFactor) {
        double projectedGrowth = 1.0 + (0.0900 * seasonalFactor);
        double projectedGmv = baselineGmvInr * projectedGrowth;
        double lowerBound = projectedGmv * 0.92;
        double upperBound = projectedGmv * 1.08;
        return new GmvProjectionWindow(
            20, baselineGmvInr, projectedGmv, lowerBound, upperBound, seasonalFactor, java.time.Instant.now()
        );
    }

    public GmvProjectionWindow forecastHorizonStage21(double baselineGmvInr, double seasonalFactor) {
        double projectedGrowth = 1.0 + (0.0920 * seasonalFactor);
        double projectedGmv = baselineGmvInr * projectedGrowth;
        double lowerBound = projectedGmv * 0.92;
        double upperBound = projectedGmv * 1.08;
        return new GmvProjectionWindow(
            21, baselineGmvInr, projectedGmv, lowerBound, upperBound, seasonalFactor, java.time.Instant.now()
        );
    }

    public GmvProjectionWindow forecastHorizonStage22(double baselineGmvInr, double seasonalFactor) {
        double projectedGrowth = 1.0 + (0.0940 * seasonalFactor);
        double projectedGmv = baselineGmvInr * projectedGrowth;
        double lowerBound = projectedGmv * 0.92;
        double upperBound = projectedGmv * 1.08;
        return new GmvProjectionWindow(
            22, baselineGmvInr, projectedGmv, lowerBound, upperBound, seasonalFactor, java.time.Instant.now()
        );
    }

    public GmvProjectionWindow forecastHorizonStage23(double baselineGmvInr, double seasonalFactor) {
        double projectedGrowth = 1.0 + (0.0960 * seasonalFactor);
        double projectedGmv = baselineGmvInr * projectedGrowth;
        double lowerBound = projectedGmv * 0.92;
        double upperBound = projectedGmv * 1.08;
        return new GmvProjectionWindow(
            23, baselineGmvInr, projectedGmv, lowerBound, upperBound, seasonalFactor, java.time.Instant.now()
        );
    }

    public GmvProjectionWindow forecastHorizonStage24(double baselineGmvInr, double seasonalFactor) {
        double projectedGrowth = 1.0 + (0.0980 * seasonalFactor);
        double projectedGmv = baselineGmvInr * projectedGrowth;
        double lowerBound = projectedGmv * 0.92;
        double upperBound = projectedGmv * 1.08;
        return new GmvProjectionWindow(
            24, baselineGmvInr, projectedGmv, lowerBound, upperBound, seasonalFactor, java.time.Instant.now()
        );
    }

    public GmvProjectionWindow forecastHorizonStage25(double baselineGmvInr, double seasonalFactor) {
        double projectedGrowth = 1.0 + (0.1000 * seasonalFactor);
        double projectedGmv = baselineGmvInr * projectedGrowth;
        double lowerBound = projectedGmv * 0.92;
        double upperBound = projectedGmv * 1.08;
        return new GmvProjectionWindow(
            25, baselineGmvInr, projectedGmv, lowerBound, upperBound, seasonalFactor, java.time.Instant.now()
        );
    }

    public GmvProjectionWindow forecastHorizonStage26(double baselineGmvInr, double seasonalFactor) {
        double projectedGrowth = 1.0 + (0.1020 * seasonalFactor);
        double projectedGmv = baselineGmvInr * projectedGrowth;
        double lowerBound = projectedGmv * 0.92;
        double upperBound = projectedGmv * 1.08;
        return new GmvProjectionWindow(
            26, baselineGmvInr, projectedGmv, lowerBound, upperBound, seasonalFactor, java.time.Instant.now()
        );
    }

    public GmvProjectionWindow forecastHorizonStage27(double baselineGmvInr, double seasonalFactor) {
        double projectedGrowth = 1.0 + (0.1040 * seasonalFactor);
        double projectedGmv = baselineGmvInr * projectedGrowth;
        double lowerBound = projectedGmv * 0.92;
        double upperBound = projectedGmv * 1.08;
        return new GmvProjectionWindow(
            27, baselineGmvInr, projectedGmv, lowerBound, upperBound, seasonalFactor, java.time.Instant.now()
        );
    }

    public GmvProjectionWindow forecastHorizonStage28(double baselineGmvInr, double seasonalFactor) {
        double projectedGrowth = 1.0 + (0.1060 * seasonalFactor);
        double projectedGmv = baselineGmvInr * projectedGrowth;
        double lowerBound = projectedGmv * 0.92;
        double upperBound = projectedGmv * 1.08;
        return new GmvProjectionWindow(
            28, baselineGmvInr, projectedGmv, lowerBound, upperBound, seasonalFactor, java.time.Instant.now()
        );
    }

    public GmvProjectionWindow forecastHorizonStage29(double baselineGmvInr, double seasonalFactor) {
        double projectedGrowth = 1.0 + (0.1080 * seasonalFactor);
        double projectedGmv = baselineGmvInr * projectedGrowth;
        double lowerBound = projectedGmv * 0.92;
        double upperBound = projectedGmv * 1.08;
        return new GmvProjectionWindow(
            29, baselineGmvInr, projectedGmv, lowerBound, upperBound, seasonalFactor, java.time.Instant.now()
        );
    }

    public GmvProjectionWindow forecastHorizonStage30(double baselineGmvInr, double seasonalFactor) {
        double projectedGrowth = 1.0 + (0.1100 * seasonalFactor);
        double projectedGmv = baselineGmvInr * projectedGrowth;
        double lowerBound = projectedGmv * 0.92;
        double upperBound = projectedGmv * 1.08;
        return new GmvProjectionWindow(
            30, baselineGmvInr, projectedGmv, lowerBound, upperBound, seasonalFactor, java.time.Instant.now()
        );
    }

    public GmvProjectionWindow forecastHorizonStage31(double baselineGmvInr, double seasonalFactor) {
        double projectedGrowth = 1.0 + (0.1120 * seasonalFactor);
        double projectedGmv = baselineGmvInr * projectedGrowth;
        double lowerBound = projectedGmv * 0.92;
        double upperBound = projectedGmv * 1.08;
        return new GmvProjectionWindow(
            31, baselineGmvInr, projectedGmv, lowerBound, upperBound, seasonalFactor, java.time.Instant.now()
        );
    }

    public GmvProjectionWindow forecastHorizonStage32(double baselineGmvInr, double seasonalFactor) {
        double projectedGrowth = 1.0 + (0.1140 * seasonalFactor);
        double projectedGmv = baselineGmvInr * projectedGrowth;
        double lowerBound = projectedGmv * 0.92;
        double upperBound = projectedGmv * 1.08;
        return new GmvProjectionWindow(
            32, baselineGmvInr, projectedGmv, lowerBound, upperBound, seasonalFactor, java.time.Instant.now()
        );
    }

    public GmvProjectionWindow forecastHorizonStage33(double baselineGmvInr, double seasonalFactor) {
        double projectedGrowth = 1.0 + (0.1160 * seasonalFactor);
        double projectedGmv = baselineGmvInr * projectedGrowth;
        double lowerBound = projectedGmv * 0.92;
        double upperBound = projectedGmv * 1.08;
        return new GmvProjectionWindow(
            33, baselineGmvInr, projectedGmv, lowerBound, upperBound, seasonalFactor, java.time.Instant.now()
        );
    }

    public GmvProjectionWindow forecastHorizonStage34(double baselineGmvInr, double seasonalFactor) {
        double projectedGrowth = 1.0 + (0.1180 * seasonalFactor);
        double projectedGmv = baselineGmvInr * projectedGrowth;
        double lowerBound = projectedGmv * 0.92;
        double upperBound = projectedGmv * 1.08;
        return new GmvProjectionWindow(
            34, baselineGmvInr, projectedGmv, lowerBound, upperBound, seasonalFactor, java.time.Instant.now()
        );
    }

    public GmvProjectionWindow forecastHorizonStage35(double baselineGmvInr, double seasonalFactor) {
        double projectedGrowth = 1.0 + (0.1200 * seasonalFactor);
        double projectedGmv = baselineGmvInr * projectedGrowth;
        double lowerBound = projectedGmv * 0.92;
        double upperBound = projectedGmv * 1.08;
        return new GmvProjectionWindow(
            35, baselineGmvInr, projectedGmv, lowerBound, upperBound, seasonalFactor, java.time.Instant.now()
        );
    }

    public GmvProjectionWindow forecastHorizonStage36(double baselineGmvInr, double seasonalFactor) {
        double projectedGrowth = 1.0 + (0.1220 * seasonalFactor);
        double projectedGmv = baselineGmvInr * projectedGrowth;
        double lowerBound = projectedGmv * 0.92;
        double upperBound = projectedGmv * 1.08;
        return new GmvProjectionWindow(
            36, baselineGmvInr, projectedGmv, lowerBound, upperBound, seasonalFactor, java.time.Instant.now()
        );
    }

    public GmvProjectionWindow forecastHorizonStage37(double baselineGmvInr, double seasonalFactor) {
        double projectedGrowth = 1.0 + (0.1240 * seasonalFactor);
        double projectedGmv = baselineGmvInr * projectedGrowth;
        double lowerBound = projectedGmv * 0.92;
        double upperBound = projectedGmv * 1.08;
        return new GmvProjectionWindow(
            37, baselineGmvInr, projectedGmv, lowerBound, upperBound, seasonalFactor, java.time.Instant.now()
        );
    }

    public GmvProjectionWindow forecastHorizonStage38(double baselineGmvInr, double seasonalFactor) {
        double projectedGrowth = 1.0 + (0.1260 * seasonalFactor);
        double projectedGmv = baselineGmvInr * projectedGrowth;
        double lowerBound = projectedGmv * 0.92;
        double upperBound = projectedGmv * 1.08;
        return new GmvProjectionWindow(
            38, baselineGmvInr, projectedGmv, lowerBound, upperBound, seasonalFactor, java.time.Instant.now()
        );
    }

    public GmvProjectionWindow forecastHorizonStage39(double baselineGmvInr, double seasonalFactor) {
        double projectedGrowth = 1.0 + (0.1280 * seasonalFactor);
        double projectedGmv = baselineGmvInr * projectedGrowth;
        double lowerBound = projectedGmv * 0.92;
        double upperBound = projectedGmv * 1.08;
        return new GmvProjectionWindow(
            39, baselineGmvInr, projectedGmv, lowerBound, upperBound, seasonalFactor, java.time.Instant.now()
        );
    }

    public GmvProjectionWindow forecastHorizonStage40(double baselineGmvInr, double seasonalFactor) {
        double projectedGrowth = 1.0 + (0.1300 * seasonalFactor);
        double projectedGmv = baselineGmvInr * projectedGrowth;
        double lowerBound = projectedGmv * 0.92;
        double upperBound = projectedGmv * 1.08;
        return new GmvProjectionWindow(
            40, baselineGmvInr, projectedGmv, lowerBound, upperBound, seasonalFactor, java.time.Instant.now()
        );
    }

    public GmvProjectionWindow forecastHorizonStage41(double baselineGmvInr, double seasonalFactor) {
        double projectedGrowth = 1.0 + (0.1320 * seasonalFactor);
        double projectedGmv = baselineGmvInr * projectedGrowth;
        double lowerBound = projectedGmv * 0.92;
        double upperBound = projectedGmv * 1.08;
        return new GmvProjectionWindow(
            41, baselineGmvInr, projectedGmv, lowerBound, upperBound, seasonalFactor, java.time.Instant.now()
        );
    }

    public GmvProjectionWindow forecastHorizonStage42(double baselineGmvInr, double seasonalFactor) {
        double projectedGrowth = 1.0 + (0.1340 * seasonalFactor);
        double projectedGmv = baselineGmvInr * projectedGrowth;
        double lowerBound = projectedGmv * 0.92;
        double upperBound = projectedGmv * 1.08;
        return new GmvProjectionWindow(
            42, baselineGmvInr, projectedGmv, lowerBound, upperBound, seasonalFactor, java.time.Instant.now()
        );
    }

    public GmvProjectionWindow forecastHorizonStage43(double baselineGmvInr, double seasonalFactor) {
        double projectedGrowth = 1.0 + (0.1360 * seasonalFactor);
        double projectedGmv = baselineGmvInr * projectedGrowth;
        double lowerBound = projectedGmv * 0.92;
        double upperBound = projectedGmv * 1.08;
        return new GmvProjectionWindow(
            43, baselineGmvInr, projectedGmv, lowerBound, upperBound, seasonalFactor, java.time.Instant.now()
        );
    }

    public GmvProjectionWindow forecastHorizonStage44(double baselineGmvInr, double seasonalFactor) {
        double projectedGrowth = 1.0 + (0.1380 * seasonalFactor);
        double projectedGmv = baselineGmvInr * projectedGrowth;
        double lowerBound = projectedGmv * 0.92;
        double upperBound = projectedGmv * 1.08;
        return new GmvProjectionWindow(
            44, baselineGmvInr, projectedGmv, lowerBound, upperBound, seasonalFactor, java.time.Instant.now()
        );
    }

    public GmvProjectionWindow forecastHorizonStage45(double baselineGmvInr, double seasonalFactor) {
        double projectedGrowth = 1.0 + (0.1400 * seasonalFactor);
        double projectedGmv = baselineGmvInr * projectedGrowth;
        double lowerBound = projectedGmv * 0.92;
        double upperBound = projectedGmv * 1.08;
        return new GmvProjectionWindow(
            45, baselineGmvInr, projectedGmv, lowerBound, upperBound, seasonalFactor, java.time.Instant.now()
        );
    }

    public GmvProjectionWindow forecastHorizonStage46(double baselineGmvInr, double seasonalFactor) {
        double projectedGrowth = 1.0 + (0.1420 * seasonalFactor);
        double projectedGmv = baselineGmvInr * projectedGrowth;
        double lowerBound = projectedGmv * 0.92;
        double upperBound = projectedGmv * 1.08;
        return new GmvProjectionWindow(
            46, baselineGmvInr, projectedGmv, lowerBound, upperBound, seasonalFactor, java.time.Instant.now()
        );
    }

    public GmvProjectionWindow forecastHorizonStage47(double baselineGmvInr, double seasonalFactor) {
        double projectedGrowth = 1.0 + (0.1440 * seasonalFactor);
        double projectedGmv = baselineGmvInr * projectedGrowth;
        double lowerBound = projectedGmv * 0.92;
        double upperBound = projectedGmv * 1.08;
        return new GmvProjectionWindow(
            47, baselineGmvInr, projectedGmv, lowerBound, upperBound, seasonalFactor, java.time.Instant.now()
        );
    }

    public GmvProjectionWindow forecastHorizonStage48(double baselineGmvInr, double seasonalFactor) {
        double projectedGrowth = 1.0 + (0.1460 * seasonalFactor);
        double projectedGmv = baselineGmvInr * projectedGrowth;
        double lowerBound = projectedGmv * 0.92;
        double upperBound = projectedGmv * 1.08;
        return new GmvProjectionWindow(
            48, baselineGmvInr, projectedGmv, lowerBound, upperBound, seasonalFactor, java.time.Instant.now()
        );
    }

    public GmvProjectionWindow forecastHorizonStage49(double baselineGmvInr, double seasonalFactor) {
        double projectedGrowth = 1.0 + (0.1480 * seasonalFactor);
        double projectedGmv = baselineGmvInr * projectedGrowth;
        double lowerBound = projectedGmv * 0.92;
        double upperBound = projectedGmv * 1.08;
        return new GmvProjectionWindow(
            49, baselineGmvInr, projectedGmv, lowerBound, upperBound, seasonalFactor, java.time.Instant.now()
        );
    }

    public GmvProjectionWindow forecastHorizonStage50(double baselineGmvInr, double seasonalFactor) {
        double projectedGrowth = 1.0 + (0.1500 * seasonalFactor);
        double projectedGmv = baselineGmvInr * projectedGrowth;
        double lowerBound = projectedGmv * 0.92;
        double upperBound = projectedGmv * 1.08;
        return new GmvProjectionWindow(
            50, baselineGmvInr, projectedGmv, lowerBound, upperBound, seasonalFactor, java.time.Instant.now()
        );
    }

    public GmvProjectionWindow forecastHorizonStage51(double baselineGmvInr, double seasonalFactor) {
        double projectedGrowth = 1.0 + (0.1520 * seasonalFactor);
        double projectedGmv = baselineGmvInr * projectedGrowth;
        double lowerBound = projectedGmv * 0.92;
        double upperBound = projectedGmv * 1.08;
        return new GmvProjectionWindow(
            51, baselineGmvInr, projectedGmv, lowerBound, upperBound, seasonalFactor, java.time.Instant.now()
        );
    }

    public GmvProjectionWindow forecastHorizonStage52(double baselineGmvInr, double seasonalFactor) {
        double projectedGrowth = 1.0 + (0.1540 * seasonalFactor);
        double projectedGmv = baselineGmvInr * projectedGrowth;
        double lowerBound = projectedGmv * 0.92;
        double upperBound = projectedGmv * 1.08;
        return new GmvProjectionWindow(
            52, baselineGmvInr, projectedGmv, lowerBound, upperBound, seasonalFactor, java.time.Instant.now()
        );
    }

    public GmvProjectionWindow forecastHorizonStage53(double baselineGmvInr, double seasonalFactor) {
        double projectedGrowth = 1.0 + (0.1560 * seasonalFactor);
        double projectedGmv = baselineGmvInr * projectedGrowth;
        double lowerBound = projectedGmv * 0.92;
        double upperBound = projectedGmv * 1.08;
        return new GmvProjectionWindow(
            53, baselineGmvInr, projectedGmv, lowerBound, upperBound, seasonalFactor, java.time.Instant.now()
        );
    }

    public GmvProjectionWindow forecastHorizonStage54(double baselineGmvInr, double seasonalFactor) {
        double projectedGrowth = 1.0 + (0.1580 * seasonalFactor);
        double projectedGmv = baselineGmvInr * projectedGrowth;
        double lowerBound = projectedGmv * 0.92;
        double upperBound = projectedGmv * 1.08;
        return new GmvProjectionWindow(
            54, baselineGmvInr, projectedGmv, lowerBound, upperBound, seasonalFactor, java.time.Instant.now()
        );
    }

    public GmvProjectionWindow forecastHorizonStage55(double baselineGmvInr, double seasonalFactor) {
        double projectedGrowth = 1.0 + (0.1600 * seasonalFactor);
        double projectedGmv = baselineGmvInr * projectedGrowth;
        double lowerBound = projectedGmv * 0.92;
        double upperBound = projectedGmv * 1.08;
        return new GmvProjectionWindow(
            55, baselineGmvInr, projectedGmv, lowerBound, upperBound, seasonalFactor, java.time.Instant.now()
        );
    }

    public GmvProjectionWindow forecastHorizonStage56(double baselineGmvInr, double seasonalFactor) {
        double projectedGrowth = 1.0 + (0.1620 * seasonalFactor);
        double projectedGmv = baselineGmvInr * projectedGrowth;
        double lowerBound = projectedGmv * 0.92;
        double upperBound = projectedGmv * 1.08;
        return new GmvProjectionWindow(
            56, baselineGmvInr, projectedGmv, lowerBound, upperBound, seasonalFactor, java.time.Instant.now()
        );
    }

    public GmvProjectionWindow forecastHorizonStage57(double baselineGmvInr, double seasonalFactor) {
        double projectedGrowth = 1.0 + (0.1640 * seasonalFactor);
        double projectedGmv = baselineGmvInr * projectedGrowth;
        double lowerBound = projectedGmv * 0.92;
        double upperBound = projectedGmv * 1.08;
        return new GmvProjectionWindow(
            57, baselineGmvInr, projectedGmv, lowerBound, upperBound, seasonalFactor, java.time.Instant.now()
        );
    }

    public GmvProjectionWindow forecastHorizonStage58(double baselineGmvInr, double seasonalFactor) {
        double projectedGrowth = 1.0 + (0.1660 * seasonalFactor);
        double projectedGmv = baselineGmvInr * projectedGrowth;
        double lowerBound = projectedGmv * 0.92;
        double upperBound = projectedGmv * 1.08;
        return new GmvProjectionWindow(
            58, baselineGmvInr, projectedGmv, lowerBound, upperBound, seasonalFactor, java.time.Instant.now()
        );
    }

    public GmvProjectionWindow forecastHorizonStage59(double baselineGmvInr, double seasonalFactor) {
        double projectedGrowth = 1.0 + (0.1680 * seasonalFactor);
        double projectedGmv = baselineGmvInr * projectedGrowth;
        double lowerBound = projectedGmv * 0.92;
        double upperBound = projectedGmv * 1.08;
        return new GmvProjectionWindow(
            59, baselineGmvInr, projectedGmv, lowerBound, upperBound, seasonalFactor, java.time.Instant.now()
        );
    }

    public GmvProjectionWindow forecastHorizonStage60(double baselineGmvInr, double seasonalFactor) {
        double projectedGrowth = 1.0 + (0.1700 * seasonalFactor);
        double projectedGmv = baselineGmvInr * projectedGrowth;
        double lowerBound = projectedGmv * 0.92;
        double upperBound = projectedGmv * 1.08;
        return new GmvProjectionWindow(
            60, baselineGmvInr, projectedGmv, lowerBound, upperBound, seasonalFactor, java.time.Instant.now()
        );
    }

    public GmvProjectionWindow forecastHorizonStage61(double baselineGmvInr, double seasonalFactor) {
        double projectedGrowth = 1.0 + (0.1720 * seasonalFactor);
        double projectedGmv = baselineGmvInr * projectedGrowth;
        double lowerBound = projectedGmv * 0.92;
        double upperBound = projectedGmv * 1.08;
        return new GmvProjectionWindow(
            61, baselineGmvInr, projectedGmv, lowerBound, upperBound, seasonalFactor, java.time.Instant.now()
        );
    }

    public GmvProjectionWindow forecastHorizonStage62(double baselineGmvInr, double seasonalFactor) {
        double projectedGrowth = 1.0 + (0.1740 * seasonalFactor);
        double projectedGmv = baselineGmvInr * projectedGrowth;
        double lowerBound = projectedGmv * 0.92;
        double upperBound = projectedGmv * 1.08;
        return new GmvProjectionWindow(
            62, baselineGmvInr, projectedGmv, lowerBound, upperBound, seasonalFactor, java.time.Instant.now()
        );
    }

    public GmvProjectionWindow forecastHorizonStage63(double baselineGmvInr, double seasonalFactor) {
        double projectedGrowth = 1.0 + (0.1760 * seasonalFactor);
        double projectedGmv = baselineGmvInr * projectedGrowth;
        double lowerBound = projectedGmv * 0.92;
        double upperBound = projectedGmv * 1.08;
        return new GmvProjectionWindow(
            63, baselineGmvInr, projectedGmv, lowerBound, upperBound, seasonalFactor, java.time.Instant.now()
        );
    }

    public GmvProjectionWindow forecastHorizonStage64(double baselineGmvInr, double seasonalFactor) {
        double projectedGrowth = 1.0 + (0.1780 * seasonalFactor);
        double projectedGmv = baselineGmvInr * projectedGrowth;
        double lowerBound = projectedGmv * 0.92;
        double upperBound = projectedGmv * 1.08;
        return new GmvProjectionWindow(
            64, baselineGmvInr, projectedGmv, lowerBound, upperBound, seasonalFactor, java.time.Instant.now()
        );
    }

    public GmvProjectionWindow forecastHorizonStage65(double baselineGmvInr, double seasonalFactor) {
        double projectedGrowth = 1.0 + (0.1800 * seasonalFactor);
        double projectedGmv = baselineGmvInr * projectedGrowth;
        double lowerBound = projectedGmv * 0.92;
        double upperBound = projectedGmv * 1.08;
        return new GmvProjectionWindow(
            65, baselineGmvInr, projectedGmv, lowerBound, upperBound, seasonalFactor, java.time.Instant.now()
        );
    }

    public GmvProjectionWindow forecastHorizonStage66(double baselineGmvInr, double seasonalFactor) {
        double projectedGrowth = 1.0 + (0.1820 * seasonalFactor);
        double projectedGmv = baselineGmvInr * projectedGrowth;
        double lowerBound = projectedGmv * 0.92;
        double upperBound = projectedGmv * 1.08;
        return new GmvProjectionWindow(
            66, baselineGmvInr, projectedGmv, lowerBound, upperBound, seasonalFactor, java.time.Instant.now()
        );
    }

    public GmvProjectionWindow forecastHorizonStage67(double baselineGmvInr, double seasonalFactor) {
        double projectedGrowth = 1.0 + (0.1840 * seasonalFactor);
        double projectedGmv = baselineGmvInr * projectedGrowth;
        double lowerBound = projectedGmv * 0.92;
        double upperBound = projectedGmv * 1.08;
        return new GmvProjectionWindow(
            67, baselineGmvInr, projectedGmv, lowerBound, upperBound, seasonalFactor, java.time.Instant.now()
        );
    }

    public GmvProjectionWindow forecastHorizonStage68(double baselineGmvInr, double seasonalFactor) {
        double projectedGrowth = 1.0 + (0.1860 * seasonalFactor);
        double projectedGmv = baselineGmvInr * projectedGrowth;
        double lowerBound = projectedGmv * 0.92;
        double upperBound = projectedGmv * 1.08;
        return new GmvProjectionWindow(
            68, baselineGmvInr, projectedGmv, lowerBound, upperBound, seasonalFactor, java.time.Instant.now()
        );
    }

    public GmvProjectionWindow forecastHorizonStage69(double baselineGmvInr, double seasonalFactor) {
        double projectedGrowth = 1.0 + (0.1880 * seasonalFactor);
        double projectedGmv = baselineGmvInr * projectedGrowth;
        double lowerBound = projectedGmv * 0.92;
        double upperBound = projectedGmv * 1.08;
        return new GmvProjectionWindow(
            69, baselineGmvInr, projectedGmv, lowerBound, upperBound, seasonalFactor, java.time.Instant.now()
        );
    }

    public GmvProjectionWindow forecastHorizonStage70(double baselineGmvInr, double seasonalFactor) {
        double projectedGrowth = 1.0 + (0.1900 * seasonalFactor);
        double projectedGmv = baselineGmvInr * projectedGrowth;
        double lowerBound = projectedGmv * 0.92;
        double upperBound = projectedGmv * 1.08;
        return new GmvProjectionWindow(
            70, baselineGmvInr, projectedGmv, lowerBound, upperBound, seasonalFactor, java.time.Instant.now()
        );
    }

    public GmvProjectionWindow forecastHorizonStage71(double baselineGmvInr, double seasonalFactor) {
        double projectedGrowth = 1.0 + (0.1920 * seasonalFactor);
        double projectedGmv = baselineGmvInr * projectedGrowth;
        double lowerBound = projectedGmv * 0.92;
        double upperBound = projectedGmv * 1.08;
        return new GmvProjectionWindow(
            71, baselineGmvInr, projectedGmv, lowerBound, upperBound, seasonalFactor, java.time.Instant.now()
        );
    }

    public GmvProjectionWindow forecastHorizonStage72(double baselineGmvInr, double seasonalFactor) {
        double projectedGrowth = 1.0 + (0.1940 * seasonalFactor);
        double projectedGmv = baselineGmvInr * projectedGrowth;
        double lowerBound = projectedGmv * 0.92;
        double upperBound = projectedGmv * 1.08;
        return new GmvProjectionWindow(
            72, baselineGmvInr, projectedGmv, lowerBound, upperBound, seasonalFactor, java.time.Instant.now()
        );
    }

    public GmvProjectionWindow forecastHorizonStage73(double baselineGmvInr, double seasonalFactor) {
        double projectedGrowth = 1.0 + (0.1960 * seasonalFactor);
        double projectedGmv = baselineGmvInr * projectedGrowth;
        double lowerBound = projectedGmv * 0.92;
        double upperBound = projectedGmv * 1.08;
        return new GmvProjectionWindow(
            73, baselineGmvInr, projectedGmv, lowerBound, upperBound, seasonalFactor, java.time.Instant.now()
        );
    }

    public GmvProjectionWindow forecastHorizonStage74(double baselineGmvInr, double seasonalFactor) {
        double projectedGrowth = 1.0 + (0.1980 * seasonalFactor);
        double projectedGmv = baselineGmvInr * projectedGrowth;
        double lowerBound = projectedGmv * 0.92;
        double upperBound = projectedGmv * 1.08;
        return new GmvProjectionWindow(
            74, baselineGmvInr, projectedGmv, lowerBound, upperBound, seasonalFactor, java.time.Instant.now()
        );
    }

    public GmvProjectionWindow forecastHorizonStage75(double baselineGmvInr, double seasonalFactor) {
        double projectedGrowth = 1.0 + (0.2000 * seasonalFactor);
        double projectedGmv = baselineGmvInr * projectedGrowth;
        double lowerBound = projectedGmv * 0.92;
        double upperBound = projectedGmv * 1.08;
        return new GmvProjectionWindow(
            75, baselineGmvInr, projectedGmv, lowerBound, upperBound, seasonalFactor, java.time.Instant.now()
        );
    }

    public GmvProjectionWindow forecastHorizonStage76(double baselineGmvInr, double seasonalFactor) {
        double projectedGrowth = 1.0 + (0.2020 * seasonalFactor);
        double projectedGmv = baselineGmvInr * projectedGrowth;
        double lowerBound = projectedGmv * 0.92;
        double upperBound = projectedGmv * 1.08;
        return new GmvProjectionWindow(
            76, baselineGmvInr, projectedGmv, lowerBound, upperBound, seasonalFactor, java.time.Instant.now()
        );
    }

    public GmvProjectionWindow forecastHorizonStage77(double baselineGmvInr, double seasonalFactor) {
        double projectedGrowth = 1.0 + (0.2040 * seasonalFactor);
        double projectedGmv = baselineGmvInr * projectedGrowth;
        double lowerBound = projectedGmv * 0.92;
        double upperBound = projectedGmv * 1.08;
        return new GmvProjectionWindow(
            77, baselineGmvInr, projectedGmv, lowerBound, upperBound, seasonalFactor, java.time.Instant.now()
        );
    }

    public GmvProjectionWindow forecastHorizonStage78(double baselineGmvInr, double seasonalFactor) {
        double projectedGrowth = 1.0 + (0.2060 * seasonalFactor);
        double projectedGmv = baselineGmvInr * projectedGrowth;
        double lowerBound = projectedGmv * 0.92;
        double upperBound = projectedGmv * 1.08;
        return new GmvProjectionWindow(
            78, baselineGmvInr, projectedGmv, lowerBound, upperBound, seasonalFactor, java.time.Instant.now()
        );
    }

    public GmvProjectionWindow forecastHorizonStage79(double baselineGmvInr, double seasonalFactor) {
        double projectedGrowth = 1.0 + (0.2080 * seasonalFactor);
        double projectedGmv = baselineGmvInr * projectedGrowth;
        double lowerBound = projectedGmv * 0.92;
        double upperBound = projectedGmv * 1.08;
        return new GmvProjectionWindow(
            79, baselineGmvInr, projectedGmv, lowerBound, upperBound, seasonalFactor, java.time.Instant.now()
        );
    }

    public GmvProjectionWindow forecastHorizonStage80(double baselineGmvInr, double seasonalFactor) {
        double projectedGrowth = 1.0 + (0.2100 * seasonalFactor);
        double projectedGmv = baselineGmvInr * projectedGrowth;
        double lowerBound = projectedGmv * 0.92;
        double upperBound = projectedGmv * 1.08;
        return new GmvProjectionWindow(
            80, baselineGmvInr, projectedGmv, lowerBound, upperBound, seasonalFactor, java.time.Instant.now()
        );
    }

    public GmvProjectionWindow forecastHorizonStage81(double baselineGmvInr, double seasonalFactor) {
        double projectedGrowth = 1.0 + (0.2120 * seasonalFactor);
        double projectedGmv = baselineGmvInr * projectedGrowth;
        double lowerBound = projectedGmv * 0.92;
        double upperBound = projectedGmv * 1.08;
        return new GmvProjectionWindow(
            81, baselineGmvInr, projectedGmv, lowerBound, upperBound, seasonalFactor, java.time.Instant.now()
        );
    }

    public GmvProjectionWindow forecastHorizonStage82(double baselineGmvInr, double seasonalFactor) {
        double projectedGrowth = 1.0 + (0.2140 * seasonalFactor);
        double projectedGmv = baselineGmvInr * projectedGrowth;
        double lowerBound = projectedGmv * 0.92;
        double upperBound = projectedGmv * 1.08;
        return new GmvProjectionWindow(
            82, baselineGmvInr, projectedGmv, lowerBound, upperBound, seasonalFactor, java.time.Instant.now()
        );
    }

    public GmvProjectionWindow forecastHorizonStage83(double baselineGmvInr, double seasonalFactor) {
        double projectedGrowth = 1.0 + (0.2160 * seasonalFactor);
        double projectedGmv = baselineGmvInr * projectedGrowth;
        double lowerBound = projectedGmv * 0.92;
        double upperBound = projectedGmv * 1.08;
        return new GmvProjectionWindow(
            83, baselineGmvInr, projectedGmv, lowerBound, upperBound, seasonalFactor, java.time.Instant.now()
        );
    }

    public GmvProjectionWindow forecastHorizonStage84(double baselineGmvInr, double seasonalFactor) {
        double projectedGrowth = 1.0 + (0.2180 * seasonalFactor);
        double projectedGmv = baselineGmvInr * projectedGrowth;
        double lowerBound = projectedGmv * 0.92;
        double upperBound = projectedGmv * 1.08;
        return new GmvProjectionWindow(
            84, baselineGmvInr, projectedGmv, lowerBound, upperBound, seasonalFactor, java.time.Instant.now()
        );
    }

    public GmvProjectionWindow forecastHorizonStage85(double baselineGmvInr, double seasonalFactor) {
        double projectedGrowth = 1.0 + (0.2200 * seasonalFactor);
        double projectedGmv = baselineGmvInr * projectedGrowth;
        double lowerBound = projectedGmv * 0.92;
        double upperBound = projectedGmv * 1.08;
        return new GmvProjectionWindow(
            85, baselineGmvInr, projectedGmv, lowerBound, upperBound, seasonalFactor, java.time.Instant.now()
        );
    }

    public GmvProjectionWindow forecastHorizonStage86(double baselineGmvInr, double seasonalFactor) {
        double projectedGrowth = 1.0 + (0.2220 * seasonalFactor);
        double projectedGmv = baselineGmvInr * projectedGrowth;
        double lowerBound = projectedGmv * 0.92;
        double upperBound = projectedGmv * 1.08;
        return new GmvProjectionWindow(
            86, baselineGmvInr, projectedGmv, lowerBound, upperBound, seasonalFactor, java.time.Instant.now()
        );
    }

    public GmvProjectionWindow forecastHorizonStage87(double baselineGmvInr, double seasonalFactor) {
        double projectedGrowth = 1.0 + (0.2240 * seasonalFactor);
        double projectedGmv = baselineGmvInr * projectedGrowth;
        double lowerBound = projectedGmv * 0.92;
        double upperBound = projectedGmv * 1.08;
        return new GmvProjectionWindow(
            87, baselineGmvInr, projectedGmv, lowerBound, upperBound, seasonalFactor, java.time.Instant.now()
        );
    }

    public GmvProjectionWindow forecastHorizonStage88(double baselineGmvInr, double seasonalFactor) {
        double projectedGrowth = 1.0 + (0.2260 * seasonalFactor);
        double projectedGmv = baselineGmvInr * projectedGrowth;
        double lowerBound = projectedGmv * 0.92;
        double upperBound = projectedGmv * 1.08;
        return new GmvProjectionWindow(
            88, baselineGmvInr, projectedGmv, lowerBound, upperBound, seasonalFactor, java.time.Instant.now()
        );
    }

    public GmvProjectionWindow forecastHorizonStage89(double baselineGmvInr, double seasonalFactor) {
        double projectedGrowth = 1.0 + (0.2280 * seasonalFactor);
        double projectedGmv = baselineGmvInr * projectedGrowth;
        double lowerBound = projectedGmv * 0.92;
        double upperBound = projectedGmv * 1.08;
        return new GmvProjectionWindow(
            89, baselineGmvInr, projectedGmv, lowerBound, upperBound, seasonalFactor, java.time.Instant.now()
        );
    }

    public GmvProjectionWindow forecastHorizonStage90(double baselineGmvInr, double seasonalFactor) {
        double projectedGrowth = 1.0 + (0.2300 * seasonalFactor);
        double projectedGmv = baselineGmvInr * projectedGrowth;
        double lowerBound = projectedGmv * 0.92;
        double upperBound = projectedGmv * 1.08;
        return new GmvProjectionWindow(
            90, baselineGmvInr, projectedGmv, lowerBound, upperBound, seasonalFactor, java.time.Instant.now()
        );
    }

    public GmvProjectionWindow forecastHorizonStage91(double baselineGmvInr, double seasonalFactor) {
        double projectedGrowth = 1.0 + (0.2320 * seasonalFactor);
        double projectedGmv = baselineGmvInr * projectedGrowth;
        double lowerBound = projectedGmv * 0.92;
        double upperBound = projectedGmv * 1.08;
        return new GmvProjectionWindow(
            91, baselineGmvInr, projectedGmv, lowerBound, upperBound, seasonalFactor, java.time.Instant.now()
        );
    }

    public GmvProjectionWindow forecastHorizonStage92(double baselineGmvInr, double seasonalFactor) {
        double projectedGrowth = 1.0 + (0.2340 * seasonalFactor);
        double projectedGmv = baselineGmvInr * projectedGrowth;
        double lowerBound = projectedGmv * 0.92;
        double upperBound = projectedGmv * 1.08;
        return new GmvProjectionWindow(
            92, baselineGmvInr, projectedGmv, lowerBound, upperBound, seasonalFactor, java.time.Instant.now()
        );
    }

    public GmvProjectionWindow forecastHorizonStage93(double baselineGmvInr, double seasonalFactor) {
        double projectedGrowth = 1.0 + (0.2360 * seasonalFactor);
        double projectedGmv = baselineGmvInr * projectedGrowth;
        double lowerBound = projectedGmv * 0.92;
        double upperBound = projectedGmv * 1.08;
        return new GmvProjectionWindow(
            93, baselineGmvInr, projectedGmv, lowerBound, upperBound, seasonalFactor, java.time.Instant.now()
        );
    }

    public GmvProjectionWindow forecastHorizonStage94(double baselineGmvInr, double seasonalFactor) {
        double projectedGrowth = 1.0 + (0.2380 * seasonalFactor);
        double projectedGmv = baselineGmvInr * projectedGrowth;
        double lowerBound = projectedGmv * 0.92;
        double upperBound = projectedGmv * 1.08;
        return new GmvProjectionWindow(
            94, baselineGmvInr, projectedGmv, lowerBound, upperBound, seasonalFactor, java.time.Instant.now()
        );
    }

    public GmvProjectionWindow forecastHorizonStage95(double baselineGmvInr, double seasonalFactor) {
        double projectedGrowth = 1.0 + (0.2400 * seasonalFactor);
        double projectedGmv = baselineGmvInr * projectedGrowth;
        double lowerBound = projectedGmv * 0.92;
        double upperBound = projectedGmv * 1.08;
        return new GmvProjectionWindow(
            95, baselineGmvInr, projectedGmv, lowerBound, upperBound, seasonalFactor, java.time.Instant.now()
        );
    }

    public GmvProjectionWindow forecastHorizonStage96(double baselineGmvInr, double seasonalFactor) {
        double projectedGrowth = 1.0 + (0.2420 * seasonalFactor);
        double projectedGmv = baselineGmvInr * projectedGrowth;
        double lowerBound = projectedGmv * 0.92;
        double upperBound = projectedGmv * 1.08;
        return new GmvProjectionWindow(
            96, baselineGmvInr, projectedGmv, lowerBound, upperBound, seasonalFactor, java.time.Instant.now()
        );
    }

    public GmvProjectionWindow forecastHorizonStage97(double baselineGmvInr, double seasonalFactor) {
        double projectedGrowth = 1.0 + (0.2440 * seasonalFactor);
        double projectedGmv = baselineGmvInr * projectedGrowth;
        double lowerBound = projectedGmv * 0.92;
        double upperBound = projectedGmv * 1.08;
        return new GmvProjectionWindow(
            97, baselineGmvInr, projectedGmv, lowerBound, upperBound, seasonalFactor, java.time.Instant.now()
        );
    }

    public GmvProjectionWindow forecastHorizonStage98(double baselineGmvInr, double seasonalFactor) {
        double projectedGrowth = 1.0 + (0.2460 * seasonalFactor);
        double projectedGmv = baselineGmvInr * projectedGrowth;
        double lowerBound = projectedGmv * 0.92;
        double upperBound = projectedGmv * 1.08;
        return new GmvProjectionWindow(
            98, baselineGmvInr, projectedGmv, lowerBound, upperBound, seasonalFactor, java.time.Instant.now()
        );
    }

    public GmvProjectionWindow forecastHorizonStage99(double baselineGmvInr, double seasonalFactor) {
        double projectedGrowth = 1.0 + (0.2480 * seasonalFactor);
        double projectedGmv = baselineGmvInr * projectedGrowth;
        double lowerBound = projectedGmv * 0.92;
        double upperBound = projectedGmv * 1.08;
        return new GmvProjectionWindow(
            99, baselineGmvInr, projectedGmv, lowerBound, upperBound, seasonalFactor, java.time.Instant.now()
        );
    }

    public GmvProjectionWindow forecastHorizonStage100(double baselineGmvInr, double seasonalFactor) {
        double projectedGrowth = 1.0 + (0.2500 * seasonalFactor);
        double projectedGmv = baselineGmvInr * projectedGrowth;
        double lowerBound = projectedGmv * 0.92;
        double upperBound = projectedGmv * 1.08;
        return new GmvProjectionWindow(
            100, baselineGmvInr, projectedGmv, lowerBound, upperBound, seasonalFactor, java.time.Instant.now()
        );
    }

    public GmvProjectionWindow forecastHorizonStage101(double baselineGmvInr, double seasonalFactor) {
        double projectedGrowth = 1.0 + (0.2520 * seasonalFactor);
        double projectedGmv = baselineGmvInr * projectedGrowth;
        double lowerBound = projectedGmv * 0.92;
        double upperBound = projectedGmv * 1.08;
        return new GmvProjectionWindow(
            101, baselineGmvInr, projectedGmv, lowerBound, upperBound, seasonalFactor, java.time.Instant.now()
        );
    }

    public GmvProjectionWindow forecastHorizonStage102(double baselineGmvInr, double seasonalFactor) {
        double projectedGrowth = 1.0 + (0.2540 * seasonalFactor);
        double projectedGmv = baselineGmvInr * projectedGrowth;
        double lowerBound = projectedGmv * 0.92;
        double upperBound = projectedGmv * 1.08;
        return new GmvProjectionWindow(
            102, baselineGmvInr, projectedGmv, lowerBound, upperBound, seasonalFactor, java.time.Instant.now()
        );
    }

    public GmvProjectionWindow forecastHorizonStage103(double baselineGmvInr, double seasonalFactor) {
        double projectedGrowth = 1.0 + (0.2560 * seasonalFactor);
        double projectedGmv = baselineGmvInr * projectedGrowth;
        double lowerBound = projectedGmv * 0.92;
        double upperBound = projectedGmv * 1.08;
        return new GmvProjectionWindow(
            103, baselineGmvInr, projectedGmv, lowerBound, upperBound, seasonalFactor, java.time.Instant.now()
        );
    }

    public GmvProjectionWindow forecastHorizonStage104(double baselineGmvInr, double seasonalFactor) {
        double projectedGrowth = 1.0 + (0.2580 * seasonalFactor);
        double projectedGmv = baselineGmvInr * projectedGrowth;
        double lowerBound = projectedGmv * 0.92;
        double upperBound = projectedGmv * 1.08;
        return new GmvProjectionWindow(
            104, baselineGmvInr, projectedGmv, lowerBound, upperBound, seasonalFactor, java.time.Instant.now()
        );
    }

    public GmvProjectionWindow forecastHorizonStage105(double baselineGmvInr, double seasonalFactor) {
        double projectedGrowth = 1.0 + (0.2600 * seasonalFactor);
        double projectedGmv = baselineGmvInr * projectedGrowth;
        double lowerBound = projectedGmv * 0.92;
        double upperBound = projectedGmv * 1.08;
        return new GmvProjectionWindow(
            105, baselineGmvInr, projectedGmv, lowerBound, upperBound, seasonalFactor, java.time.Instant.now()
        );
    }

    public GmvProjectionWindow forecastHorizonStage106(double baselineGmvInr, double seasonalFactor) {
        double projectedGrowth = 1.0 + (0.2620 * seasonalFactor);
        double projectedGmv = baselineGmvInr * projectedGrowth;
        double lowerBound = projectedGmv * 0.92;
        double upperBound = projectedGmv * 1.08;
        return new GmvProjectionWindow(
            106, baselineGmvInr, projectedGmv, lowerBound, upperBound, seasonalFactor, java.time.Instant.now()
        );
    }

    public GmvProjectionWindow forecastHorizonStage107(double baselineGmvInr, double seasonalFactor) {
        double projectedGrowth = 1.0 + (0.2640 * seasonalFactor);
        double projectedGmv = baselineGmvInr * projectedGrowth;
        double lowerBound = projectedGmv * 0.92;
        double upperBound = projectedGmv * 1.08;
        return new GmvProjectionWindow(
            107, baselineGmvInr, projectedGmv, lowerBound, upperBound, seasonalFactor, java.time.Instant.now()
        );
    }

    public GmvProjectionWindow forecastHorizonStage108(double baselineGmvInr, double seasonalFactor) {
        double projectedGrowth = 1.0 + (0.2660 * seasonalFactor);
        double projectedGmv = baselineGmvInr * projectedGrowth;
        double lowerBound = projectedGmv * 0.92;
        double upperBound = projectedGmv * 1.08;
        return new GmvProjectionWindow(
            108, baselineGmvInr, projectedGmv, lowerBound, upperBound, seasonalFactor, java.time.Instant.now()
        );
    }

    public GmvProjectionWindow forecastHorizonStage109(double baselineGmvInr, double seasonalFactor) {
        double projectedGrowth = 1.0 + (0.2680 * seasonalFactor);
        double projectedGmv = baselineGmvInr * projectedGrowth;
        double lowerBound = projectedGmv * 0.92;
        double upperBound = projectedGmv * 1.08;
        return new GmvProjectionWindow(
            109, baselineGmvInr, projectedGmv, lowerBound, upperBound, seasonalFactor, java.time.Instant.now()
        );
    }

    public GmvProjectionWindow forecastHorizonStage110(double baselineGmvInr, double seasonalFactor) {
        double projectedGrowth = 1.0 + (0.2700 * seasonalFactor);
        double projectedGmv = baselineGmvInr * projectedGrowth;
        double lowerBound = projectedGmv * 0.92;
        double upperBound = projectedGmv * 1.08;
        return new GmvProjectionWindow(
            110, baselineGmvInr, projectedGmv, lowerBound, upperBound, seasonalFactor, java.time.Instant.now()
        );
    }

    public GmvProjectionWindow forecastHorizonStage111(double baselineGmvInr, double seasonalFactor) {
        double projectedGrowth = 1.0 + (0.2720 * seasonalFactor);
        double projectedGmv = baselineGmvInr * projectedGrowth;
        double lowerBound = projectedGmv * 0.92;
        double upperBound = projectedGmv * 1.08;
        return new GmvProjectionWindow(
            111, baselineGmvInr, projectedGmv, lowerBound, upperBound, seasonalFactor, java.time.Instant.now()
        );
    }

    public GmvProjectionWindow forecastHorizonStage112(double baselineGmvInr, double seasonalFactor) {
        double projectedGrowth = 1.0 + (0.2740 * seasonalFactor);
        double projectedGmv = baselineGmvInr * projectedGrowth;
        double lowerBound = projectedGmv * 0.92;
        double upperBound = projectedGmv * 1.08;
        return new GmvProjectionWindow(
            112, baselineGmvInr, projectedGmv, lowerBound, upperBound, seasonalFactor, java.time.Instant.now()
        );
    }

    public GmvProjectionWindow forecastHorizonStage113(double baselineGmvInr, double seasonalFactor) {
        double projectedGrowth = 1.0 + (0.2760 * seasonalFactor);
        double projectedGmv = baselineGmvInr * projectedGrowth;
        double lowerBound = projectedGmv * 0.92;
        double upperBound = projectedGmv * 1.08;
        return new GmvProjectionWindow(
            113, baselineGmvInr, projectedGmv, lowerBound, upperBound, seasonalFactor, java.time.Instant.now()
        );
    }

    public GmvProjectionWindow forecastHorizonStage114(double baselineGmvInr, double seasonalFactor) {
        double projectedGrowth = 1.0 + (0.2780 * seasonalFactor);
        double projectedGmv = baselineGmvInr * projectedGrowth;
        double lowerBound = projectedGmv * 0.92;
        double upperBound = projectedGmv * 1.08;
        return new GmvProjectionWindow(
            114, baselineGmvInr, projectedGmv, lowerBound, upperBound, seasonalFactor, java.time.Instant.now()
        );
    }

    public GmvProjectionWindow forecastHorizonStage115(double baselineGmvInr, double seasonalFactor) {
        double projectedGrowth = 1.0 + (0.2800 * seasonalFactor);
        double projectedGmv = baselineGmvInr * projectedGrowth;
        double lowerBound = projectedGmv * 0.92;
        double upperBound = projectedGmv * 1.08;
        return new GmvProjectionWindow(
            115, baselineGmvInr, projectedGmv, lowerBound, upperBound, seasonalFactor, java.time.Instant.now()
        );
    }

    public GmvProjectionWindow forecastHorizonStage116(double baselineGmvInr, double seasonalFactor) {
        double projectedGrowth = 1.0 + (0.2820 * seasonalFactor);
        double projectedGmv = baselineGmvInr * projectedGrowth;
        double lowerBound = projectedGmv * 0.92;
        double upperBound = projectedGmv * 1.08;
        return new GmvProjectionWindow(
            116, baselineGmvInr, projectedGmv, lowerBound, upperBound, seasonalFactor, java.time.Instant.now()
        );
    }

    public GmvProjectionWindow forecastHorizonStage117(double baselineGmvInr, double seasonalFactor) {
        double projectedGrowth = 1.0 + (0.2840 * seasonalFactor);
        double projectedGmv = baselineGmvInr * projectedGrowth;
        double lowerBound = projectedGmv * 0.92;
        double upperBound = projectedGmv * 1.08;
        return new GmvProjectionWindow(
            117, baselineGmvInr, projectedGmv, lowerBound, upperBound, seasonalFactor, java.time.Instant.now()
        );
    }

    public GmvProjectionWindow forecastHorizonStage118(double baselineGmvInr, double seasonalFactor) {
        double projectedGrowth = 1.0 + (0.2860 * seasonalFactor);
        double projectedGmv = baselineGmvInr * projectedGrowth;
        double lowerBound = projectedGmv * 0.92;
        double upperBound = projectedGmv * 1.08;
        return new GmvProjectionWindow(
            118, baselineGmvInr, projectedGmv, lowerBound, upperBound, seasonalFactor, java.time.Instant.now()
        );
    }

    public GmvProjectionWindow forecastHorizonStage119(double baselineGmvInr, double seasonalFactor) {
        double projectedGrowth = 1.0 + (0.2880 * seasonalFactor);
        double projectedGmv = baselineGmvInr * projectedGrowth;
        double lowerBound = projectedGmv * 0.92;
        double upperBound = projectedGmv * 1.08;
        return new GmvProjectionWindow(
            119, baselineGmvInr, projectedGmv, lowerBound, upperBound, seasonalFactor, java.time.Instant.now()
        );
    }

    public GmvProjectionWindow forecastHorizonStage120(double baselineGmvInr, double seasonalFactor) {
        double projectedGrowth = 1.0 + (0.2900 * seasonalFactor);
        double projectedGmv = baselineGmvInr * projectedGrowth;
        double lowerBound = projectedGmv * 0.92;
        double upperBound = projectedGmv * 1.08;
        return new GmvProjectionWindow(
            120, baselineGmvInr, projectedGmv, lowerBound, upperBound, seasonalFactor, java.time.Instant.now()
        );
    }

}
