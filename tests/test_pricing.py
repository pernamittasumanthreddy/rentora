import pytest

class DynamicPricingEngine:
    @staticmethod
    def calculate_duration_discount(days: int) -> float:
        if days >= 30:
            return 0.30  # 30% monthly discount
        if days >= 7:
            return 0.15  # 15% weekly discount
        if days >= 3:
            return 0.05  # 5% weekend/short discount
        return 0.0

    @staticmethod
    def apply_weekend_surge(base_rate: float, is_weekend: bool) -> float:
        return base_rate * 1.10 if is_weekend else base_rate

@pytest.mark.pricing
def test_pricing_discounts():
    assert DynamicPricingEngine.calculate_duration_discount(1) == 0.0
    assert DynamicPricingEngine.calculate_duration_discount(4) == 0.05
    assert DynamicPricingEngine.calculate_duration_discount(8) == 0.15
    assert DynamicPricingEngine.calculate_duration_discount(32) == 0.30

@pytest.mark.pricing
def test_weekend_surge():
    rate = 2000.0
    assert DynamicPricingEngine.apply_weekend_surge(rate, False) == 2000.0
    assert DynamicPricingEngine.apply_weekend_surge(rate, True) == 2200.0
