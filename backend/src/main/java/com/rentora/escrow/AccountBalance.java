package com.rentora.escrow;

import java.math.BigDecimal;

public class AccountBalance {
    private final String accountNumber;
    private final String accountName;
    private final AccountType accountType;
    private BigDecimal currentBalance = BigDecimal.ZERO;
    private long totalPostings = 0;

    public AccountBalance(String accountNumber, String accountName, AccountType accountType) {
        this.accountNumber = accountNumber;
        this.accountName = accountName;
        this.accountType = accountType;
    }

    public synchronized void applyPosting(LedgerPosting posting) {
        if (accountType == AccountType.ASSET || accountType == AccountType.EXPENSE) {
            if (posting.getPostingType() == PostingType.DEBIT) {
                this.currentBalance = this.currentBalance.add(posting.getAmount());
            } else {
                this.currentBalance = this.currentBalance.subtract(posting.getAmount());
            }
        } else {
            // LIABILITY, EQUITY, REVENUE
            if (posting.getPostingType() == PostingType.CREDIT) {
                this.currentBalance = this.currentBalance.add(posting.getAmount());
            } else {
                this.currentBalance = this.currentBalance.subtract(posting.getAmount());
            }
        }
        this.totalPostings++;
    }

    public String getAccountNumber() { return accountNumber; }
    public String getAccountName() { return accountName; }
    public AccountType getAccountType() { return accountType; }
    public BigDecimal getCurrentBalance() { return currentBalance; }
    public long getTotalPostings() { return totalPostings; }
}
