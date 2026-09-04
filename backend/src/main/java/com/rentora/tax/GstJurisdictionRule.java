package com.rentora.tax;

public class GstJurisdictionRule {
    private final String stateCode;
    private final String stateName;
    private final String alphaCode;
    private final boolean intraStateEligible;
    private final double cgstRate;
    private final double sgstRate;
    private final double igstRate;
    private final String sacCode;
    private final String notes;

    public GstJurisdictionRule(String stateCode, String stateName, String alphaCode, boolean intraStateEligible, double cgstRate, double sgstRate, double igstRate, String sacCode, String notes) {
        this.stateCode = stateCode;
        this.stateName = stateName;
        this.alphaCode = alphaCode;
        this.intraStateEligible = intraStateEligible;
        this.cgstRate = cgstRate;
        this.sgstRate = sgstRate;
        this.igstRate = igstRate;
        this.sacCode = sacCode;
        this.notes = notes;
    }

    public String getStateCode() { return stateCode; }
    public String getStateName() { return stateName; }
    public String getAlphaCode() { return alphaCode; }
    public boolean isIntraStateEligible() { return intraStateEligible; }
    public double getCgstRate() { return cgstRate; }
    public double getSgstRate() { return sgstRate; }
    public double getIgstRate() { return igstRate; }
    public String getSacCode() { return sacCode; }
    public String getNotes() { return notes; }
}
