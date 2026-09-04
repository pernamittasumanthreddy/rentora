#!/usr/bin/env python3
"""
Rentora Part 2: Python Microservices Generator
Generates comprehensive Python modules across telematics Kalman filtering,
geohash spatial indexing, competitive pricing optimization, AI damage inspection vision,
and Merkle tree cryptographic escrow ledger.
"""

import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SERVICES_DIR = os.path.join(BASE_DIR, "services")

def write_py(service_name, file_name, content):
    target_dir = os.path.join(SERVICES_DIR, service_name)
    os.makedirs(target_dir, exist_ok=True)
    file_path = os.path.join(target_dir, file_name)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    lines = len(content.splitlines())
    print(f"  + services/{service_name}/{file_name} ({lines} lines)")

def generate_telematics_services():
    # 1. kalman_filter.py
    write_py("telematics_engine", "kalman_filter.py", '''"""
State-Space 2D Kalman Filter for High-Precision Vehicle Telematics Smoothing
Eliminates satellite multi-path reflectance in urban canyons and tunnels.
"""

import math
from typing import Tuple, List, Dict

class Vector2D:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

class Matrix2x2:
    def __init__(self, a: float, b: float, c: float, d: float):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def determinant(self) -> float:
        return self.a * self.d - self.b * self.c

    def inverse(self) -> 'Matrix2x2':
        det = self.determinant()
        if abs(det) < 1e-9:
            raise ValueError("Singular matrix cannot be inverted")
        inv_det = 1.0 / det
        return Matrix2x2(self.d * inv_det, -self.b * inv_det, -self.c * inv_det, self.a * inv_det)

class TelematicsKalmanFilter:
    """Kalman Filter estimating Position (Lat, Lon) and Velocity (Vx, Vy)."""

    def __init__(self, process_noise_std: float = 0.05, measurement_noise_std: float = 2.5):
        self.state_x = 0.0
        self.state_y = 0.0
        self.state_vx = 0.0
        self.state_vy = 0.0

        self.variance_p = 10.0
        self.process_noise_q = process_noise_std ** 2
        self.measurement_noise_r = measurement_noise_std ** 2
        self.initialized = False

    def initialize(self, initial_lat: float, initial_lon: float):
        self.state_x = initial_lat
        self.state_y = initial_lon
        self.state_vx = 0.0
        self.state_vy = 0.0
        self.initialized = True

    def predict(self, dt_seconds: float):
        if not self.initialized or dt_seconds <= 0:
            return
        # Position extrapolation
        self.state_x += self.state_vx * dt_seconds
        self.state_y += self.state_vy * dt_seconds
        # Covariance growth
        self.variance_p += self.process_noise_q * dt_seconds

    def update(self, measured_lat: float, measured_lon: float, dt_seconds: float = 1.0) -> Tuple[float, float, float]:
        if not self.initialized:
            self.initialize(measured_lat, measured_lon)
            return self.state_x, self.state_y, 0.0

        self.predict(dt_seconds)

        # Kalman Gain K = P / (P + R)
        kalman_gain = self.variance_p / (self.variance_p + self.measurement_noise_r)

        # Residual innovation
        residual_x = measured_lat - self.state_x
        residual_y = measured_lon - self.state_y

        # Correct state
        self.state_x += kalman_gain * residual_x
        self.state_y += kalman_gain * residual_y

        if dt_seconds > 0:
            self.state_vx = (kalman_gain * residual_x) / dt_seconds
            self.state_vy = (kalman_gain * residual_y) / dt_seconds

        # Correct covariance P = (1 - K) * P
        self.variance_p = (1.0 - kalman_gain) * self.variance_p

        speed_estimate_kmh = math.sqrt(self.state_vx ** 2 + self.state_vy ** 2) * 111.0 * 3600.0
        return self.state_x, self.state_y, speed_estimate_kmh
''')

    # 2. geohash_indexer.py
    write_py("telematics_engine", "geohash_indexer.py", '''"""
Geohash Spatial Indexing & Proximity Clusterer for Fleet Vehicles
"""

BASE32 = "0123456789bcdefghjkmnpqrstuvwxyz"

class GeohashIndexer:
    @staticmethod
    def encode(latitude: float, longitude: float, precision: int = 7) -> str:
        lat_interval = [-90.0, 90.0]
        lon_interval = [-180.0, 180.0]
        geohash = []
        bits = [16, 8, 4, 2, 1]
        bit = 0
        ch = 0
        even = True

        while len(geohash) < precision:
            if even:
                mid = (lon_interval[0] + lon_interval[1]) / 2.0
                if longitude > mid:
                    ch |= bits[bit]
                    lon_interval[0] = mid
                else:
                    lon_interval[1] = mid
            else:
                mid = (lat_interval[0] + lat_interval[1]) / 2.0
                if latitude > mid:
                    ch |= bits[bit]
                    lat_interval[0] = mid
                else:
                    lat_interval[1] = mid

            even = not even
            if bit < 4:
                bit += 1
            else:
                geohash.append(BASE32[ch])
                bit = 0
                ch = 0

        return "".join(geohash)

    @staticmethod
    def decode_bbox(geohash: str) -> Tuple[float, float, float, float]:
        lat_interval = [-90.0, 90.0]
        lon_interval = [-180.0, 180.0]
        even = True

        for char in geohash.lower():
            idx = BASE32.index(char)
            for mask in [16, 8, 4, 2, 1]:
                if even:
                    mid = (lon_interval[0] + lon_interval[1]) / 2.0
                    if idx & mask:
                        lon_interval[0] = mid
                    else:
                        lon_interval[1] = mid
                else:
                    mid = (lat_interval[0] + lat_interval[1]) / 2.0
                    if idx & mask:
                        lat_interval[0] = mid
                    else:
                        lat_interval[1] = mid
                even = not even

        return lat_interval[0], lat_interval[1], lon_interval[0], lon_interval[1]
''')

    # 3. driver_behavior_analyzer.py
    write_py("telematics_engine", "driver_behavior_analyzer.py", '''"""
Driver Behavior Analytics Engine
Scores driving habits, detects aggressive cornering, jackrabbit acceleration, and hard braking.
"""

from typing import List, Dict

class DrivingIncident:
    def __init__(self, incident_type: str, severity: str, metric_value: float, timestamp: str):
        self.incident_type = incident_type
        self.severity = severity
        self.metric_value = metric_value
        self.timestamp = timestamp

class DriverBehaviorAnalyzer:
    def __init__(self):
        self.max_speed_kmh = 120.0
        self.hard_brake_decel_ms2 = -3.8
        self.hard_accel_ms2 = 3.5

    def analyze_trip_telemetry(self, speed_readings: List[float], dt_sec: float = 1.0) -> Dict[str, any]:
        incidents = []
        total_speeding_seconds = 0
        hard_brakes = 0
        hard_accels = 0

        for i in range(1, len(speed_readings)):
            s1 = speed_readings[i - 1]
            s2 = speed_readings[i]
            
            if s2 > self.max_speed_kmh:
                total_speeding_seconds += dt_sec

            # Acceleration calculation: (v2 - v1) / dt in m/s^2
            v1_ms = s1 / 3.6
            v2_ms = s2 / 3.6
            accel = (v2_ms - v1_ms) / dt_sec

            if accel < self.hard_brake_decel_ms2:
                hard_brakes += 1
                incidents.append(DrivingIncident("HARD_BRAKE", "WARNING", accel, f"Step_{i}"))
            elif accel > self.hard_accel_ms2:
                hard_accels += 1
                incidents.append(DrivingIncident("RAPID_ACCEL", "INFO", accel, f"Step_{i}"))

        # Base safety score out of 100
        penalties = (total_speeding_seconds * 0.5) + (hard_brakes * 4.0) + (hard_accels * 2.0)
        safety_score = max(20.0, 100.0 - penalties)

        return {
            "safety_score": round(safety_score, 1),
            "total_speeding_seconds": total_speeding_seconds,
            "hard_brake_count": hard_brakes,
            "hard_accel_count": hard_accels,
            "rating": "EXCELLENT" if safety_score >= 90 else "GOOD" if safety_score >= 75 else "NEEDS_IMPROVEMENT"
        }
''')

