package com.rentora.pricing;

import java.math.BigDecimal;
import java.math.RoundingMode;
import java.time.DayOfWeek;
import java.time.LocalDate;
import java.util.*;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

/**
 * Enterprise Dynamic Pricing Optimizer.
 * Computes base rate scaling based on duration tiers, fleet demand saturation,
 * seasonal surge calendar, and renter trust score safety credits.
 */
public class DynamicPricingAlgorithm {
    private static final Logger log = LoggerFactory.getLogger(DynamicPricingAlgorithm.class);

    private final SurgeMultiplierCalculator surgeCalc = new SurgeMultiplierCalculator();
    private final VolumeDiscountTierMatrix volumeMatrix = new VolumeDiscountTierMatrix();
    private final CustomerRiskDepositCalculator depositCalc = new CustomerRiskDepositCalculator();

    public PriceQuote calculateQuote(
            long productId,
            BigDecimal baseDailyRate,
            BigDecimal baseDeposit,
            LocalDate startDate,
            LocalDate endDate,
            int customerTrustScore,
            double fleetUtilizationRatio
    ) {
        int durationDays = (int) java.time.temporal.ChronoUnit.DAYS.between(startDate, endDate);
        if (durationDays <= 0) durationDays = 1;

        // 1. Calculate duration volume discount
        double durationDiscountFactor = volumeMatrix.getDiscountFactor(durationDays);
        BigDecimal dailyRateAfterVolume = baseDailyRate.multiply(BigDecimal.valueOf(1.0 - durationDiscountFactor))
            .setScale(2, RoundingMode.HALF_UP);

        // 2. Calculate seasonal and weekend surge multipliers
        double surgeMultiplier = surgeCalc.calculateCompositeSurge(startDate, endDate, fleetUtilizationRatio);
        BigDecimal finalDailyRate = dailyRateAfterVolume.multiply(BigDecimal.valueOf(surgeMultiplier))
            .setScale(2, RoundingMode.HALF_UP);

        // 3. Compute base rental subtotal
        BigDecimal rentalSubtotal = finalDailyRate.multiply(BigDecimal.valueOf(durationDays))
            .setScale(2, RoundingMode.HALF_UP);

        // 4. Calculate Risk-Adjusted Deposit based on Customer Trust Score (0 - 100)
        BigDecimal finalDeposit = depositCalc.computeAdjustedDeposit(baseDeposit, customerTrustScore);

        // 5. GST (18% Total: 9% CGST + 9% SGST)
        BigDecimal cgst = rentalSubtotal.multiply(new BigDecimal("0.09")).setScale(2, RoundingMode.HALF_UP);
        BigDecimal sgst = rentalSubtotal.multiply(new BigDecimal("0.09")).setScale(2, RoundingMode.HALF_UP);
        BigDecimal taxTotal = cgst.add(sgst);

        BigDecimal grandTotal = rentalSubtotal.add(taxTotal).add(finalDeposit);

        log.debug("Quote for Product #{}: {} days @ INR {}/day (Surge {}x). Subtotal: {}, Deposit: {}, Grand: {}",
            productId, durationDays, finalDailyRate, surgeMultiplier, rentalSubtotal, finalDeposit, grandTotal);

        return new PriceQuote(
            productId, durationDays, baseDailyRate, finalDailyRate, durationDiscountFactor,
            surgeMultiplier, rentalSubtotal, cgst, sgst, taxTotal, finalDeposit, grandTotal
        );
    }
}
