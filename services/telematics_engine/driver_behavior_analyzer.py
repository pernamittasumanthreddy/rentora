"""
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
