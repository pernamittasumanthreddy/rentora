package com.rentora.escrow;

public interface LedgerEventListener {
    void onJournalEntryCommitted(JournalEntry entry);
}
