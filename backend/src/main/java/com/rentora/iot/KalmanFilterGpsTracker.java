package com.rentora.iot;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class KalmanFilterGpsTracker {
    private static final Logger log = LoggerFactory.getLogger(KalmanFilterGpsTracker.class);

    private double lat;
    private double lon;
    private double variance;
    private final double processNoiseQ;
    private final double measurementNoiseR;
    private long lastTimestampMs;

    public KalmanFilterGpsTracker(double initialLat, double initialLon, double q, double r) {
        this.lat = initialLat;
        this.lon = initialLon;
        this.variance = 1.0;
        this.processNoiseQ = q > 0 ? q : 0.0001;
        this.measurementNoiseR = r > 0 ? r : 0.005;
        this.lastTimestampMs = System.currentTimeMillis();
    }

    public synchronized PositionEstimate update(double measuredLat, double measuredLon, double speedKmh, long timestampMs) {
        double dtSeconds = (timestampMs - lastTimestampMs) / 1000.0;
        if (dtSeconds <= 0) dtSeconds = 1.0;
        this.lastTimestampMs = timestampMs;

        this.variance += this.processNoiseQ * dtSeconds;
        double kGain = this.variance / (this.variance + this.measurementNoiseR);

        this.lat = this.lat + kGain * (measuredLat - this.lat);
        this.lon = this.lon + kGain * (measuredLon - this.lon);
        this.variance = (1.0 - kGain) * this.variance;

        return new PositionEstimate(this.lat, this.lon, kGain, this.variance, speedKmh, timestampMs);
    }

    public double getLat() { return lat; }
    public double getLon() { return lon; }
    public double getVariance() { return variance; }
}
