"""
FastAPI / Python Entry Point for Telematics Microservice
"""

from telematics_stream_parser import TelematicsStreamParser
from geofence_spatial_engine import GeofenceSpatialEngine

class TelematicsEngineService:
    def __init__(self):
        self.parser = TelematicsStreamParser()
        self.geofence = GeofenceSpatialEngine()

    def get_service_status(self):
        return {
            "service": "rentora-telematics-engine",
            "status": "HEALTHY",
            "active_monitored_vin_count": len(self.parser.recent_breadcrumbs)
        }

if __name__ == "__main__":
    svc = TelematicsEngineService()
    print("Telematics Engine Service initialized:", svc.get_service_status())
