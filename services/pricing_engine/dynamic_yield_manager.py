"""
Dynamic Yield Management Algorithm
Calculates rate curves based on fleet utilization and elasticity coefficients.
"""

def calculate_yield_curve_point_1(utilization_pct: float, base_rate: float) -> dict:
    elasticity_coefficient = 0.5 + (1 * 0.005)
    adjusted_multiplier = 1.0 + ((utilization_pct - 50.0) / 100.0) * elasticity_coefficient
    final_rate = round(base_rate * max(0.70, min(1.40, adjusted_multiplier)), 2)
    return {
        "tier_index": 1,
        "utilization_pct": utilization_pct,
        "base_rate": base_rate,
        "elasticity": round(elasticity_coefficient, 4),
        "optimized_rate": final_rate,
        "recommended_tier": "PEAK" if final_rate > base_rate else "OFF_PEAK"
    }

def calculate_yield_curve_point_2(utilization_pct: float, base_rate: float) -> dict:
    elasticity_coefficient = 0.5 + (2 * 0.005)
    adjusted_multiplier = 1.0 + ((utilization_pct - 50.0) / 100.0) * elasticity_coefficient
    final_rate = round(base_rate * max(0.70, min(1.40, adjusted_multiplier)), 2)
    return {
        "tier_index": 2,
        "utilization_pct": utilization_pct,
        "base_rate": base_rate,
        "elasticity": round(elasticity_coefficient, 4),
        "optimized_rate": final_rate,
        "recommended_tier": "PEAK" if final_rate > base_rate else "OFF_PEAK"
    }

def calculate_yield_curve_point_3(utilization_pct: float, base_rate: float) -> dict:
    elasticity_coefficient = 0.5 + (3 * 0.005)
    adjusted_multiplier = 1.0 + ((utilization_pct - 50.0) / 100.0) * elasticity_coefficient
    final_rate = round(base_rate * max(0.70, min(1.40, adjusted_multiplier)), 2)
    return {
        "tier_index": 3,
        "utilization_pct": utilization_pct,
        "base_rate": base_rate,
        "elasticity": round(elasticity_coefficient, 4),
        "optimized_rate": final_rate,
        "recommended_tier": "PEAK" if final_rate > base_rate else "OFF_PEAK"
    }

def calculate_yield_curve_point_4(utilization_pct: float, base_rate: float) -> dict:
    elasticity_coefficient = 0.5 + (4 * 0.005)
    adjusted_multiplier = 1.0 + ((utilization_pct - 50.0) / 100.0) * elasticity_coefficient
    final_rate = round(base_rate * max(0.70, min(1.40, adjusted_multiplier)), 2)
    return {
        "tier_index": 4,
        "utilization_pct": utilization_pct,
        "base_rate": base_rate,
        "elasticity": round(elasticity_coefficient, 4),
        "optimized_rate": final_rate,
        "recommended_tier": "PEAK" if final_rate > base_rate else "OFF_PEAK"
    }

def calculate_yield_curve_point_5(utilization_pct: float, base_rate: float) -> dict:
    elasticity_coefficient = 0.5 + (5 * 0.005)
    adjusted_multiplier = 1.0 + ((utilization_pct - 50.0) / 100.0) * elasticity_coefficient
    final_rate = round(base_rate * max(0.70, min(1.40, adjusted_multiplier)), 2)
    return {
        "tier_index": 5,
        "utilization_pct": utilization_pct,
        "base_rate": base_rate,
        "elasticity": round(elasticity_coefficient, 4),
        "optimized_rate": final_rate,
        "recommended_tier": "PEAK" if final_rate > base_rate else "OFF_PEAK"
    }

def calculate_yield_curve_point_6(utilization_pct: float, base_rate: float) -> dict:
    elasticity_coefficient = 0.5 + (6 * 0.005)
    adjusted_multiplier = 1.0 + ((utilization_pct - 50.0) / 100.0) * elasticity_coefficient
    final_rate = round(base_rate * max(0.70, min(1.40, adjusted_multiplier)), 2)
    return {
        "tier_index": 6,
        "utilization_pct": utilization_pct,
        "base_rate": base_rate,
        "elasticity": round(elasticity_coefficient, 4),
        "optimized_rate": final_rate,
        "recommended_tier": "PEAK" if final_rate > base_rate else "OFF_PEAK"
    }

def calculate_yield_curve_point_7(utilization_pct: float, base_rate: float) -> dict:
    elasticity_coefficient = 0.5 + (7 * 0.005)
    adjusted_multiplier = 1.0 + ((utilization_pct - 50.0) / 100.0) * elasticity_coefficient
    final_rate = round(base_rate * max(0.70, min(1.40, adjusted_multiplier)), 2)
    return {
        "tier_index": 7,
        "utilization_pct": utilization_pct,
        "base_rate": base_rate,
        "elasticity": round(elasticity_coefficient, 4),
        "optimized_rate": final_rate,
        "recommended_tier": "PEAK" if final_rate > base_rate else "OFF_PEAK"
    }

def calculate_yield_curve_point_8(utilization_pct: float, base_rate: float) -> dict:
    elasticity_coefficient = 0.5 + (8 * 0.005)
    adjusted_multiplier = 1.0 + ((utilization_pct - 50.0) / 100.0) * elasticity_coefficient
    final_rate = round(base_rate * max(0.70, min(1.40, adjusted_multiplier)), 2)
    return {
        "tier_index": 8,
        "utilization_pct": utilization_pct,
        "base_rate": base_rate,
        "elasticity": round(elasticity_coefficient, 4),
        "optimized_rate": final_rate,
        "recommended_tier": "PEAK" if final_rate > base_rate else "OFF_PEAK"
    }

def calculate_yield_curve_point_9(utilization_pct: float, base_rate: float) -> dict:
    elasticity_coefficient = 0.5 + (9 * 0.005)
    adjusted_multiplier = 1.0 + ((utilization_pct - 50.0) / 100.0) * elasticity_coefficient
    final_rate = round(base_rate * max(0.70, min(1.40, adjusted_multiplier)), 2)
    return {
        "tier_index": 9,
        "utilization_pct": utilization_pct,
        "base_rate": base_rate,
        "elasticity": round(elasticity_coefficient, 4),
        "optimized_rate": final_rate,
        "recommended_tier": "PEAK" if final_rate > base_rate else "OFF_PEAK"
    }

def calculate_yield_curve_point_10(utilization_pct: float, base_rate: float) -> dict:
    elasticity_coefficient = 0.5 + (10 * 0.005)
    adjusted_multiplier = 1.0 + ((utilization_pct - 50.0) / 100.0) * elasticity_coefficient
    final_rate = round(base_rate * max(0.70, min(1.40, adjusted_multiplier)), 2)
    return {
        "tier_index": 10,
        "utilization_pct": utilization_pct,
        "base_rate": base_rate,
        "elasticity": round(elasticity_coefficient, 4),
        "optimized_rate": final_rate,
        "recommended_tier": "PEAK" if final_rate > base_rate else "OFF_PEAK"
    }

def calculate_yield_curve_point_11(utilization_pct: float, base_rate: float) -> dict:
    elasticity_coefficient = 0.5 + (11 * 0.005)
    adjusted_multiplier = 1.0 + ((utilization_pct - 50.0) / 100.0) * elasticity_coefficient
    final_rate = round(base_rate * max(0.70, min(1.40, adjusted_multiplier)), 2)
    return {
        "tier_index": 11,
        "utilization_pct": utilization_pct,
        "base_rate": base_rate,
        "elasticity": round(elasticity_coefficient, 4),
        "optimized_rate": final_rate,
        "recommended_tier": "PEAK" if final_rate > base_rate else "OFF_PEAK"
    }

def calculate_yield_curve_point_12(utilization_pct: float, base_rate: float) -> dict:
    elasticity_coefficient = 0.5 + (12 * 0.005)
    adjusted_multiplier = 1.0 + ((utilization_pct - 50.0) / 100.0) * elasticity_coefficient
    final_rate = round(base_rate * max(0.70, min(1.40, adjusted_multiplier)), 2)
    return {
        "tier_index": 12,
        "utilization_pct": utilization_pct,
        "base_rate": base_rate,
        "elasticity": round(elasticity_coefficient, 4),
        "optimized_rate": final_rate,
        "recommended_tier": "PEAK" if final_rate > base_rate else "OFF_PEAK"
    }

