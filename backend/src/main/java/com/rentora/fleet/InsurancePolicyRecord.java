package com.rentora.fleet;

import java.time.LocalDate;

public class InsurancePolicyRecord {
    private final String policyNumber;
    private final String provider;
    private final String policyType;
    private final double insuredDeclaredValue;
    private final LocalDate startDate;
    private final LocalDate expiryDate;
    private final boolean zeroDepreciationCoverage;

    public InsurancePolicyRecord(String policyNumber, String provider, String policyType, double insuredDeclaredValue, LocalDate startDate, LocalDate expiryDate, boolean zeroDepreciationCoverage) {
        this.policyNumber = policyNumber;
        this.provider = provider;
        this.policyType = policyType;
        this.insuredDeclaredValue = insuredDeclaredValue;
        this.startDate = startDate;
        this.expiryDate = expiryDate;
        this.zeroDepreciationCoverage = zeroDepreciationCoverage;
    }

    public String getPolicyNumber() { return policyNumber; }
    public String getProvider() { return provider; }
    public String getPolicyType() { return policyType; }
    public double getInsuredDeclaredValue() { return insuredDeclaredValue; }
    public LocalDate getStartDate() { return startDate; }
    public LocalDate getExpiryDate() { return expiryDate; }
    public boolean isZeroDepreciationCoverage() { return zeroDepreciationCoverage; }
}
