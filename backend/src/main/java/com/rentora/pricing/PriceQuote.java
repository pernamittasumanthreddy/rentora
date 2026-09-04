package com.rentora.pricing;

import java.math.BigDecimal;

public class PriceQuote {
    private final long productId;
    private final int durationDays;
    private final BigDecimal baseDailyRate;
    private final BigDecimal finalDailyRate;
    private final double durationDiscountPercent;
    private final double surgeMultiplier;
    private final BigDecimal rentalSubtotal;
    private final BigDecimal cgst;
    private final BigDecimal sgst;
    private final BigDecimal taxTotal;
    private final BigDecimal refundableDeposit;
    private final BigDecimal grandTotalPayable;

    public PriceQuote(
        long productId, int durationDays, BigDecimal baseDailyRate, BigDecimal finalDailyRate,
        double durationDiscountPercent, double surgeMultiplier, BigDecimal rentalSubtotal,
        BigDecimal cgst, BigDecimal sgst, BigDecimal taxTotal, BigDecimal refundableDeposit,
        BigDecimal grandTotalPayable
    ) {
        this.productId = productId;
        this.durationDays = durationDays;
        this.baseDailyRate = baseDailyRate;
        this.finalDailyRate = finalDailyRate;
        this.durationDiscountPercent = durationDiscountPercent;
        this.surgeMultiplier = surgeMultiplier;
        this.rentalSubtotal = rentalSubtotal;
        this.cgst = cgst;
        this.sgst = sgst;
        this.taxTotal = taxTotal;
        this.refundableDeposit = refundableDeposit;
        this.grandTotalPayable = grandTotalPayable;
    }

    public long getProductId() { return productId; }
    public int getDurationDays() { return durationDays; }
    public BigDecimal getBaseDailyRate() { return baseDailyRate; }
    public BigDecimal getFinalDailyRate() { return finalDailyRate; }
    public double getDurationDiscountPercent() { return durationDiscountPercent; }
    public double getSurgeMultiplier() { return surgeMultiplier; }
    public BigDecimal getRentalSubtotal() { return rentalSubtotal; }
    public BigDecimal getCgst() { return cgst; }
    public BigDecimal getSgst() { return sgst; }
    public BigDecimal getTaxTotal() { return taxTotal; }
    public BigDecimal getRefundableDeposit() { return refundableDeposit; }
    public BigDecimal getGrandTotalPayable() { return grandTotalPayable; }
}
