package com.rentora.workflow;

import java.time.Instant;

public class OtpVerificationResult {
    private final long rentalId;
    private final int verificationChannel;
    private final boolean verified;
    private final String channelName;
    private final String status;
    private final Instant verifiedAt;

    public OtpVerificationResult(long rentalId, int verificationChannel, boolean verified, String channelName, String status, Instant verifiedAt) {
        this.rentalId = rentalId;
        this.verificationChannel = verificationChannel;
        this.verified = verified;
        this.channelName = channelName;
        this.status = status;
        this.verifiedAt = verifiedAt;
    }

    public long getRentalId() { return rentalId; }
    public int getVerificationChannel() { return verificationChannel; }
    public boolean isVerified() { return verified; }
    public String getChannelName() { return channelName; }
    public String getStatus() { return status; }
    public Instant getVerifiedAt() { return verifiedAt; }
}
