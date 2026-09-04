package com.rentora.analytics;

import java.math.BigDecimal;

public class OrderMetricSample {
    private final long orderId;
    private final BigDecimal orderAmount;
    private final boolean disputed;

    public OrderMetricSample(long orderId, BigDecimal orderAmount, boolean disputed) {
        this.orderId = orderId;
        this.orderAmount = orderAmount;
        this.disputed = disputed;
    }

    public long getOrderId() { return orderId; }
    public BigDecimal getOrderAmount() { return orderAmount; }
    public boolean isDisputed() { return disputed; }
}