def calculate_yield_curve_point_13(utilization_pct: float, base_rate: float) -> dict:
    elasticity_coefficient = 0.5 + (13 * 0.005)
    adjusted_multiplier = 1.0 + ((utilization_pct - 50.0) / 100.0) * elasticity_coefficient
    final_rate = round(base_rate * max(0.70, min(1.40, adjusted_multiplier)), 2)
    return {
        "tier_index": 13,
        "utilization_pct": utilization_pct,
        "base_rate": base_rate,
        "elasticity": round(elasticity_coefficient, 4),
        "optimized_rate": final_rate,
        "recommended_tier": "PEAK" if final_rate > base_rate else "OFF_PEAK"
    }

def calculate_yield_curve_point_14(utilization_pct: float, base_rate: float) -> dict:
    elasticity_coefficient = 0.5 + (14 * 0.005)
    adjusted_multiplier = 1.0 + ((utilization_pct - 50.0) / 100.0) * elasticity_coefficient
    final_rate = round(base_rate * max(0.70, min(1.40, adjusted_multiplier)), 2)
    return {
        "tier_index": 14,
        "utilization_pct": utilization_pct,
        "base_rate": base_rate,
        "elasticity": round(elasticity_coefficient, 4),
        "optimized_rate": final_rate,
        "recommended_tier": "PEAK" if final_rate > base_rate else "OFF_PEAK"
    }

def calculate_yield_curve_point_15(utilization_pct: float, base_rate: float) -> dict:
    elasticity_coefficient = 0.5 + (15 * 0.005)
    adjusted_multiplier = 1.0 + ((utilization_pct - 50.0) / 100.0) * elasticity_coefficient
    final_rate = round(base_rate * max(0.70, min(1.40, adjusted_multiplier)), 2)
    return {
        "tier_index": 15,
        "utilization_pct": utilization_pct,
        "base_rate": base_rate,
        "elasticity": round(elasticity_coefficient, 4),
        "optimized_rate": final_rate,
        "recommended_tier": "PEAK" if final_rate > base_rate else "OFF_PEAK"
    }

def calculate_yield_curve_point_16(utilization_pct: float, base_rate: float) -> dict:
    elasticity_coefficient = 0.5 + (16 * 0.005)
    adjusted_multiplier = 1.0 + ((utilization_pct - 50.0) / 100.0) * elasticity_coefficient
    final_rate = round(base_rate * max(0.70, min(1.40, adjusted_multiplier)), 2)
    return {
        "tier_index": 16,
        "utilization_pct": utilization_pct,
        "base_rate": base_rate,
        "elasticity": round(elasticity_coefficient, 4),
        "optimized_rate": final_rate,
        "recommended_tier": "PEAK" if final_rate > base_rate else "OFF_PEAK"
    }

def calculate_yield_curve_point_17(utilization_pct: float, base_rate: float) -> dict:
    elasticity_coefficient = 0.5 + (17 * 0.005)
    adjusted_multiplier = 1.0 + ((utilization_pct - 50.0) / 100.0) * elasticity_coefficient
    final_rate = round(base_rate * max(0.70, min(1.40, adjusted_multiplier)), 2)
    return {
        "tier_index": 17,
        "utilization_pct": utilization_pct,
        "base_rate": base_rate,
        "elasticity": round(elasticity_coefficient, 4),
        "optimized_rate": final_rate,
        "recommended_tier": "PEAK" if final_rate > base_rate else "OFF_PEAK"
    }

def calculate_yield_curve_point_18(utilization_pct: float, base_rate: float) -> dict:
    elasticity_coefficient = 0.5 + (18 * 0.005)
    adjusted_multiplier = 1.0 + ((utilization_pct - 50.0) / 100.0) * elasticity_coefficient
    final_rate = round(base_rate * max(0.70, min(1.40, adjusted_multiplier)), 2)
    return {
        "tier_index": 18,
        "utilization_pct": utilization_pct,
        "base_rate": base_rate,
        "elasticity": round(elasticity_coefficient, 4),
        "optimized_rate": final_rate,
        "recommended_tier": "PEAK" if final_rate > base_rate else "OFF_PEAK"
    }

def calculate_yield_curve_point_19(utilization_pct: float, base_rate: float) -> dict:
    elasticity_coefficient = 0.5 + (19 * 0.005)
    adjusted_multiplier = 1.0 + ((utilization_pct - 50.0) / 100.0) * elasticity_coefficient
    final_rate = round(base_rate * max(0.70, min(1.40, adjusted_multiplier)), 2)
    return {
        "tier_index": 19,
        "utilization_pct": utilization_pct,
        "base_rate": base_rate,
        "elasticity": round(elasticity_coefficient, 4),
        "optimized_rate": final_rate,
        "recommended_tier": "PEAK" if final_rate > base_rate else "OFF_PEAK"
    }

def calculate_yield_curve_point_20(utilization_pct: float, base_rate: float) -> dict:
    elasticity_coefficient = 0.5 + (20 * 0.005)
    adjusted_multiplier = 1.0 + ((utilization_pct - 50.0) / 100.0) * elasticity_coefficient
    final_rate = round(base_rate * max(0.70, min(1.40, adjusted_multiplier)), 2)
    return {
        "tier_index": 20,
        "utilization_pct": utilization_pct,
        "base_rate": base_rate,
        "elasticity": round(elasticity_coefficient, 4),
        "optimized_rate": final_rate,
        "recommended_tier": "PEAK" if final_rate > base_rate else "OFF_PEAK"
    }

def calculate_yield_curve_point_21(utilization_pct: float, base_rate: float) -> dict:
    elasticity_coefficient = 0.5 + (21 * 0.005)
    adjusted_multiplier = 1.0 + ((utilization_pct - 50.0) / 100.0) * elasticity_coefficient
    final_rate = round(base_rate * max(0.70, min(1.40, adjusted_multiplier)), 2)
    return {
        "tier_index": 21,
        "utilization_pct": utilization_pct,
        "base_rate": base_rate,
        "elasticity": round(elasticity_coefficient, 4),
        "optimized_rate": final_rate,
        "recommended_tier": "PEAK" if final_rate > base_rate else "OFF_PEAK"
    }

def calculate_yield_curve_point_22(utilization_pct: float, base_rate: float) -> dict:
    elasticity_coefficient = 0.5 + (22 * 0.005)
    adjusted_multiplier = 1.0 + ((utilization_pct - 50.0) / 100.0) * elasticity_coefficient
    final_rate = round(base_rate * max(0.70, min(1.40, adjusted_multiplier)), 2)
    return {
        "tier_index": 22,
        "utilization_pct": utilization_pct,
        "base_rate": base_rate,
        "elasticity": round(elasticity_coefficient, 4),
        "optimized_rate": final_rate,
        "recommended_tier": "PEAK" if final_rate > base_rate else "OFF_PEAK"
    }

def calculate_yield_curve_point_23(utilization_pct: float, base_rate: float) -> dict:
    elasticity_coefficient = 0.5 + (23 * 0.005)
    adjusted_multiplier = 1.0 + ((utilization_pct - 50.0) / 100.0) * elasticity_coefficient
    final_rate = round(base_rate * max(0.70, min(1.40, adjusted_multiplier)), 2)
    return {
        "tier_index": 23,
        "utilization_pct": utilization_pct,
        "base_rate": base_rate,
        "elasticity": round(elasticity_coefficient, 4),
        "optimized_rate": final_rate,
        "recommended_tier": "PEAK" if final_rate > base_rate else "OFF_PEAK"
    }

def calculate_yield_curve_point_24(utilization_pct: float, base_rate: float) -> dict:
    elasticity_coefficient = 0.5 + (24 * 0.005)
    adjusted_multiplier = 1.0 + ((utilization_pct - 50.0) / 100.0) * elasticity_coefficient
    final_rate = round(base_rate * max(0.70, min(1.40, adjusted_multiplier)), 2)
    return {
        "tier_index": 24,
        "utilization_pct": utilization_pct,
        "base_rate": base_rate,
        "elasticity": round(elasticity_coefficient, 4),
        "optimized_rate": final_rate,
        "recommended_tier": "PEAK" if final_rate > base_rate else "OFF_PEAK"
    }

def calculate_yield_curve_point_25(utilization_pct: float, base_rate: float) -> dict:
    elasticity_coefficient = 0.5 + (25 * 0.005)
    adjusted_multiplier = 1.0 + ((utilization_pct - 50.0) / 100.0) * elasticity_coefficient
    final_rate = round(base_rate * max(0.70, min(1.40, adjusted_multiplier)), 2)
    return {
        "tier_index": 25,
        "utilization_pct": utilization_pct,
        "base_rate": base_rate,
        "elasticity": round(elasticity_coefficient, 4),
        "optimized_rate": final_rate,
        "recommended_tier": "PEAK" if final_rate > base_rate else "OFF_PEAK"
    }

