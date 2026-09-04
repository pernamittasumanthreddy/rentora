package com.rentora.escrow;

import java.math.BigDecimal;
import java.time.Instant;
import java.util.List;
import java.util.Map;

public class JournalEntry {
    private final long entryId;
    private final String referenceCode;
    private final String description;
    private final List<LedgerPosting> postings;
    private final BigDecimal totalAmount;
    private final String previousBlockHash;
    private final String blockHash;
    private final Instant timestamp;
    private final Map<String, String> metadata;

    public JournalEntry(
        long entryId,
        String referenceCode,
        String description,
        List<LedgerPosting> postings,
        BigDecimal totalAmount,
        String previousBlockHash,
        String blockHash,
        Instant timestamp,
        Map<String, String> metadata
    ) {
        this.entryId = entryId;
        this.referenceCode = referenceCode;
        this.description = description;
        this.postings = postings;
        this.totalAmount = totalAmount;
        this.previousBlockHash = previousBlockHash;
        this.blockHash = blockHash;
        this.timestamp = timestamp;
        this.metadata = metadata;
    }

    public long getEntryId() { return entryId; }
    public String getReferenceCode() { return referenceCode; }
    public String getDescription() { return description; }
    public List<LedgerPosting> getPostings() { return postings; }
    public BigDecimal getTotalAmount() { return totalAmount; }
    public String getPreviousBlockHash() { return previousBlockHash; }
    public String getBlockHash() { return blockHash; }
    public Instant getTimestamp() { return timestamp; }
    public Map<String, String> getMetadata() { return metadata; }
}
