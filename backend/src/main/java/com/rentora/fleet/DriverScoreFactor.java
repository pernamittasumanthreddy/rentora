package com.rentora.fleet;

public class DriverScoreFactor {
    private final String factorCode;
    private final double score;
    private final double totalPenalty;
    private final String drivingClassification;

    public DriverScoreFactor(String factorCode, double score, double totalPenalty, String drivingClassification) {
        this.factorCode = factorCode;
        this.score = score;
        this.totalPenalty = totalPenalty;
        this.drivingClassification = drivingClassification;
    }

    public String getFactorCode() { return factorCode; }
    public double getScore() { return score; }
    public double getTotalPenalty() { return totalPenalty; }
    public String getDrivingClassification() { return drivingClassification; }
}