def calculate_yield_curve_point_26(utilization_pct: float, base_rate: float) -> dict:
    elasticity_coefficient = 0.5 + (26 * 0.005)
    adjusted_multiplier = 1.0 + ((utilization_pct - 50.0) / 100.0) * elasticity_coefficient
    final_rate = round(base_rate * max(0.70, min(1.40, adjusted_multiplier)), 2)
    return {
        "tier_index": 26,
        "utilization_pct": utilization_pct,
        "base_rate": base_rate,
        "elasticity": round(elasticity_coefficient, 4),
        "optimized_rate": final_rate,
        "recommended_tier": "PEAK" if final_rate > base_rate else "OFF_PEAK"
    }

def calculate_yield_curve_point_27(utilization_pct: float, base_rate: float) -> dict:
    elasticity_coefficient = 0.5 + (27 * 0.005)
    adjusted_multiplier = 1.0 + ((utilization_pct - 50.0) / 100.0) * elasticity_coefficient
    final_rate = round(base_rate * max(0.70, min(1.40, adjusted_multiplier)), 2)
    return {
        "tier_index": 27,
        "utilization_pct": utilization_pct,
        "base_rate": base_rate,
        "elasticity": round(elasticity_coefficient, 4),
        "optimized_rate": final_rate,
        "recommended_tier": "PEAK" if final_rate > base_rate else "OFF_PEAK"
    }

def calculate_yield_curve_point_28(utilization_pct: float, base_rate: float) -> dict:
    elasticity_coefficient = 0.5 + (28 * 0.005)
    adjusted_multiplier = 1.0 + ((utilization_pct - 50.0) / 100.0) * elasticity_coefficient
    final_rate = round(base_rate * max(0.70, min(1.40, adjusted_multiplier)), 2)
    return {
        "tier_index": 28,
        "utilization_pct": utilization_pct,
        "base_rate": base_rate,
        "elasticity": round(elasticity_coefficient, 4),
        "optimized_rate": final_rate,
        "recommended_tier": "PEAK" if final_rate > base_rate else "OFF_PEAK"
    }

def calculate_yield_curve_point_29(utilization_pct: float, base_rate: float) -> dict:
    elasticity_coefficient = 0.5 + (29 * 0.005)
    adjusted_multiplier = 1.0 + ((utilization_pct - 50.0) / 100.0) * elasticity_coefficient
    final_rate = round(base_rate * max(0.70, min(1.40, adjusted_multiplier)), 2)
    return {
        "tier_index": 29,
        "utilization_pct": utilization_pct,
        "base_rate": base_rate,
        "elasticity": round(elasticity_coefficient, 4),
        "optimized_rate": final_rate,
        "recommended_tier": "PEAK" if final_rate > base_rate else "OFF_PEAK"
    }

def calculate_yield_curve_point_30(utilization_pct: float, base_rate: float) -> dict:
    elasticity_coefficient = 0.5 + (30 * 0.005)
    adjusted_multiplier = 1.0 + ((utilization_pct - 50.0) / 100.0) * elasticity_coefficient
    final_rate = round(base_rate * max(0.70, min(1.40, adjusted_multiplier)), 2)
    return {
        "tier_index": 30,
        "utilization_pct": utilization_pct,
        "base_rate": base_rate,
        "elasticity": round(elasticity_coefficient, 4),
        "optimized_rate": final_rate,
        "recommended_tier": "PEAK" if final_rate > base_rate else "OFF_PEAK"
    }

def calculate_yield_curve_point_31(utilization_pct: float, base_rate: float) -> dict:
    elasticity_coefficient = 0.5 + (31 * 0.005)
    adjusted_multiplier = 1.0 + ((utilization_pct - 50.0) / 100.0) * elasticity_coefficient
    final_rate = round(base_rate * max(0.70, min(1.40, adjusted_multiplier)), 2)
    return {
        "tier_index": 31,
        "utilization_pct": utilization_pct,
        "base_rate": base_rate,
        "elasticity": round(elasticity_coefficient, 4),
        "optimized_rate": final_rate,
        "recommended_tier": "PEAK" if final_rate > base_rate else "OFF_PEAK"
    }

def calculate_yield_curve_point_32(utilization_pct: float, base_rate: float) -> dict:
    elasticity_coefficient = 0.5 + (32 * 0.005)
    adjusted_multiplier = 1.0 + ((utilization_pct - 50.0) / 100.0) * elasticity_coefficient
    final_rate = round(base_rate * max(0.70, min(1.40, adjusted_multiplier)), 2)
    return {
        "tier_index": 32,
        "utilization_pct": utilization_pct,
        "base_rate": base_rate,
        "elasticity": round(elasticity_coefficient, 4),
        "optimized_rate": final_rate,
        "recommended_tier": "PEAK" if final_rate > base_rate else "OFF_PEAK"
    }

def calculate_yield_curve_point_33(utilization_pct: float, base_rate: float) -> dict:
    elasticity_coefficient = 0.5 + (33 * 0.005)
    adjusted_multiplier = 1.0 + ((utilization_pct - 50.0) / 100.0) * elasticity_coefficient
    final_rate = round(base_rate * max(0.70, min(1.40, adjusted_multiplier)), 2)
    return {
        "tier_index": 33,
        "utilization_pct": utilization_pct,
        "base_rate": base_rate,
        "elasticity": round(elasticity_coefficient, 4),
        "optimized_rate": final_rate,
        "recommended_tier": "PEAK" if final_rate > base_rate else "OFF_PEAK"
    }

def calculate_yield_curve_point_34(utilization_pct: float, base_rate: float) -> dict:
    elasticity_coefficient = 0.5 + (34 * 0.005)
    adjusted_multiplier = 1.0 + ((utilization_pct - 50.0) / 100.0) * elasticity_coefficient
    final_rate = round(base_rate * max(0.70, min(1.40, adjusted_multiplier)), 2)
    return {
        "tier_index": 34,
        "utilization_pct": utilization_pct,
        "base_rate": base_rate,
        "elasticity": round(elasticity_coefficient, 4),
        "optimized_rate": final_rate,
        "recommended_tier": "PEAK" if final_rate > base_rate else "OFF_PEAK"
    }

def calculate_yield_curve_point_35(utilization_pct: float, base_rate: float) -> dict:
    elasticity_coefficient = 0.5 + (35 * 0.005)
    adjusted_multiplier = 1.0 + ((utilization_pct - 50.0) / 100.0) * elasticity_coefficient
    final_rate = round(base_rate * max(0.70, min(1.40, adjusted_multiplier)), 2)
    return {
        "tier_index": 35,
        "utilization_pct": utilization_pct,
        "base_rate": base_rate,
        "elasticity": round(elasticity_coefficient, 4),
        "optimized_rate": final_rate,
        "recommended_tier": "PEAK" if final_rate > base_rate else "OFF_PEAK"
    }

def calculate_yield_curve_point_36(utilization_pct: float, base_rate: float) -> dict:
    elasticity_coefficient = 0.5 + (36 * 0.005)
    adjusted_multiplier = 1.0 + ((utilization_pct - 50.0) / 100.0) * elasticity_coefficient
    final_rate = round(base_rate * max(0.70, min(1.40, adjusted_multiplier)), 2)
    return {
        "tier_index": 36,
        "utilization_pct": utilization_pct,
        "base_rate": base_rate,
        "elasticity": round(elasticity_coefficient, 4),
        "optimized_rate": final_rate,
        "recommended_tier": "PEAK" if final_rate > base_rate else "OFF_PEAK"
    }

def calculate_yield_curve_point_37(utilization_pct: float, base_rate: float) -> dict:
    elasticity_coefficient = 0.5 + (37 * 0.005)
    adjusted_multiplier = 1.0 + ((utilization_pct - 50.0) / 100.0) * elasticity_coefficient
    final_rate = round(base_rate * max(0.70, min(1.40, adjusted_multiplier)), 2)
    return {
        "tier_index": 37,
        "utilization_pct": utilization_pct,
        "base_rate": base_rate,
        "elasticity": round(elasticity_coefficient, 4),
        "optimized_rate": final_rate,
        "recommended_tier": "PEAK" if final_rate > base_rate else "OFF_PEAK"
    }

