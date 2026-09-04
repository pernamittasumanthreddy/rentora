package com.rentora.inspection;

import java.math.BigDecimal;

public class ChecklistItemResult {
    private final String category;
    private final boolean passed;
    private final String observations;
    private final BigDecimal assessedPenalty;

    public ChecklistItemResult(String category, boolean passed, String observations, BigDecimal assessedPenalty) {
        this.category = category;
        this.passed = passed;
        this.observations = observations;
        this.assessedPenalty = assessedPenalty;
    }

    public String getCategory() { return category; }
    public boolean isPassed() { return passed; }
    public String getObservations() { return observations; }
    public BigDecimal getAssessedPenalty() { return assessedPenalty; }
}
