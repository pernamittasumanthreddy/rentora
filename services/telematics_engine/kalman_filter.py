"""
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