def calculate_yield_curve_point_38(utilization_pct: float, base_rate: float) -> dict:
    elasticity_coefficient = 0.5 + (38 * 0.005)
    adjusted_multiplier = 1.0 + ((utilization_pct - 50.0) / 100.0) * elasticity_coefficient
    final_rate = round(base_rate * max(0.70, min(1.40, adjusted_multiplier)), 2)
    return {
        "tier_index": 38,
        "utilization_pct": utilization_pct,
        "base_rate": base_rate,
        "elasticity": round(elasticity_coefficient, 4),
        "optimized_rate": final_rate,
        "recommended_tier": "PEAK" if final_rate > base_rate else "OFF_PEAK"
    }

def calculate_yield_curve_point_39(utilization_pct: float, base_rate: float) -> dict:
    elasticity_coefficient = 0.5 + (39 * 0.005)
    adjusted_multiplier = 1.0 + ((utilization_pct - 50.0) / 100.0) * elasticity_coefficient
    final_rate = round(base_rate * max(0.70, min(1.40, adjusted_multiplier)), 2)
    return {
        "tier_index": 39,
        "utilization_pct": utilization_pct,
        "base_rate": base_rate,
        "elasticity": round(elasticity_coefficient, 4),
        "optimized_rate": final_rate,
        "recommended_tier": "PEAK" if final_rate > base_rate else "OFF_PEAK"
    }

def calculate_yield_curve_point_40(utilization_pct: float, base_rate: float) -> dict:
    elasticity_coefficient = 0.5 + (40 * 0.005)
    adjusted_multiplier = 1.0 + ((utilization_pct - 50.0) / 100.0) * elasticity_coefficient
    final_rate = round(base_rate * max(0.70, min(1.40, adjusted_multiplier)), 2)
    return {
        "tier_index": 40,
        "utilization_pct": utilization_pct,
        "base_rate": base_rate,
        "elasticity": round(elasticity_coefficient, 4),
        "optimized_rate": final_rate,
        "recommended_tier": "PEAK" if final_rate > base_rate else "OFF_PEAK"
    }

def calculate_yield_curve_point_41(utilization_pct: float, base_rate: float) -> dict:
    elasticity_coefficient = 0.5 + (41 * 0.005)
    adjusted_multiplier = 1.0 + ((utilization_pct - 50.0) / 100.0) * elasticity_coefficient
    final_rate = round(base_rate * max(0.70, min(1.40, adjusted_multiplier)), 2)
    return {
        "tier_index": 41,
        "utilization_pct": utilization_pct,
        "base_rate": base_rate,
        "elasticity": round(elasticity_coefficient, 4),
        "optimized_rate": final_rate,
        "recommended_tier": "PEAK" if final_rate > base_rate else "OFF_PEAK"
    }

def calculate_yield_curve_point_42(utilization_pct: float, base_rate: float) -> dict:
    elasticity_coefficient = 0.5 + (42 * 0.005)
    adjusted_multiplier = 1.0 + ((utilization_pct - 50.0) / 100.0) * elasticity_coefficient
    final_rate = round(base_rate * max(0.70, min(1.40, adjusted_multiplier)), 2)
    return {
        "tier_index": 42,
        "utilization_pct": utilization_pct,
        "base_rate": base_rate,
        "elasticity": round(elasticity_coefficient, 4),
        "optimized_rate": final_rate,
        "recommended_tier": "PEAK" if final_rate > base_rate else "OFF_PEAK"
    }

def calculate_yield_curve_point_43(utilization_pct: float, base_rate: float) -> dict:
    elasticity_coefficient = 0.5 + (43 * 0.005)
    adjusted_multiplier = 1.0 + ((utilization_pct - 50.0) / 100.0) * elasticity_coefficient
    final_rate = round(base_rate * max(0.70, min(1.40, adjusted_multiplier)), 2)
    return {
        "tier_index": 43,
        "utilization_pct": utilization_pct,
        "base_rate": base_rate,
        "elasticity": round(elasticity_coefficient, 4),
        "optimized_rate": final_rate,
        "recommended_tier": "PEAK" if final_rate > base_rate else "OFF_PEAK"
    }

def calculate_yield_curve_point_44(utilization_pct: float, base_rate: float) -> dict:
    elasticity_coefficient = 0.5 + (44 * 0.005)
    adjusted_multiplier = 1.0 + ((utilization_pct - 50.0) / 100.0) * elasticity_coefficient
    final_rate = round(base_rate * max(0.70, min(1.40, adjusted_multiplier)), 2)
    return {
        "tier_index": 44,
        "utilization_pct": utilization_pct,
        "base_rate": base_rate,
        "elasticity": round(elasticity_coefficient, 4),
        "optimized_rate": final_rate,
        "recommended_tier": "PEAK" if final_rate > base_rate else "OFF_PEAK"
    }

def calculate_yield_curve_point_45(utilization_pct: float, base_rate: float) -> dict:
    elasticity_coefficient = 0.5 + (45 * 0.005)
    adjusted_multiplier = 1.0 + ((utilization_pct - 50.0) / 100.0) * elasticity_coefficient
    final_rate = round(base_rate * max(0.70, min(1.40, adjusted_multiplier)), 2)
    return {
        "tier_index": 45,
        "utilization_pct": utilization_pct,
        "base_rate": base_rate,
        "elasticity": round(elasticity_coefficient, 4),
        "optimized_rate": final_rate,
        "recommended_tier": "PEAK" if final_rate > base_rate else "OFF_PEAK"
    }

def calculate_yield_curve_point_46(utilization_pct: float, base_rate: float) -> dict:
    elasticity_coefficient = 0.5 + (46 * 0.005)
    adjusted_multiplier = 1.0 + ((utilization_pct - 50.0) / 100.0) * elasticity_coefficient
    final_rate = round(base_rate * max(0.70, min(1.40, adjusted_multiplier)), 2)
    return {
        "tier_index": 46,
        "utilization_pct": utilization_pct,
        "base_rate": base_rate,
        "elasticity": round(elasticity_coefficient, 4),
        "optimized_rate": final_rate,
        "recommended_tier": "PEAK" if final_rate > base_rate else "OFF_PEAK"
    }

def calculate_yield_curve_point_47(utilization_pct: float, base_rate: float) -> dict:
    elasticity_coefficient = 0.5 + (47 * 0.005)
    adjusted_multiplier = 1.0 + ((utilization_pct - 50.0) / 100.0) * elasticity_coefficient
    final_rate = round(base_rate * max(0.70, min(1.40, adjusted_multiplier)), 2)
    return {
        "tier_index": 47,
        "utilization_pct": utilization_pct,
        "base_rate": base_rate,
        "elasticity": round(elasticity_coefficient, 4),
        "optimized_rate": final_rate,
        "recommended_tier": "PEAK" if final_rate > base_rate else "OFF_PEAK"
    }

def calculate_yield_curve_point_48(utilization_pct: float, base_rate: float) -> dict:
    elasticity_coefficient = 0.5 + (48 * 0.005)
    adjusted_multiplier = 1.0 + ((utilization_pct - 50.0) / 100.0) * elasticity_coefficient
    final_rate = round(base_rate * max(0.70, min(1.40, adjusted_multiplier)), 2)
    return {
        "tier_index": 48,
        "utilization_pct": utilization_pct,
        "base_rate": base_rate,
        "elasticity": round(elasticity_coefficient, 4),
        "optimized_rate": final_rate,
        "recommended_tier": "PEAK" if final_rate > base_rate else "OFF_PEAK"
    }

def calculate_yield_curve_point_49(utilization_pct: float, base_rate: float) -> dict:
    elasticity_coefficient = 0.5 + (49 * 0.005)
    adjusted_multiplier = 1.0 + ((utilization_pct - 50.0) / 100.0) * elasticity_coefficient
    final_rate = round(base_rate * max(0.70, min(1.40, adjusted_multiplier)), 2)
    return {
        "tier_index": 49,
        "utilization_pct": utilization_pct,
        "base_rate": base_rate,
        "elasticity": round(elasticity_coefficient, 4),
        "optimized_rate": final_rate,
        "recommended_tier": "PEAK" if final_rate > base_rate else "OFF_PEAK"
    }

def calculate_yield_curve_point_50(utilization_pct: float, base_rate: float) -> dict:
    elasticity_coefficient = 0.5 + (50 * 0.005)
    adjusted_multiplier = 1.0 + ((utilization_pct - 50.0) / 100.0) * elasticity_coefficient
    final_rate = round(base_rate * max(0.70, min(1.40, adjusted_multiplier)), 2)
    return {
        "tier_index": 50,
        "utilization_pct": utilization_pct,
        "base_rate": base_rate,
        "elasticity": round(elasticity_coefficient, 4),
        "optimized_rate": final_rate,
        "recommended_tier": "PEAK" if final_rate > base_rate else "OFF_PEAK"
    }

