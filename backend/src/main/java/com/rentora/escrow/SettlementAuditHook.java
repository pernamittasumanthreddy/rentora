package com.rentora.escrow;

public interface SettlementAuditHook {
    void onSettlementEvent(EscrowDepositRecord record, String eventType);
}
