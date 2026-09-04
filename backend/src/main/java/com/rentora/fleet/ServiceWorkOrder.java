package com.rentora.fleet;

import java.time.LocalDate;

public class ServiceWorkOrder {
    private final String orderId;
    private final String serviceType;
    private final LocalDate serviceDate;
    private final double cost;
    private final String serviceCenter;
    private final String notes;

    public ServiceWorkOrder(String orderId, String serviceType, LocalDate serviceDate, double cost, String serviceCenter, String notes) {
        this.orderId = orderId;
        this.serviceType = serviceType;
        this.serviceDate = serviceDate;
        this.cost = cost;
        this.serviceCenter = serviceCenter;
        this.notes = notes;
    }

    public String getOrderId() { return orderId; }
    public String getServiceType() { return serviceType; }
    public LocalDate getServiceDate() { return serviceDate; }
    public double getCost() { return cost; }
    public String getServiceCenter() { return serviceCenter; }
    public String getNotes() { return notes; }
}