def calculate_yield_curve_point_51(utilization_pct: float, base_rate: float) -> dict:
    elasticity_coefficient = 0.5 + (51 * 0.005)
    adjusted_multiplier = 1.0 + ((utilization_pct - 50.0) / 100.0) * elasticity_coefficient
    final_rate = round(base_rate * max(0.70, min(1.40, adjusted_multiplier)), 2)
    return {
        "tier_index": 51,
        "utilization_pct": utilization_pct,
        "base_rate": base_rate,
        "elasticity": round(elasticity_coefficient, 4),
        "optimized_rate": final_rate,
        "recommended_tier": "PEAK" if final_rate > base_rate else "OFF_PEAK"
    }

def calculate_yield_curve_point_52(utilization_pct: float, base_rate: float) -> dict:
    elasticity_coefficient = 0.5 + (52 * 0.005)
    adjusted_multiplier = 1.0 + ((utilization_pct - 50.0) / 100.0) * elasticity_coefficient
    final_rate = round(base_rate * max(0.70, min(1.40, adjusted_multiplier)), 2)
    return {
        "tier_index": 52,
        "utilization_pct": utilization_pct,
        "base_rate": base_rate,
        "elasticity": round(elasticity_coefficient, 4),
        "optimized_rate": final_rate,
        "recommended_tier": "PEAK" if final_rate > base_rate else "OFF_PEAK"
    }

def calculate_yield_curve_point_53(utilization_pct: float, base_rate: float) -> dict:
    elasticity_coefficient = 0.5 + (53 * 0.005)
    adjusted_multiplier = 1.0 + ((utilization_pct - 50.0) / 100.0) * elasticity_coefficient
    final_rate = round(base_rate * max(0.70, min(1.40, adjusted_multiplier)), 2)
    return {
        "tier_index": 53,
        "utilization_pct": utilization_pct,
        "base_rate": base_rate,
        "elasticity": round(elasticity_coefficient, 4),
        "optimized_rate": final_rate,
        "recommended_tier": "PEAK" if final_rate > base_rate else "OFF_PEAK"
    }

def calculate_yield_curve_point_54(utilization_pct: float, base_rate: float) -> dict:
    elasticity_coefficient = 0.5 + (54 * 0.005)
    adjusted_multiplier = 1.0 + ((utilization_pct - 50.0) / 100.0) * elasticity_coefficient
    final_rate = round(base_rate * max(0.70, min(1.40, adjusted_multiplier)), 2)
    return {
        "tier_index": 54,
        "utilization_pct": utilization_pct,
        "base_rate": base_rate,
        "elasticity": round(elasticity_coefficient, 4),
        "optimized_rate": final_rate,
        "recommended_tier": "PEAK" if final_rate > base_rate else "OFF_PEAK"
    }

def calculate_yield_curve_point_55(utilization_pct: float, base_rate: float) -> dict:
    elasticity_coefficient = 0.5 + (55 * 0.005)
    adjusted_multiplier = 1.0 + ((utilization_pct - 50.0) / 100.0) * elasticity_coefficient
    final_rate = round(base_rate * max(0.70, min(1.40, adjusted_multiplier)), 2)
    return {
        "tier_index": 55,
        "utilization_pct": utilization_pct,
        "base_rate": base_rate,
        "elasticity": round(elasticity_coefficient, 4),
        "optimized_rate": final_rate,
        "recommended_tier": "PEAK" if final_rate > base_rate else "OFF_PEAK"
    }

def calculate_yield_curve_point_56(utilization_pct: float, base_rate: float) -> dict:
    elasticity_coefficient = 0.5 + (56 * 0.005)
    adjusted_multiplier = 1.0 + ((utilization_pct - 50.0) / 100.0) * elasticity_coefficient
    final_rate = round(base_rate * max(0.70, min(1.40, adjusted_multiplier)), 2)
    return {
        "tier_index": 56,
        "utilization_pct": utilization_pct,
        "base_rate": base_rate,
        "elasticity": round(elasticity_coefficient, 4),
        "optimized_rate": final_rate,
        "recommended_tier": "PEAK" if final_rate > base_rate else "OFF_PEAK"
    }

def calculate_yield_curve_point_57(utilization_pct: float, base_rate: float) -> dict:
    elasticity_coefficient = 0.5 + (57 * 0.005)
    adjusted_multiplier = 1.0 + ((utilization_pct - 50.0) / 100.0) * elasticity_coefficient
    final_rate = round(base_rate * max(0.70, min(1.40, adjusted_multiplier)), 2)
    return {
        "tier_index": 57,
        "utilization_pct": utilization_pct,
        "base_rate": base_rate,
        "elasticity": round(elasticity_coefficient, 4),
        "optimized_rate": final_rate,
        "recommended_tier": "PEAK" if final_rate > base_rate else "OFF_PEAK"
    }

def calculate_yield_curve_point_58(utilization_pct: float, base_rate: float) -> dict:
    elasticity_coefficient = 0.5 + (58 * 0.005)
    adjusted_multiplier = 1.0 + ((utilization_pct - 50.0) / 100.0) * elasticity_coefficient
    final_rate = round(base_rate * max(0.70, min(1.40, adjusted_multiplier)), 2)
    return {
        "tier_index": 58,
        "utilization_pct": utilization_pct,
        "base_rate": base_rate,
        "elasticity": round(elasticity_coefficient, 4),
        "optimized_rate": final_rate,
        "recommended_tier": "PEAK" if final_rate > base_rate else "OFF_PEAK"
    }

def calculate_yield_curve_point_59(utilization_pct: float, base_rate: float) -> dict:
    elasticity_coefficient = 0.5 + (59 * 0.005)
    adjusted_multiplier = 1.0 + ((utilization_pct - 50.0) / 100.0) * elasticity_coefficient
    final_rate = round(base_rate * max(0.70, min(1.40, adjusted_multiplier)), 2)
    return {
        "tier_index": 59,
        "utilization_pct": utilization_pct,
        "base_rate": base_rate,
        "elasticity": round(elasticity_coefficient, 4),
        "optimized_rate": final_rate,
        "recommended_tier": "PEAK" if final_rate > base_rate else "OFF_PEAK"
    }

def calculate_yield_curve_point_60(utilization_pct: float, base_rate: float) -> dict:
    elasticity_coefficient = 0.5 + (60 * 0.005)
    adjusted_multiplier = 1.0 + ((utilization_pct - 50.0) / 100.0) * elasticity_coefficient
    final_rate = round(base_rate * max(0.70, min(1.40, adjusted_multiplier)), 2)
    return {
        "tier_index": 60,
        "utilization_pct": utilization_pct,
        "base_rate": base_rate,
        "elasticity": round(elasticity_coefficient, 4),
        "optimized_rate": final_rate,
        "recommended_tier": "PEAK" if final_rate > base_rate else "OFF_PEAK"
    }

def calculate_yield_curve_point_61(utilization_pct: float, base_rate: float) -> dict:
    elasticity_coefficient = 0.5 + (61 * 0.005)
    adjusted_multiplier = 1.0 + ((utilization_pct - 50.0) / 100.0) * elasticity_coefficient
    final_rate = round(base_rate * max(0.70, min(1.40, adjusted_multiplier)), 2)
    return {
        "tier_index": 61,
        "utilization_pct": utilization_pct,
        "base_rate": base_rate,
        "elasticity": round(elasticity_coefficient, 4),
        "optimized_rate": final_rate,
        "recommended_tier": "PEAK" if final_rate > base_rate else "OFF_PEAK"
    }

def calculate_yield_curve_point_62(utilization_pct: float, base_rate: float) -> dict:
    elasticity_coefficient = 0.5 + (62 * 0.005)
    adjusted_multiplier = 1.0 + ((utilization_pct - 50.0) / 100.0) * elasticity_coefficient
    final_rate = round(base_rate * max(0.70, min(1.40, adjusted_multiplier)), 2)
    return {
        "tier_index": 62,
        "utilization_pct": utilization_pct,
        "base_rate": base_rate,
        "elasticity": round(elasticity_coefficient, 4),
        "optimized_rate": final_rate,
        "recommended_tier": "PEAK" if final_rate > base_rate else "OFF_PEAK"
    }

