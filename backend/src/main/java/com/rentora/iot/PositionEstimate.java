package com.rentora.iot;

public class PositionEstimate {
    private final double smoothedLatitude;
    private final double smoothedLongitude;
    private final double kalmanGain;
    private final double estimateVariance;
    private final double speedKmh;
    private final long timestampMs;

    public PositionEstimate(double smoothedLatitude, double smoothedLongitude, double kalmanGain, double estimateVariance, double speedKmh, long timestampMs) {
        this.smoothedLatitude = smoothedLatitude;
        this.smoothedLongitude = smoothedLongitude;
        this.kalmanGain = kalmanGain;
        this.estimateVariance = estimateVariance;
        this.speedKmh = speedKmh;
        this.timestampMs = timestampMs;
    }

    public double getSmoothedLatitude() { return smoothedLatitude; }
    public double getSmoothedLongitude() { return smoothedLongitude; }
    public double getKalmanGain() { return kalmanGain; }
    public double getEstimateVariance() { return estimateVariance; }
    public double getSpeedKmh() { return speedKmh; }
    public long getTimestampMs() { return timestampMs; }
}
