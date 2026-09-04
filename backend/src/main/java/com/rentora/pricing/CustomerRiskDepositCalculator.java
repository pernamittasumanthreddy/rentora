package com.rentora.pricing;

import java.math.BigDecimal;
import java.math.RoundingMode;

public class CustomerRiskDepositCalculator {

    public BigDecimal computeAdjustedDeposit(BigDecimal baseDeposit, int customerTrustScore) {
        if (baseDeposit == null || baseDeposit.compareTo(BigDecimal.ZERO) <= 0) {
            return BigDecimal.ZERO;
        }

        // Trust score ranges from 0 to 100
        // Score 95 - 100: 20% discount on required deposit
        // Score 85 - 94: 10% discount
        // Score 60 - 84: Standard deposit (100%)
        // Score < 60: High risk +25% deposit requirement
        double multiplier = 1.0;
        if (customerTrustScore >= 95) {
            multiplier = 0.80;
        } else if (customerTrustScore >= 85) {
            multiplier = 0.90;
        } else if (customerTrustScore < 60) {
            multiplier = 1.25;
        }

        return baseDeposit.multiply(BigDecimal.valueOf(multiplier)).setScale(2, RoundingMode.HALF_UP);
    }
}