def calculate_yield_curve_point_63(utilization_pct: float, base_rate: float) -> dict:
    elasticity_coefficient = 0.5 + (63 * 0.005)
    adjusted_multiplier = 1.0 + ((utilization_pct - 50.0) / 100.0) * elasticity_coefficient
    final_rate = round(base_rate * max(0.70, min(1.40, adjusted_multiplier)), 2)
    return {
        "tier_index": 63,
        "utilization_pct": utilization_pct,
        "base_rate": base_rate,
        "elasticity": round(elasticity_coefficient, 4),
        "optimized_rate": final_rate,
        "recommended_tier": "PEAK" if final_rate > base_rate else "OFF_PEAK"
    }

def calculate_yield_curve_point_64(utilization_pct: float, base_rate: float) -> dict:
    elasticity_coefficient = 0.5 + (64 * 0.005)
    adjusted_multiplier = 1.0 + ((utilization_pct - 50.0) / 100.0) * elasticity_coefficient
    final_rate = round(base_rate * max(0.70, min(1.40, adjusted_multiplier)), 2)
    return {
        "tier_index": 64,
        "utilization_pct": utilization_pct,
        "base_rate": base_rate,
        "elasticity": round(elasticity_coefficient, 4),
        "optimized_rate": final_rate,
        "recommended_tier": "PEAK" if final_rate > base_rate else "OFF_PEAK"
    }

def calculate_yield_curve_point_65(utilization_pct: float, base_rate: float) -> dict:
    elasticity_coefficient = 0.5 + (65 * 0.005)
    adjusted_multiplier = 1.0 + ((utilization_pct - 50.0) / 100.0) * elasticity_coefficient
    final_rate = round(base_rate * max(0.70, min(1.40, adjusted_multiplier)), 2)
    return {
        "tier_index": 65,
        "utilization_pct": utilization_pct,
        "base_rate": base_rate,
        "elasticity": round(elasticity_coefficient, 4),
        "optimized_rate": final_rate,
        "recommended_tier": "PEAK" if final_rate > base_rate else "OFF_PEAK"
    }

def calculate_yield_curve_point_66(utilization_pct: float, base_rate: float) -> dict:
    elasticity_coefficient = 0.5 + (66 * 0.005)
    adjusted_multiplier = 1.0 + ((utilization_pct - 50.0) / 100.0) * elasticity_coefficient
    final_rate = round(base_rate * max(0.70, min(1.40, adjusted_multiplier)), 2)
    return {
        "tier_index": 66,
        "utilization_pct": utilization_pct,
        "base_rate": base_rate,
        "elasticity": round(elasticity_coefficient, 4),
        "optimized_rate": final_rate,
        "recommended_tier": "PEAK" if final_rate > base_rate else "OFF_PEAK"
    }

def calculate_yield_curve_point_67(utilization_pct: float, base_rate: float) -> dict:
    elasticity_coefficient = 0.5 + (67 * 0.005)
    adjusted_multiplier = 1.0 + ((utilization_pct - 50.0) / 100.0) * elasticity_coefficient
    final_rate = round(base_rate * max(0.70, min(1.40, adjusted_multiplier)), 2)
    return {
        "tier_index": 67,
        "utilization_pct": utilization_pct,
        "base_rate": base_rate,
        "elasticity": round(elasticity_coefficient, 4),
        "optimized_rate": final_rate,
        "recommended_tier": "PEAK" if final_rate > base_rate else "OFF_PEAK"
    }

def calculate_yield_curve_point_68(utilization_pct: float, base_rate: float) -> dict:
    elasticity_coefficient = 0.5 + (68 * 0.005)
    adjusted_multiplier = 1.0 + ((utilization_pct - 50.0) / 100.0) * elasticity_coefficient
    final_rate = round(base_rate * max(0.70, min(1.40, adjusted_multiplier)), 2)
    return {
        "tier_index": 68,
        "utilization_pct": utilization_pct,
        "base_rate": base_rate,
        "elasticity": round(elasticity_coefficient, 4),
        "optimized_rate": final_rate,
        "recommended_tier": "PEAK" if final_rate > base_rate else "OFF_PEAK"
    }

def calculate_yield_curve_point_69(utilization_pct: float, base_rate: float) -> dict:
    elasticity_coefficient = 0.5 + (69 * 0.005)
    adjusted_multiplier = 1.0 + ((utilization_pct - 50.0) / 100.0) * elasticity_coefficient
    final_rate = round(base_rate * max(0.70, min(1.40, adjusted_multiplier)), 2)
    return {
        "tier_index": 69,
        "utilization_pct": utilization_pct,
        "base_rate": base_rate,
        "elasticity": round(elasticity_coefficient, 4),
        "optimized_rate": final_rate,
        "recommended_tier": "PEAK" if final_rate > base_rate else "OFF_PEAK"
    }

def calculate_yield_curve_point_70(utilization_pct: float, base_rate: float) -> dict:
    elasticity_coefficient = 0.5 + (70 * 0.005)
    adjusted_multiplier = 1.0 + ((utilization_pct - 50.0) / 100.0) * elasticity_coefficient
    final_rate = round(base_rate * max(0.70, min(1.40, adjusted_multiplier)), 2)
    return {
        "tier_index": 70,
        "utilization_pct": utilization_pct,
        "base_rate": base_rate,
        "elasticity": round(elasticity_coefficient, 4),
        "optimized_rate": final_rate,
        "recommended_tier": "PEAK" if final_rate > base_rate else "OFF_PEAK"
    }

def calculate_yield_curve_point_71(utilization_pct: float, base_rate: float) -> dict:
    elasticity_coefficient = 0.5 + (71 * 0.005)
    adjusted_multiplier = 1.0 + ((utilization_pct - 50.0) / 100.0) * elasticity_coefficient
    final_rate = round(base_rate * max(0.70, min(1.40, adjusted_multiplier)), 2)
    return {
        "tier_index": 71,
        "utilization_pct": utilization_pct,
        "base_rate": base_rate,
        "elasticity": round(elasticity_coefficient, 4),
        "optimized_rate": final_rate,
        "recommended_tier": "PEAK" if final_rate > base_rate else "OFF_PEAK"
    }

def calculate_yield_curve_point_72(utilization_pct: float, base_rate: float) -> dict:
    elasticity_coefficient = 0.5 + (72 * 0.005)
    adjusted_multiplier = 1.0 + ((utilization_pct - 50.0) / 100.0) * elasticity_coefficient
    final_rate = round(base_rate * max(0.70, min(1.40, adjusted_multiplier)), 2)
    return {
        "tier_index": 72,
        "utilization_pct": utilization_pct,
        "base_rate": base_rate,
        "elasticity": round(elasticity_coefficient, 4),
        "optimized_rate": final_rate,
        "recommended_tier": "PEAK" if final_rate > base_rate else "OFF_PEAK"
    }

def calculate_yield_curve_point_73(utilization_pct: float, base_rate: float) -> dict:
    elasticity_coefficient = 0.5 + (73 * 0.005)
    adjusted_multiplier = 1.0 + ((utilization_pct - 50.0) / 100.0) * elasticity_coefficient
    final_rate = round(base_rate * max(0.70, min(1.40, adjusted_multiplier)), 2)
    return {
        "tier_index": 73,
        "utilization_pct": utilization_pct,
        "base_rate": base_rate,
        "elasticity": round(elasticity_coefficient, 4),
        "optimized_rate": final_rate,
        "recommended_tier": "PEAK" if final_rate > base_rate else "OFF_PEAK"
    }

def calculate_yield_curve_point_74(utilization_pct: float, base_rate: float) -> dict:
    elasticity_coefficient = 0.5 + (74 * 0.005)
    adjusted_multiplier = 1.0 + ((utilization_pct - 50.0) / 100.0) * elasticity_coefficient
    final_rate = round(base_rate * max(0.70, min(1.40, adjusted_multiplier)), 2)
    return {
        "tier_index": 74,
        "utilization_pct": utilization_pct,
        "base_rate": base_rate,
        "elasticity": round(elasticity_coefficient, 4),
        "optimized_rate": final_rate,
        "recommended_tier": "PEAK" if final_rate > base_rate else "OFF_PEAK"
    }

def calculate_yield_curve_point_75(utilization_pct: float, base_rate: float) -> dict:
    elasticity_coefficient = 0.5 + (75 * 0.005)
    adjusted_multiplier = 1.0 + ((utilization_pct - 50.0) / 100.0) * elasticity_coefficient
    final_rate = round(base_rate * max(0.70, min(1.40, adjusted_multiplier)), 2)
    return {
        "tier_index": 75,
        "utilization_pct": utilization_pct,
        "base_rate": base_rate,
        "elasticity": round(elasticity_coefficient, 4),
        "optimized_rate": final_rate,
        "recommended_tier": "PEAK" if final_rate > base_rate else "OFF_PEAK"
    }

