package com.rentora.inspection;

import java.math.BigDecimal;
import java.time.Instant;
import java.util.*;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

/**
 * 5-Point Return Inspection Protocol Protocol Engine.
 * Formally evaluates physical condition across Chassis, Optics/Glass, Electronics,
 * Accessories Checklist, and Operational Functional Tests.
 */
public class DigitalInspectionProtocol {
    private static final Logger log = LoggerFactory.getLogger(DigitalInspectionProtocol.class);

    public InspectionEvaluation assessCondition(InspectionReportInput input) {
        List<ChecklistItemResult> results = new ArrayList<>();
        BigDecimal totalDamageAssessment = BigDecimal.ZERO;

        // 1. Physical & Chassis
        results.add(new ChecklistItemResult("CHASSIS_BODY", input.isChassisClean(), input.getChassisNotes(), input.getChassisDamageFee()));
        totalDamageAssessment = totalDamageAssessment.add(input.getChassisDamageFee());

        // 2. Optics / Glass / Sensor
        results.add(new ChecklistItemResult("OPTICS_GLASS", input.isOpticsFlawless(), input.getOpticsNotes(), input.getOpticsDamageFee()));
        totalDamageAssessment = totalDamageAssessment.add(input.getOpticsDamageFee());

        // 3. Electronic Diagnostics
        results.add(new ChecklistItemResult("ELECTRONICS", input.isElectronicsSound(), input.getElectronicsNotes(), input.getElectronicsDamageFee()));
        totalDamageAssessment = totalDamageAssessment.add(input.getElectronicsDamageFee());

        // 4. Kit Accessories Inclusions
        results.add(new ChecklistItemResult("ACCESSORIES_KIT", input.isAllAccessoriesPresent(), input.getAccessoriesNotes(), input.getAccessoriesMissingFee()));
        totalDamageAssessment = totalDamageAssessment.add(input.getAccessoriesMissingFee());

        // 5. Functional Operational Test
        results.add(new ChecklistItemResult("OPERATIONAL_TEST", input.isOperationalPass(), input.getOperationalNotes(), input.getOperationalDamageFee()));
        totalDamageAssessment = totalDamageAssessment.add(input.getOperationalDamageFee());

        boolean isCleanReturn = totalDamageAssessment.compareTo(BigDecimal.ZERO) == 0;
        ConditionGrade grade = isCleanReturn ? ConditionGrade.GRADE_A_PRISTINE : ConditionGrade.GRADE_C_DAMAGED;

        log.info("Inspection evaluated for Rental #{}: Grade {}, Total Damages: INR {}",
            input.getRentalId(), grade, totalDamageAssessment);

        return new InspectionEvaluation(
            input.getRentalId(),
            input.getInspectorName(),
            grade,
            isCleanReturn,
            totalDamageAssessment,
            results,
            input.getPhotographicProofs(),
            Instant.now()
        );
    }
}