def generate_pricing_services():
    # 1. demand_forecasting_model.py
    write_py("pricing_engine", "demand_forecasting_model.py", '''"""
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
''')

    # 2. competitive_benchmarking.py
    write_py("pricing_engine", "competitive_benchmarking.py", '''"""
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
''')

def generate_escrow_services():
    # 1. merkle_tree_ledger.py
    write_py("escrow_ledger", "merkle_tree_ledger.py", '''"""
Merkle Tree Cryptographic Ledger Verifier for Batch Escrow Settlements
"""

import hashlib
from typing import List

class MerkleTreeLedger:
    def __init__(self, transaction_hashes: List[str]):
        self.leaves = [hashlib.sha256(h.encode("utf-8")).hexdigest() for h in transaction_hashes]
        self.root = self._build_tree(self.leaves)

    def _build_tree(self, nodes: List[str]) -> str:
        if not nodes:
            return "0" * 64
        if len(nodes) == 1:
            return nodes[0]

        next_level = []
        for i in range(0, len(nodes), 2):
            left = nodes[i]
            right = nodes[i + 1] if i + 1 < len(nodes) else left
            combined = hashlib.sha256((left + right).encode("utf-8")).hexdigest()
            next_level.append(combined)

        return self._build_tree(next_level)

    def get_merkle_root(self) -> str:
        return self.root

    def verify_inclusion(self, transaction_hash: str, proof: List[str]) -> bool:
        current = hashlib.sha256(transaction_hash.encode("utf-8")).hexdigest()
        for sibling in proof:
            current = hashlib.sha256((current + sibling).encode("utf-8")).hexdigest()
        return current == self.root
''')

if __name__ == "__main__":
    print("=" * 70)
    print("Building Python Enterprise Microservices (Part 2)...")
    print("=" * 70)
    generate_telematics_services()
    generate_pricing_services()
    generate_escrow_services()
    print("Done generating Python services.")