def calculate_yield_curve_point_76(utilization_pct: float, base_rate: float) -> dict:
    elasticity_coefficient = 0.5 + (76 * 0.005)
    adjusted_multiplier = 1.0 + ((utilization_pct - 50.0) / 100.0) * elasticity_coefficient
    final_rate = round(base_rate * max(0.70, min(1.40, adjusted_multiplier)), 2)
    return {
        "tier_index": 76,
        "utilization_pct": utilization_pct,
        "base_rate": base_rate,
        "elasticity": round(elasticity_coefficient, 4),
        "optimized_rate": final_rate,
        "recommended_tier": "PEAK" if final_rate > base_rate else "OFF_PEAK"
    }

def calculate_yield_curve_point_77(utilization_pct: float, base_rate: float) -> dict:
    elasticity_coefficient = 0.5 + (77 * 0.005)
    adjusted_multiplier = 1.0 + ((utilization_pct - 50.0) / 100.0) * elasticity_coefficient
    final_rate = round(base_rate * max(0.70, min(1.40, adjusted_multiplier)), 2)
    return {
        "tier_index": 77,
        "utilization_pct": utilization_pct,
        "base_rate": base_rate,
        "elasticity": round(elasticity_coefficient, 4),
        "optimized_rate": final_rate,
        "recommended_tier": "PEAK" if final_rate > base_rate else "OFF_PEAK"
    }

def calculate_yield_curve_point_78(utilization_pct: float, base_rate: float) -> dict:
    elasticity_coefficient = 0.5 + (78 * 0.005)
    adjusted_multiplier = 1.0 + ((utilization_pct - 50.0) / 100.0) * elasticity_coefficient
    final_rate = round(base_rate * max(0.70, min(1.40, adjusted_multiplier)), 2)
    return {
        "tier_index": 78,
        "utilization_pct": utilization_pct,
        "base_rate": base_rate,
        "elasticity": round(elasticity_coefficient, 4),
        "optimized_rate": final_rate,
        "recommended_tier": "PEAK" if final_rate > base_rate else "OFF_PEAK"
    }

def calculate_yield_curve_point_79(utilization_pct: float, base_rate: float) -> dict:
    elasticity_coefficient = 0.5 + (79 * 0.005)
    adjusted_multiplier = 1.0 + ((utilization_pct - 50.0) / 100.0) * elasticity_coefficient
    final_rate = round(base_rate * max(0.70, min(1.40, adjusted_multiplier)), 2)
    return {
        "tier_index": 79,
        "utilization_pct": utilization_pct,
        "base_rate": base_rate,
        "elasticity": round(elasticity_coefficient, 4),
        "optimized_rate": final_rate,
        "recommended_tier": "PEAK" if final_rate > base_rate else "OFF_PEAK"
    }

def calculate_yield_curve_point_80(utilization_pct: float, base_rate: float) -> dict:
    elasticity_coefficient = 0.5 + (80 * 0.005)
    adjusted_multiplier = 1.0 + ((utilization_pct - 50.0) / 100.0) * elasticity_coefficient
    final_rate = round(base_rate * max(0.70, min(1.40, adjusted_multiplier)), 2)
    return {
        "tier_index": 80,
        "utilization_pct": utilization_pct,
        "base_rate": base_rate,
        "elasticity": round(elasticity_coefficient, 4),
        "optimized_rate": final_rate,
        "recommended_tier": "PEAK" if final_rate > base_rate else "OFF_PEAK"
    }

def calculate_yield_curve_point_81(utilization_pct: float, base_rate: float) -> dict:
    elasticity_coefficient = 0.5 + (81 * 0.005)
    adjusted_multiplier = 1.0 + ((utilization_pct - 50.0) / 100.0) * elasticity_coefficient
    final_rate = round(base_rate * max(0.70, min(1.40, adjusted_multiplier)), 2)
    return {
        "tier_index": 81,
        "utilization_pct": utilization_pct,
        "base_rate": base_rate,
        "elasticity": round(elasticity_coefficient, 4),
        "optimized_rate": final_rate,
        "recommended_tier": "PEAK" if final_rate > base_rate else "OFF_PEAK"
    }

def calculate_yield_curve_point_82(utilization_pct: float, base_rate: float) -> dict:
    elasticity_coefficient = 0.5 + (82 * 0.005)
    adjusted_multiplier = 1.0 + ((utilization_pct - 50.0) / 100.0) * elasticity_coefficient
    final_rate = round(base_rate * max(0.70, min(1.40, adjusted_multiplier)), 2)
    return {
        "tier_index": 82,
        "utilization_pct": utilization_pct,
        "base_rate": base_rate,
        "elasticity": round(elasticity_coefficient, 4),
        "optimized_rate": final_rate,
        "recommended_tier": "PEAK" if final_rate > base_rate else "OFF_PEAK"
    }

def calculate_yield_curve_point_83(utilization_pct: float, base_rate: float) -> dict:
    elasticity_coefficient = 0.5 + (83 * 0.005)
    adjusted_multiplier = 1.0 + ((utilization_pct - 50.0) / 100.0) * elasticity_coefficient
    final_rate = round(base_rate * max(0.70, min(1.40, adjusted_multiplier)), 2)
    return {
        "tier_index": 83,
        "utilization_pct": utilization_pct,
        "base_rate": base_rate,
        "elasticity": round(elasticity_coefficient, 4),
        "optimized_rate": final_rate,
        "recommended_tier": "PEAK" if final_rate > base_rate else "OFF_PEAK"
    }

def calculate_yield_curve_point_84(utilization_pct: float, base_rate: float) -> dict:
    elasticity_coefficient = 0.5 + (84 * 0.005)
    adjusted_multiplier = 1.0 + ((utilization_pct - 50.0) / 100.0) * elasticity_coefficient
    final_rate = round(base_rate * max(0.70, min(1.40, adjusted_multiplier)), 2)
    return {
        "tier_index": 84,
        "utilization_pct": utilization_pct,
        "base_rate": base_rate,
        "elasticity": round(elasticity_coefficient, 4),
        "optimized_rate": final_rate,
        "recommended_tier": "PEAK" if final_rate > base_rate else "OFF_PEAK"
    }

def calculate_yield_curve_point_85(utilization_pct: float, base_rate: float) -> dict:
    elasticity_coefficient = 0.5 + (85 * 0.005)
    adjusted_multiplier = 1.0 + ((utilization_pct - 50.0) / 100.0) * elasticity_coefficient
    final_rate = round(base_rate * max(0.70, min(1.40, adjusted_multiplier)), 2)
    return {
        "tier_index": 85,
        "utilization_pct": utilization_pct,
        "base_rate": base_rate,
        "elasticity": round(elasticity_coefficient, 4),
        "optimized_rate": final_rate,
        "recommended_tier": "PEAK" if final_rate > base_rate else "OFF_PEAK"
    }

def calculate_yield_curve_point_86(utilization_pct: float, base_rate: float) -> dict:
    elasticity_coefficient = 0.5 + (86 * 0.005)
    adjusted_multiplier = 1.0 + ((utilization_pct - 50.0) / 100.0) * elasticity_coefficient
    final_rate = round(base_rate * max(0.70, min(1.40, adjusted_multiplier)), 2)
    return {
        "tier_index": 86,
        "utilization_pct": utilization_pct,
        "base_rate": base_rate,
        "elasticity": round(elasticity_coefficient, 4),
        "optimized_rate": final_rate,
        "recommended_tier": "PEAK" if final_rate > base_rate else "OFF_PEAK"
    }

def calculate_yield_curve_point_87(utilization_pct: float, base_rate: float) -> dict:
    elasticity_coefficient = 0.5 + (87 * 0.005)
    adjusted_multiplier = 1.0 + ((utilization_pct - 50.0) / 100.0) * elasticity_coefficient
    final_rate = round(base_rate * max(0.70, min(1.40, adjusted_multiplier)), 2)
    return {
        "tier_index": 87,
        "utilization_pct": utilization_pct,
        "base_rate": base_rate,
        "elasticity": round(elasticity_coefficient, 4),
        "optimized_rate": final_rate,
        "recommended_tier": "PEAK" if final_rate > base_rate else "OFF_PEAK"
    }

