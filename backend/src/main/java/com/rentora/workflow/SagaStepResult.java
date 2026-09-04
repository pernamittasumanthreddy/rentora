package com.rentora.workflow;

public class SagaStepResult {
    private final long rentalId;
    private final int phaseNumber;
    private final String correlationId;
    private final boolean success;
    private final String status;
    private final String memo;

    public SagaStepResult(long rentalId, int phaseNumber, String correlationId, boolean success, String status, String memo) {
        this.rentalId = rentalId;
        this.phaseNumber = phaseNumber;
        this.correlationId = correlationId;
        this.success = success;
        this.status = status;
        this.memo = memo;
    }

    public long getRentalId() { return rentalId; }
    public int getPhaseNumber() { return phaseNumber; }
    public String getCorrelationId() { return correlationId; }
    public boolean isSuccess() { return success; }
    public String getStatus() { return status; }
    public String getMemo() { return memo; }
}
