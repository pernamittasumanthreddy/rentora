"""
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
