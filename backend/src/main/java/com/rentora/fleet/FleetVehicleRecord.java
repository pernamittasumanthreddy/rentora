package com.rentora.fleet;

import java.time.LocalDate;

public class FleetVehicleRecord {
    private final String vin;
    private final String registrationNumber;
    private final String modelName;
    private final String category;
    private final String assignedCity;
    private double currentOdometerKm;
    private String operationalStatus;
    private final LocalDate purchaseDate;

    public FleetVehicleRecord(String vin, String registrationNumber, String modelName, String category, String assignedCity, double currentOdometerKm, String operationalStatus, LocalDate purchaseDate) {
        this.vin = vin;
        this.registrationNumber = registrationNumber;
        this.modelName = modelName;
        this.category = category;
        this.assignedCity = assignedCity;
        this.currentOdometerKm = currentOdometerKm;
        this.operationalStatus = operationalStatus;
        this.purchaseDate = purchaseDate;
    }

    public String getVin() { return vin; }
    public String getRegistrationNumber() { return registrationNumber; }
    public String getModelName() { return modelName; }
    public String getCategory() { return category; }
    public String getAssignedCity() { return assignedCity; }
    public double getCurrentOdometerKm() { return currentOdometerKm; }
    public void setCurrentOdometerKm(double km) { this.currentOdometerKm = km; }
    public String getOperationalStatus() { return operationalStatus; }
    public void setOperationalStatus(String status) { this.operationalStatus = status; }
    public LocalDate getPurchaseDate() { return purchaseDate; }
}
