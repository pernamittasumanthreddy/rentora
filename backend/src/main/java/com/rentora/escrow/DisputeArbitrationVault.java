package com.rentora.escrow;

import java.math.BigDecimal;
import java.time.Instant;
import java.util.*;
import java.util.concurrent.ConcurrentHashMap;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class DisputeArbitrationVault {
    private static final Logger log = LoggerFactory.getLogger(DisputeArbitrationVault.class);
    private final Map<Long, DisputeCase> cases = new ConcurrentHashMap<>();

    public DisputeCase openDispute(long rentalId, long initiatedByUserId, String claimCategory, String statement, BigDecimal contestedAmount) {
        DisputeCase dispute = new DisputeCase(
            rentalId, initiatedByUserId, claimCategory, statement, contestedAmount, Instant.now()
        );
        cases.put(rentalId, dispute);
        log.warn("Opened Dispute Case for Rental #{}: [{}] Contested Amount: INR {}", rentalId, claimCategory, contestedAmount);
        return dispute;
    }

    public void assignMediator(long rentalId, String mediatorName) {
        DisputeCase dispute = cases.get(rentalId);
        if (dispute != null) {
            dispute.setAssignedMediator(mediatorName);
            dispute.setStatus("UNDER_ARBITRATION");
            log.info("Assigned mediator {} to Rental #{} dispute.", mediatorName, rentalId);
        }
    }

    public void resolveCase(long rentalId, String resolutionSummary, BigDecimal approvedCustomerRefund, BigDecimal approvedVendorAward) {
        DisputeCase dispute = cases.get(rentalId);
        if (dispute != null) {
            dispute.setResolution(resolutionSummary);
            dispute.setApprovedCustomerRefund(approvedCustomerRefund);
            dispute.setApprovedVendorAward(approvedVendorAward);
            dispute.setStatus("RESOLVED");
            dispute.setResolvedAt(Instant.now());
            log.info("Dispute resolved for Rental #{}. Customer Award: INR {}, Vendor Award: INR {}",
                rentalId, approvedCustomerRefund, approvedVendorAward);
        }
    }

    public Optional<DisputeCase> getDispute(long rentalId) {
        return Optional.ofNullable(cases.get(rentalId));
    }
}
