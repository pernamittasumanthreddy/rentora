package com.rentora.escrow;

import java.time.Instant;

public class EscrowAuditLogEntry {
    private final int auditSequence;
    private final long rentalId;
    private final double heldAmountInr;
    private final String hashVerification;
    private final String auditMemo;
    private final Instant timestamp;

    public EscrowAuditLogEntry(int auditSequence, long rentalId, double heldAmountInr, String hashVerification, String auditMemo, Instant timestamp) {
        this.auditSequence = auditSequence;
        this.rentalId = rentalId;
        this.heldAmountInr = heldAmountInr;
        this.hashVerification = hashVerification;
        this.auditMemo = auditMemo;
        this.timestamp = timestamp;
    }

    public int getAuditSequence() { return auditSequence; }
    public long getRentalId() { return rentalId; }
    public double getHeldAmountInr() { return heldAmountInr; }
    public String getHashVerification() { return hashVerification; }
    public String getAuditMemo() { return auditMemo; }
    public Instant getTimestamp() { return timestamp; }
}
