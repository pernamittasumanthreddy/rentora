"""
Competitive Market Rate Benchmark Aggregator
"""

from typing import Dict, List

class CompetitiveBenchmarkEngine:
    def __init__(self):
        self.market_aggregates = {
            "mahindra_thar_4x4": {"avg_market_inr": 4200.0, "p25_inr": 3600.0, "p75_inr": 4800.0},
            "bmw_330i_msport": {"avg_market_inr": 8200.0, "p25_inr": 7200.0, "p75_inr": 9500.0},
            "royal_enfield_himalayan_450": {"avg_market_inr": 1600.0, "p25_inr": 1300.0, "p75_inr": 1900.0},
            "kawasaki_ninja_zx6r": {"avg_market_inr": 3600.0, "p25_inr": 3000.0, "p75_inr": 4200.0},
            "sony_fx3": {"avg_market_inr": 3200.0, "p25_inr": 2700.0, "p75_inr": 3600.0},
            "dji_mavic_3_pro": {"avg_market_inr": 3900.0, "p25_inr": 3400.0, "p75_inr": 4400.0}
        }

    def evaluate_pricing_competitiveness(self, slug: str, our_rate_inr: float) -> Dict[str, any]:
        benchmark = self.market_aggregates.get(slug)
        if not benchmark:
            return {"status": "NO_BENCHMARK_DATA", "recommendation": "MAINTAIN_CURRENT"}

        market_avg = benchmark["avg_market_inr"]
        discount_vs_market_pct = round(((market_avg - our_rate_inr) / market_avg) * 100.0, 1)

        if our_rate_inr < benchmark["p25_inr"]:
            recommendation = "VALUE_LEADER_CONSIDER_PRICE_INCREASE"
        elif our_rate_inr > benchmark["p75_inr"]:
            recommendation = "PREMIUM_RATE_CONSIDER_PROMOTIONAL_DISCOUNT"
        else:
            recommendation = "OPTIMAL_MARKET_COMPETITIVE"

        return {
            "slug": slug,
            "our_rate": our_rate_inr,
            "market_avg": market_avg,
            "discount_vs_market_pct": discount_vs_market_pct,
            "recommendation": recommendation
        }
