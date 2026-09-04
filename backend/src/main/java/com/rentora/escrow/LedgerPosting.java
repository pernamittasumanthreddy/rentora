package com.rentora.escrow;

import java.math.BigDecimal;

public class LedgerPosting {
    private final String accountNumber;
    private final PostingType postingType;
    private final BigDecimal amount;
    private final String memo;

    public LedgerPosting(String accountNumber, PostingType postingType, BigDecimal amount, String memo) {
        this.accountNumber = accountNumber;
        this.postingType = postingType;
        this.amount = amount;
        this.memo = memo;
    }

    public String getAccountNumber() { return accountNumber; }
    public PostingType getPostingType() { return postingType; }
    public BigDecimal getAmount() { return amount; }
    public String getMemo() { return memo; }
}
