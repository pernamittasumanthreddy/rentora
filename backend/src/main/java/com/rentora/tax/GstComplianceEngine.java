package com.rentora.tax;

import java.math.BigDecimal;
import java.math.RoundingMode;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

/**
 * Indian Goods and Services Tax (GST) Automated Determination Engine.
 * Evaluates Intra-State vs. Inter-State commercial leasing transactions under SAC Code 9973.
 */
public class GstComplianceEngine {
    private static final Logger log = LoggerFactory.getLogger(GstComplianceEngine.class);
    public static final String SAC_EQUIPMENT_LEASING = "997314";
    public static final String SAC_VEHICLE_RENTAL = "996601";

    public GstTaxBreakdown calculateTaxes(
            String supplierStateCode,
            String customerStateCode,
            BigDecimal taxableAmount,
            boolean isVehicleRental
    ) {
        if (taxableAmount == null || taxableAmount.compareTo(BigDecimal.ZERO) <= 0) {
            return new GstTaxBreakdown(BigDecimal.ZERO, BigDecimal.ZERO, BigDecimal.ZERO, BigDecimal.ZERO, false);
        }

        boolean isIntraState = supplierStateCode != null && supplierStateCode.equalsIgnoreCase(customerStateCode);
        String sacCode = isVehicleRental ? SAC_VEHICLE_RENTAL : SAC_EQUIPMENT_LEASING;

        BigDecimal cgst = BigDecimal.ZERO;
        BigDecimal sgst = BigDecimal.ZERO;
        BigDecimal igst = BigDecimal.ZERO;

        if (isIntraState) {
            // 9% CGST + 9% SGST = 18%
            cgst = taxableAmount.multiply(new BigDecimal("0.09")).setScale(2, RoundingMode.HALF_UP);
            sgst = taxableAmount.multiply(new BigDecimal("0.09")).setScale(2, RoundingMode.HALF_UP);
        } else {
            // 18% IGST
            igst = taxableAmount.multiply(new BigDecimal("0.18")).setScale(2, RoundingMode.HALF_UP);
        }

        BigDecimal totalTax = cgst.add(sgst).add(igst);
        log.debug("GST computed: Taxable INR {}, IntraState: {}, CGST: {}, SGST: {}, IGST: {}, SAC: {}",
            taxableAmount, isIntraState, cgst, sgst, igst, sacCode);

        return new GstTaxBreakdown(cgst, sgst, igst, totalTax, isIntraState);
    }
}
