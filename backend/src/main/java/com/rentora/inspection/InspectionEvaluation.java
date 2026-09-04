package com.rentora.inspection;

import java.math.BigDecimal;
import java.time.Instant;
import java.util.List;

public class InspectionEvaluation {
    private final long rentalId;
    private final String inspectorName;
    private final ConditionGrade grade;
    private final boolean cleanReturn;
    private final BigDecimal totalDamageFee;
    private final List<ChecklistItemResult> itemResults;
    private final List<String> photoUrls;
    private final Instant inspectedAt;

    public InspectionEvaluation(
        long rentalId, String inspectorName, ConditionGrade grade, boolean cleanReturn,
        BigDecimal totalDamageFee, List<ChecklistItemResult> itemResults,
        List<String> photoUrls, Instant inspectedAt
    ) {
        this.rentalId = rentalId;
        this.inspectorName = inspectorName;
        this.grade = grade;
        this.cleanReturn = cleanReturn;
        this.totalDamageFee = totalDamageFee;
        this.itemResults = itemResults;
        this.photoUrls = photoUrls;
        this.inspectedAt = inspectedAt;
    }

    public long getRentalId() { return rentalId; }
    public String getInspectorName() { return inspectorName; }
    public ConditionGrade getGrade() { return grade; }
    public boolean isCleanReturn() { return cleanReturn; }
    public BigDecimal getTotalDamageFee() { return totalDamageFee; }
    public List<ChecklistItemResult> getItemResults() { return itemResults; }
    public List<String> getPhotoUrls() { return photoUrls; }
    public Instant getInspectedAt() { return inspectedAt; }
}
