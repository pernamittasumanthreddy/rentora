"""
Rentora Real-Time Pricing Intelligence & Elasticity Optimizer
Calculates dynamic rental yields, competitor adjustments, and seasonal elasticity.
"""

from datetime import date, timedelta
from typing import Dict, List, Optional

class PricingOptimizer:
    def __init__(self):
        self.base_elasticity_curve = {
            "luxury_car": 0.85,
            "superbike": 0.90,
            "cinema_camera": 0.70,
            "drone": 0.75,
            "power_tool": 0.95
        }

    def compute_optimized_rate(
        self,
        base_rate: float,
        category: str,
        days: int,
        lead_time_days: int,
        fleet_utilization_pct: float
    ) -> Dict[str, float]:
        elasticity = self.base_elasticity_curve.get(category, 0.80)
        
        # Duration factor
        if days >= 30:
            duration_mult = 0.70  # 30% discount
        elif days >= 14:
            duration_mult = 0.80  # 20% discount
        elif days >= 7:
            duration_mult = 0.85  # 15% discount
        elif days >= 3:
            duration_mult = 0.95  # 5% discount
        else:
            duration_mult = 1.0

        # Demand pressure multiplier
        if fleet_utilization_pct >= 90.0:
            demand_mult = 1.25
        elif fleet_utilization_pct >= 75.0:
            demand_mult = 1.10
        elif fleet_utilization_pct <= 30.0:
            demand_mult = 0.90  # Stimulate low-demand periods
        else:
            demand_mult = 1.0

        # Last-minute booking surcharge
        lead_time_mult = 1.08 if lead_time_days <= 1 else 1.0

        daily_rate = round(base_rate * duration_mult * demand_mult * lead_time_mult, 2)
        total_rent = round(daily_rate * days, 2)

        return {
            "base_rate": base_rate,
            "optimized_daily_rate": daily_rate,
            "duration_multiplier": duration_mult,
            "demand_multiplier": demand_mult,
            "lead_time_multiplier": lead_time_mult,
            "total_rent": total_rent
        }
