package com.rentora.tax;

import java.math.BigDecimal;

public class GstTaxBreakdown {
    private final BigDecimal cgst;
    private final BigDecimal sgst;
    private final BigDecimal igst;
    private final BigDecimal totalTax;
    private final boolean intraState;

    public GstTaxBreakdown(BigDecimal cgst, BigDecimal sgst, BigDecimal igst, BigDecimal totalTax, boolean intraState) {
        this.cgst = cgst;
        this.sgst = sgst;
        this.igst = igst;
        this.totalTax = totalTax;
        this.intraState = intraState;
    }

    public BigDecimal getCgst() { return cgst; }
    public BigDecimal getSgst() { return sgst; }
    public BigDecimal getIgst() { return igst; }
    public BigDecimal getTotalTax() { return totalTax; }
    public boolean isIntraState() { return intraState; }
}
