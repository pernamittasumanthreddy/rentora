"""
Rentora High-Frequency Telematics Data Stream Parser
Processes binary/JSON CAN bus telemetry packets from OBD-II vehicle transponders.
"""

import json
import math
import logging
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Dict, List, Optional, Tuple

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] [TelematicsStream] %(message)s")
logger = logging.getLogger("telematics-stream")

@dataclass
class TelematicsPacket:
    vin: str
    latitude: float
    longitude: float
    speed_kmh: float
    heading_deg: float
    odometer_km: float
    fuel_level_pct: float
    engine_temp_c: float
    engine_rpm: float
    battery_v: float
    ignition_on: bool
    timestamp: datetime = field(default_factory=lambda: datetime.now(timezone.utc))

class TelematicsStreamParser:
    """Decodes live vehicle telemetry streams and performs anomaly threshold detection."""

    def __init__(self, max_speed_kmh: float = 120.0, severe_temp_c: float = 105.0):
        self.max_speed_kmh = max_speed_kmh
        self.severe_temp_c = severe_temp_c
        self.recent_breadcrumbs: Dict[str, List[Tuple[float, float, datetime]]] = {}

    def parse_raw_payload(self, raw_data: bytes) -> Optional[TelematicsPacket]:
        try:
            payload = json.loads(raw_data.decode("utf-8"))
            packet = TelematicsPacket(
                vin=payload["vin"],
                latitude=float(payload["lat"]),
                longitude=float(payload["lon"]),
                speed_kmh=float(payload["speed"]),
                heading_deg=float(payload.get("heading", 0.0)),
                odometer_km=float(payload.get("odometer", 0.0)),
                fuel_level_pct=float(payload.get("fuel", 100.0)),
                engine_temp_c=float(payload.get("temp", 90.0)),
                engine_rpm=float(payload.get("rpm", 1500.0)),
                battery_v=float(payload.get("battery", 13.6)),
                ignition_on=bool(payload.get("ignition", True)),
                timestamp=datetime.fromisoformat(payload["time"]) if "time" in payload else datetime.now(timezone.utc)
            )
            self._record_breadcrumb(packet)
            return packet
        except Exception as ex:
            logger.error(f"Failed to parse incoming telematics payload: {ex}")
            return None

    def _record_breadcrumb(self, packet: TelematicsPacket):
        if packet.vin not in self.recent_breadcrumbs:
            self.recent_breadcrumbs[packet.vin] = []
        history = self.recent_breadcrumbs[packet.vin]
        history.append((packet.latitude, packet.longitude, packet.timestamp))
        if len(history) > 1000:
            history.pop(0)

    def detect_violations(self, packet: TelematicsPacket) -> List[Dict[str, any]]:
        violations = []
        if packet.speed_kmh > self.max_speed_kmh:
            violations.append({
                "type": "SPEED_LIMIT_BREACH",
                "severity": "CRITICAL" if packet.speed_kmh > 140 else "WARNING",
                "message": f"Vehicle exceeding max speed: {packet.speed_kmh:.1f} km/h (Limit: {self.max_speed_kmh:.1f})"
            })
        if packet.engine_temp_c > self.severe_temp_c:
            violations.append({
                "type": "ENGINE_OVERHEAT",
                "severity": "HIGH",
                "message": f"Engine coolant temperature high: {packet.engine_temp_c:.1f} C"
            })
        if packet.battery_v < 11.5:
            violations.append({
                "type": "LOW_BATTERY",
                "severity": "WARNING",
                "message": f"12V battery discharged: {packet.battery_v:.2f} V"
            })
        return violations

    def compute_travel_distance_km(self, vin: str) -> float:
        points = self.recent_breadcrumbs.get(vin, [])
        if len(points) < 2:
            return 0.0
        total_km = 0.0
        for i in range(1, len(points)):
            lat1, lon1, _ = points[i - 1]
            lat2, lon2, _ = points[i]
            total_km += self._haversine(lat1, lon1, lat2, lon2)
        return round(total_km, 2)

    @staticmethod
    def _haversine(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
        r = 6371.0  # Earth radius km
        d_lat = math.radians(lat2 - lat1)
        d_lon = math.radians(lon2 - lon1)
        a = math.sin(d_lat / 2.0) ** 2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(d_lon / 2.0) ** 2
        c = 2.0 * math.atan2(math.sqrt(a), math.sqrt(1.0 - a))
        return r * c
