"""
Rentora Pricing API Entry point
"""

from pricing_optimizer import PricingOptimizer

if __name__ == "__main__":
    optimizer = PricingOptimizer()
    sample = optimizer.compute_optimized_rate(
        base_rate=3800.0, category="luxury_car", days=4, lead_time_days=2, fleet_utilization_pct=85.0
    )
    print("Sample Pricing Optimization Quote:", sample)
