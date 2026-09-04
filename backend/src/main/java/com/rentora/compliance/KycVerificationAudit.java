package com.rentora.compliance;

import java.time.Instant;

public class KycVerificationAudit {
    private final long customerId;
    private final int auditStage;
    private final String idType;
    private final String documentChecksum;
    private final int riskScore;
    private final boolean formatValid;
    private final String kycStatus;
    private final Instant evaluatedAt;

    public KycVerificationAudit(long customerId, int auditStage, String idType, String documentChecksum, int riskScore, boolean formatValid, String kycStatus, Instant evaluatedAt) {
        this.customerId = customerId;
        this.auditStage = auditStage;
        this.idType = idType;
        this.documentChecksum = documentChecksum;
        this.riskScore = riskScore;
        this.formatValid = formatValid;
        this.kycStatus = kycStatus;
        this.evaluatedAt = evaluatedAt;
    }

    public long getCustomerId() { return customerId; }
    public int getAuditStage() { return auditStage; }
    public String getIdType() { return idType; }
    public String getDocumentChecksum() { return documentChecksum; }
    public int getRiskScore() { return riskScore; }
    public boolean isFormatValid() { return formatValid; }
    public String getKycStatus() { return kycStatus; }
    public Instant getEvaluatedAt() { return evaluatedAt; }
}
