"""
Rentora Geofencing & Spatial Zone Compliance Engine
Monitors vehicle location against allowed operating boundaries (e.g. state border restrictions).
"""

import math
from typing import List, Tuple

class GeofencePolygon:
    def __init__(self, zone_id: str, name: str, vertices: List[Tuple[float, float]]):
        self.zone_id = zone_id
        self.name = name
        self.vertices = vertices

    def contains(self, lat: float, lon: float) -> bool:
        """Ray-casting algorithm to determine if (lat, lon) is inside polygon boundary."""
        n = len(self.vertices)
        inside = False
        p1x, p1y = self.vertices[0]
        for i in range(n + 1):
            p2x, p2y = self.vertices[i % n]
            if lat > min(p1x, p2x):
                if lat <= max(p1x, p2x):
                    if lon <= max(p1y, p2y):
                        if p1x != p2x:
                            xinters = (lat - p1x) * (p2y - p1y) / (p2x - p1x) + p1y
                        if p1y == p2y or lon <= xinters:
                            inside = not inside
            p1x, p1y = p2x, p2y
        return inside

class GeofenceSpatialEngine:
    def __init__(self):
        self.registered_zones: List[GeofencePolygon] = []
        self._init_default_zones()

    def _init_default_zones(self):
        # Default Karnataka State perimeter zone approx
        karnataka_bounds = [
            (11.5, 75.0), (15.5, 74.0), (18.5, 77.0), (16.0, 78.5), (12.0, 77.5)
        ]
        self.registered_zones.append(GeofencePolygon("KA-STATE", "Karnataka State Zone", karnataka_bounds))

    def check_position(self, lat: float, lon: float) -> Tuple[bool, str]:
        for zone in self.registered_zones:
            if zone.contains(lat, lon):
                return True, zone.name
        return False, "OUT_OF_BOUNDS"
