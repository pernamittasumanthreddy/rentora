package com.rentora.analytics;

import java.math.BigDecimal;
import java.math.RoundingMode;
import java.util.*;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class BusinessIntelligenceAggregator {
    private static final Logger log = LoggerFactory.getLogger(BusinessIntelligenceAggregator.class);

    public PlatformMetrics computePlatformHealth(List<OrderMetricSample> samples) {
        if (samples == null || samples.isEmpty()) {
            return new PlatformMetrics(BigDecimal.ZERO, 0, BigDecimal.ZERO, 100.0, 0.0);
        }

        BigDecimal totalGmv = BigDecimal.ZERO;
        int totalBookings = samples.size();
        int disputeCount = 0;

        for (OrderMetricSample sample : samples) {
            totalGmv = totalGmv.add(sample.getOrderAmount());
            if (sample.isDisputed()) {
                disputeCount++;
            }
        }

        BigDecimal avgOrderValue = totalGmv.divide(BigDecimal.valueOf(totalBookings), 2, RoundingMode.HALF_UP);
        double disputeFreeRate = 100.0 - (((double) disputeCount / totalBookings) * 100.0);
        double takeRateCommission = 10.0; // 10% platform take rate

        log.info("Platform Health aggregated: GMV INR {}, Bookings {}, Dispute-free: {}%",
            totalGmv, totalBookings, disputeFreeRate);

        return new PlatformMetrics(totalGmv, totalBookings, avgOrderValue, disputeFreeRate, takeRateCommission);
    }
}
