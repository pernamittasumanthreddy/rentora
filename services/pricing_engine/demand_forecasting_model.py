"""
Time-Series Demand Forecasting Engine for Fleet & Equipment Bookings
"""

from typing import List, Dict
import math

class DemandForecastingModel:
    """Holt-Winters double exponential smoothing for seasonal rental demand."""

    def __init__(self, alpha: float = 0.3, beta: float = 0.1):
        self.alpha = alpha
        self.beta = beta

    def forecast_next_periods(self, historical_series: List[float], periods_ahead: int = 7) -> List[float]:
        if not historical_series:
            return [10.0] * periods_ahead

        level = historical_series[0]
        trend = (historical_series[-1] - historical_series[0]) / max(1, len(historical_series) - 1)

        for value in historical_series:
            last_level = level
            level = self.alpha * value + (1.0 - self.alpha) * (level + trend)
            trend = self.beta * (level - last_level) + (1.0 - self.beta) * trend

        forecasts = []
        for h in range(1, periods_ahead + 1):
            forecast = level + h * trend
            forecasts.append(max(0.0, round(forecast, 2)))

        return forecasts
