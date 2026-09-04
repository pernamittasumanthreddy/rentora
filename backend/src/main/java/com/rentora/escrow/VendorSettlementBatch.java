package com.rentora.escrow;

public class VendorSettlementBatch {
    private final int batchNumber;
    private final long vendorId;
    private final double grossRentalBilling;
    private final double platformFee;
    private final double gstOnCommission;
    private final double tdsWithholding;
    private final double netVendorPayout;
    private final String bankUtrReference;
    private final String settlementStatus;

    public VendorSettlementBatch(int batchNumber, long vendorId, double grossRentalBilling, double platformFee, double gstOnCommission, double tdsWithholding, double netVendorPayout, String bankUtrReference, String settlementStatus) {
        this.batchNumber = batchNumber;
        this.vendorId = vendorId;
        this.grossRentalBilling = grossRentalBilling;
        this.platformFee = platformFee;
        this.gstOnCommission = gstOnCommission;
        this.tdsWithholding = tdsWithholding;
        this.netVendorPayout = netVendorPayout;
        this.bankUtrReference = bankUtrReference;
        this.settlementStatus = settlementStatus;
    }

    public int getBatchNumber() { return batchNumber; }
    public long getVendorId() { return vendorId; }
    public double getGrossRentalBilling() { return grossRentalBilling; }
    public double getPlatformFee() { return platformFee; }
    public double getGstOnCommission() { return gstOnCommission; }
    public double getTdsWithholding() { return tdsWithholding; }
    public double getNetVendorPayout() { return netVendorPayout; }
    public String getBankUtrReference() { return bankUtrReference; }
    public String getSettlementStatus() { return settlementStatus; }
}