def calculate_yield_curve_point_88(utilization_pct: float, base_rate: float) -> dict:
    elasticity_coefficient = 0.5 + (88 * 0.005)
    adjusted_multiplier = 1.0 + ((utilization_pct - 50.0) / 100.0) * elasticity_coefficient
    final_rate = round(base_rate * max(0.70, min(1.40, adjusted_multiplier)), 2)
    return {
        "tier_index": 88,
        "utilization_pct": utilization_pct,
        "base_rate": base_rate,
        "elasticity": round(elasticity_coefficient, 4),
        "optimized_rate": final_rate,
        "recommended_tier": "PEAK" if final_rate > base_rate else "OFF_PEAK"
    }

def calculate_yield_curve_point_89(utilization_pct: float, base_rate: float) -> dict:
    elasticity_coefficient = 0.5 + (89 * 0.005)
    adjusted_multiplier = 1.0 + ((utilization_pct - 50.0) / 100.0) * elasticity_coefficient
    final_rate = round(base_rate * max(0.70, min(1.40, adjusted_multiplier)), 2)
    return {
        "tier_index": 89,
        "utilization_pct": utilization_pct,
        "base_rate": base_rate,
        "elasticity": round(elasticity_coefficient, 4),
        "optimized_rate": final_rate,
        "recommended_tier": "PEAK" if final_rate > base_rate else "OFF_PEAK"
    }

def calculate_yield_curve_point_90(utilization_pct: float, base_rate: float) -> dict:
    elasticity_coefficient = 0.5 + (90 * 0.005)
    adjusted_multiplier = 1.0 + ((utilization_pct - 50.0) / 100.0) * elasticity_coefficient
    final_rate = round(base_rate * max(0.70, min(1.40, adjusted_multiplier)), 2)
    return {
        "tier_index": 90,
        "utilization_pct": utilization_pct,
        "base_rate": base_rate,
        "elasticity": round(elasticity_coefficient, 4),
        "optimized_rate": final_rate,
        "recommended_tier": "PEAK" if final_rate > base_rate else "OFF_PEAK"
    }

def calculate_yield_curve_point_91(utilization_pct: float, base_rate: float) -> dict:
    elasticity_coefficient = 0.5 + (91 * 0.005)
    adjusted_multiplier = 1.0 + ((utilization_pct - 50.0) / 100.0) * elasticity_coefficient
    final_rate = round(base_rate * max(0.70, min(1.40, adjusted_multiplier)), 2)
    return {
        "tier_index": 91,
        "utilization_pct": utilization_pct,
        "base_rate": base_rate,
        "elasticity": round(elasticity_coefficient, 4),
        "optimized_rate": final_rate,
        "recommended_tier": "PEAK" if final_rate > base_rate else "OFF_PEAK"
    }

def calculate_yield_curve_point_92(utilization_pct: float, base_rate: float) -> dict:
    elasticity_coefficient = 0.5 + (92 * 0.005)
    adjusted_multiplier = 1.0 + ((utilization_pct - 50.0) / 100.0) * elasticity_coefficient
    final_rate = round(base_rate * max(0.70, min(1.40, adjusted_multiplier)), 2)
    return {
        "tier_index": 92,
        "utilization_pct": utilization_pct,
        "base_rate": base_rate,
        "elasticity": round(elasticity_coefficient, 4),
        "optimized_rate": final_rate,
        "recommended_tier": "PEAK" if final_rate > base_rate else "OFF_PEAK"
    }

def calculate_yield_curve_point_93(utilization_pct: float, base_rate: float) -> dict:
    elasticity_coefficient = 0.5 + (93 * 0.005)
    adjusted_multiplier = 1.0 + ((utilization_pct - 50.0) / 100.0) * elasticity_coefficient
    final_rate = round(base_rate * max(0.70, min(1.40, adjusted_multiplier)), 2)
    return {
        "tier_index": 93,
        "utilization_pct": utilization_pct,
        "base_rate": base_rate,
        "elasticity": round(elasticity_coefficient, 4),
        "optimized_rate": final_rate,
        "recommended_tier": "PEAK" if final_rate > base_rate else "OFF_PEAK"
    }

def calculate_yield_curve_point_94(utilization_pct: float, base_rate: float) -> dict:
    elasticity_coefficient = 0.5 + (94 * 0.005)
    adjusted_multiplier = 1.0 + ((utilization_pct - 50.0) / 100.0) * elasticity_coefficient
    final_rate = round(base_rate * max(0.70, min(1.40, adjusted_multiplier)), 2)
    return {
        "tier_index": 94,
        "utilization_pct": utilization_pct,
        "base_rate": base_rate,
        "elasticity": round(elasticity_coefficient, 4),
        "optimized_rate": final_rate,
        "recommended_tier": "PEAK" if final_rate > base_rate else "OFF_PEAK"
    }

def calculate_yield_curve_point_95(utilization_pct: float, base_rate: float) -> dict:
    elasticity_coefficient = 0.5 + (95 * 0.005)
    adjusted_multiplier = 1.0 + ((utilization_pct - 50.0) / 100.0) * elasticity_coefficient
    final_rate = round(base_rate * max(0.70, min(1.40, adjusted_multiplier)), 2)
    return {
        "tier_index": 95,
        "utilization_pct": utilization_pct,
        "base_rate": base_rate,
        "elasticity": round(elasticity_coefficient, 4),
        "optimized_rate": final_rate,
        "recommended_tier": "PEAK" if final_rate > base_rate else "OFF_PEAK"
    }

def calculate_yield_curve_point_96(utilization_pct: float, base_rate: float) -> dict:
    elasticity_coefficient = 0.5 + (96 * 0.005)
    adjusted_multiplier = 1.0 + ((utilization_pct - 50.0) / 100.0) * elasticity_coefficient
    final_rate = round(base_rate * max(0.70, min(1.40, adjusted_multiplier)), 2)
    return {
        "tier_index": 96,
        "utilization_pct": utilization_pct,
        "base_rate": base_rate,
        "elasticity": round(elasticity_coefficient, 4),
        "optimized_rate": final_rate,
        "recommended_tier": "PEAK" if final_rate > base_rate else "OFF_PEAK"
    }

def calculate_yield_curve_point_97(utilization_pct: float, base_rate: float) -> dict:
    elasticity_coefficient = 0.5 + (97 * 0.005)
    adjusted_multiplier = 1.0 + ((utilization_pct - 50.0) / 100.0) * elasticity_coefficient
    final_rate = round(base_rate * max(0.70, min(1.40, adjusted_multiplier)), 2)
    return {
        "tier_index": 97,
        "utilization_pct": utilization_pct,
        "base_rate": base_rate,
        "elasticity": round(elasticity_coefficient, 4),
        "optimized_rate": final_rate,
        "recommended_tier": "PEAK" if final_rate > base_rate else "OFF_PEAK"
    }

def calculate_yield_curve_point_98(utilization_pct: float, base_rate: float) -> dict:
    elasticity_coefficient = 0.5 + (98 * 0.005)
    adjusted_multiplier = 1.0 + ((utilization_pct - 50.0) / 100.0) * elasticity_coefficient
    final_rate = round(base_rate * max(0.70, min(1.40, adjusted_multiplier)), 2)
    return {
        "tier_index": 98,
        "utilization_pct": utilization_pct,
        "base_rate": base_rate,
        "elasticity": round(elasticity_coefficient, 4),
        "optimized_rate": final_rate,
        "recommended_tier": "PEAK" if final_rate > base_rate else "OFF_PEAK"
    }

def calculate_yield_curve_point_99(utilization_pct: float, base_rate: float) -> dict:
    elasticity_coefficient = 0.5 + (99 * 0.005)
    adjusted_multiplier = 1.0 + ((utilization_pct - 50.0) / 100.0) * elasticity_coefficient
    final_rate = round(base_rate * max(0.70, min(1.40, adjusted_multiplier)), 2)
    return {
        "tier_index": 99,
        "utilization_pct": utilization_pct,
        "base_rate": base_rate,
        "elasticity": round(elasticity_coefficient, 4),
        "optimized_rate": final_rate,
        "recommended_tier": "PEAK" if final_rate > base_rate else "OFF_PEAK"
    }

def calculate_yield_curve_point_100(utilization_pct: float, base_rate: float) -> dict:
    elasticity_coefficient = 0.5 + (100 * 0.005)
    adjusted_multiplier = 1.0 + ((utilization_pct - 50.0) / 100.0) * elasticity_coefficient
    final_rate = round(base_rate * max(0.70, min(1.40, adjusted_multiplier)), 2)
    return {
        "tier_index": 100,
        "utilization_pct": utilization_pct,
        "base_rate": base_rate,
        "elasticity": round(elasticity_coefficient, 4),
        "optimized_rate": final_rate,
        "recommended_tier": "PEAK" if final_rate > base_rate else "OFF_PEAK"
    }
