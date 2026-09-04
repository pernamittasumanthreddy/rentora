package com.rentora.tax;

import java.math.BigDecimal;
import java.time.LocalDate;

public class CommercialInvoice {
    private final String invoiceNumber;
    private final long rentalId;
    private final LocalDate invoiceDate;
    private final String customerName;
    private final String customerGstin;
    private final String vendorBusinessName;
    private final String vendorGstin;
    private final BigDecimal taxableRent;
    private final BigDecimal cgst;
    private final BigDecimal sgst;
    private final BigDecimal igst;
    private final BigDecimal totalGst;
    private final BigDecimal totalAmount;

    public CommercialInvoice(
        String invoiceNumber, long rentalId, LocalDate invoiceDate, String customerName,
        String customerGstin, String vendorBusinessName, String vendorGstin,
        BigDecimal taxableRent, BigDecimal cgst, BigDecimal sgst, BigDecimal igst,
        BigDecimal totalGst, BigDecimal totalAmount
    ) {
        this.invoiceNumber = invoiceNumber;
        this.rentalId = rentalId;
        this.invoiceDate = invoiceDate;
        this.customerName = customerName;
        this.customerGstin = customerGstin;
        this.vendorBusinessName = vendorBusinessName;
        this.vendorGstin = vendorGstin;
        this.taxableRent = taxableRent;
        this.cgst = cgst;
        this.sgst = sgst;
        this.igst = igst;
        this.totalGst = totalGst;
        this.totalAmount = totalAmount;
    }

    public String getInvoiceNumber() { return invoiceNumber; }
    public long getRentalId() { return rentalId; }
    public LocalDate getInvoiceDate() { return invoiceDate; }
    public String getCustomerName() { return customerName; }
    public String getCustomerGstin() { return customerGstin; }
    public String getVendorBusinessName() { return vendorBusinessName; }
    public String getVendorGstin() { return vendorGstin; }
    public BigDecimal getTaxableRent() { return taxableRent; }
    public BigDecimal getCgst() { return cgst; }
    public BigDecimal getSgst() { return sgst; }
    public BigDecimal getIgst() { return igst; }
    public BigDecimal getTotalGst() { return totalGst; }
    public BigDecimal getTotalAmount() { return totalAmount; }
}
