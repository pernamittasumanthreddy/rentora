import pytest
from datetime import date, timedelta

class RentalCalculator:
    """Core domain calculator for rental pricing and escrow taxes."""
    GST_RATE = 0.18
    CGST_RATE = 0.09
    SGST_RATE = 0.09

    @staticmethod
    def calculate_duration(start_date: date, end_date: date) -> int:
        if end_date < start_date:
            raise ValueError("End date cannot be prior to start date")
        days = (end_date - start_date).days
        return max(1, days)

    @classmethod
    def calculate_cost(cls, price_per_day: float, deposit: float, days: int, discount_pct: float = 0.0):
        base_rent = price_per_day * days * (1.0 - discount_pct)
        cgst = base_rent * cls.CGST_RATE
        sgst = base_rent * cls.SGST_RATE
        tax_total = cgst + sgst
        total_payable = base_rent + tax_total + deposit
        return {
            "days": days,
            "base_rent": round(base_rent, 2),
            "cgst": round(cgst, 2),
            "sgst": round(sgst, 2),
            "tax_total": round(tax_total, 2),
            "deposit": round(deposit, 2),
            "total_payable": round(total_payable, 2),
        }

@pytest.mark.unit
def test_rental_duration_single_day():
    today = date.today()
    assert RentalCalculator.calculate_duration(today, today) == 1

@pytest.mark.unit
def test_rental_duration_multi_day():
    start = date(2026, 9, 10)
    end = date(2026, 9, 15)
    assert RentalCalculator.calculate_duration(start, end) == 5

@pytest.mark.unit
def test_rental_cost_breakdown():
    # Thar 4x4: ₹3,800/day, ₹10,000 deposit, 3 days
    res = RentalCalculator.calculate_cost(price_per_day=3800.0, deposit=10000.0, days=3)
    assert res["base_rent"] == 11400.0
    assert res["cgst"] == 1026.0
    assert res["sgst"] == 1026.0
    assert res["tax_total"] == 2052.0
    assert res["deposit"] == 10000.0
    assert res["total_payable"] == 23452.0

@pytest.mark.unit
def test_rental_invalid_dates():
    with pytest.raises(ValueError):
        RentalCalculator.calculate_duration(date(2026, 9, 20), date(2026, 9, 15))
