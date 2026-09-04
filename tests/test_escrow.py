import pytest

class EscrowLedger:
    def __init__(self):
        self.ledger = {}

    def lock_deposit(self, rental_id: int, customer_id: int, amount: float):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.ledger[rental_id] = {
            "customer_id": customer_id,
            "held_amount": amount,
            "status": "HELD_IN_ESCROW",
            "refunded_amount": 0.0,
            "damage_deduction": 0.0,
        }
        return self.ledger[rental_id]

    def settle_return(self, rental_id: int, damage_fee: float = 0.0):
        if rental_id not in self.ledger:
            raise KeyError(f"Rental {rental_id} not found in escrow ledger")
        entry = self.ledger[rental_id]
        if damage_fee > entry["held_amount"]:
            raise ValueError("Damage deduction cannot exceed held deposit")
        
        refund = entry["held_amount"] - damage_fee
        entry["damage_deduction"] = damage_fee
        entry["refunded_amount"] = refund
        entry["status"] = "SETTLED_REFUNDED" if damage_fee == 0 else "SETTLED_WITH_DEDUCTION"
        return entry

@pytest.mark.escrow
def test_escrow_deposit_lock():
    ledger = EscrowLedger()
    record = ledger.lock_deposit(rental_id=1001, customer_id=42, amount=12000.0)
    assert record["status"] == "HELD_IN_ESCROW"
    assert record["held_amount"] == 12000.0

@pytest.mark.escrow
def test_escrow_clean_return_100_percent_refund():
    ledger = EscrowLedger()
    ledger.lock_deposit(rental_id=1002, customer_id=42, amount=10000.0)
    settled = ledger.settle_return(rental_id=1002, damage_fee=0.0)
    assert settled["status"] == "SETTLED_REFUNDED"
    assert settled["refunded_amount"] == 10000.0
    assert settled["damage_deduction"] == 0.0

@pytest.mark.escrow
def test_escrow_damaged_return_deduction():
    ledger = EscrowLedger()
    ledger.lock_deposit(rental_id=1003, customer_id=42, amount=15000.0)
    settled = ledger.settle_return(rental_id=1003, damage_fee=2500.0)
    assert settled["status"] == "SETTLED_WITH_DEDUCTION"
    assert settled["refunded_amount"] == 12500.0
    assert settled["damage_deduction"] == 2500.0
