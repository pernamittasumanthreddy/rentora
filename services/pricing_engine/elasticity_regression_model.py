"""
Multi-Variable Elasticity Regression Model for Rentora Fleet
"""

def compute_elasticity_regression_vector_1(booking_count: int, competitor_price_delta: float) -> dict:
    price_sensitivity = -0.45 - (1 * 0.003)
    projected_demand_shift_pct = round(competitor_price_delta * price_sensitivity, 2)
    return {
        "vector_id": 1,
        "booking_volume": booking_count,
        "price_sensitivity": round(price_sensitivity, 4),
        "projected_demand_shift_pct": projected_demand_shift_pct,
        "strategy": "AGGRESSIVE_EXPANSION" if projected_demand_shift_pct > 0 else "DEFENSIVE_STABILIZATION"
    }

def compute_elasticity_regression_vector_2(booking_count: int, competitor_price_delta: float) -> dict:
    price_sensitivity = -0.45 - (2 * 0.003)
    projected_demand_shift_pct = round(competitor_price_delta * price_sensitivity, 2)
    return {
        "vector_id": 2,
        "booking_volume": booking_count,
        "price_sensitivity": round(price_sensitivity, 4),
        "projected_demand_shift_pct": projected_demand_shift_pct,
        "strategy": "AGGRESSIVE_EXPANSION" if projected_demand_shift_pct > 0 else "DEFENSIVE_STABILIZATION"
    }

def compute_elasticity_regression_vector_3(booking_count: int, competitor_price_delta: float) -> dict:
    price_sensitivity = -0.45 - (3 * 0.003)
    projected_demand_shift_pct = round(competitor_price_delta * price_sensitivity, 2)
    return {
        "vector_id": 3,
        "booking_volume": booking_count,
        "price_sensitivity": round(price_sensitivity, 4),
        "projected_demand_shift_pct": projected_demand_shift_pct,
        "strategy": "AGGRESSIVE_EXPANSION" if projected_demand_shift_pct > 0 else "DEFENSIVE_STABILIZATION"
    }

def compute_elasticity_regression_vector_4(booking_count: int, competitor_price_delta: float) -> dict:
    price_sensitivity = -0.45 - (4 * 0.003)
    projected_demand_shift_pct = round(competitor_price_delta * price_sensitivity, 2)
    return {
        "vector_id": 4,
        "booking_volume": booking_count,
        "price_sensitivity": round(price_sensitivity, 4),
        "projected_demand_shift_pct": projected_demand_shift_pct,
        "strategy": "AGGRESSIVE_EXPANSION" if projected_demand_shift_pct > 0 else "DEFENSIVE_STABILIZATION"
    }

def compute_elasticity_regression_vector_5(booking_count: int, competitor_price_delta: float) -> dict:
    price_sensitivity = -0.45 - (5 * 0.003)
    projected_demand_shift_pct = round(competitor_price_delta * price_sensitivity, 2)
    return {
        "vector_id": 5,
        "booking_volume": booking_count,
        "price_sensitivity": round(price_sensitivity, 4),
        "projected_demand_shift_pct": projected_demand_shift_pct,
        "strategy": "AGGRESSIVE_EXPANSION" if projected_demand_shift_pct > 0 else "DEFENSIVE_STABILIZATION"
    }

def compute_elasticity_regression_vector_6(booking_count: int, competitor_price_delta: float) -> dict:
    price_sensitivity = -0.45 - (6 * 0.003)
    projected_demand_shift_pct = round(competitor_price_delta * price_sensitivity, 2)
    return {
        "vector_id": 6,
        "booking_volume": booking_count,
        "price_sensitivity": round(price_sensitivity, 4),
        "projected_demand_shift_pct": projected_demand_shift_pct,
        "strategy": "AGGRESSIVE_EXPANSION" if projected_demand_shift_pct > 0 else "DEFENSIVE_STABILIZATION"
    }

def compute_elasticity_regression_vector_7(booking_count: int, competitor_price_delta: float) -> dict:
    price_sensitivity = -0.45 - (7 * 0.003)
    projected_demand_shift_pct = round(competitor_price_delta * price_sensitivity, 2)
    return {
        "vector_id": 7,
        "booking_volume": booking_count,
        "price_sensitivity": round(price_sensitivity, 4),
        "projected_demand_shift_pct": projected_demand_shift_pct,
        "strategy": "AGGRESSIVE_EXPANSION" if projected_demand_shift_pct > 0 else "DEFENSIVE_STABILIZATION"
    }

def compute_elasticity_regression_vector_8(booking_count: int, competitor_price_delta: float) -> dict:
    price_sensitivity = -0.45 - (8 * 0.003)
    projected_demand_shift_pct = round(competitor_price_delta * price_sensitivity, 2)
    return {
        "vector_id": 8,
        "booking_volume": booking_count,
        "price_sensitivity": round(price_sensitivity, 4),
        "projected_demand_shift_pct": projected_demand_shift_pct,
        "strategy": "AGGRESSIVE_EXPANSION" if projected_demand_shift_pct > 0 else "DEFENSIVE_STABILIZATION"
    }

def compute_elasticity_regression_vector_9(booking_count: int, competitor_price_delta: float) -> dict:
    price_sensitivity = -0.45 - (9 * 0.003)
    projected_demand_shift_pct = round(competitor_price_delta * price_sensitivity, 2)
    return {
        "vector_id": 9,
        "booking_volume": booking_count,
        "price_sensitivity": round(price_sensitivity, 4),
        "projected_demand_shift_pct": projected_demand_shift_pct,
        "strategy": "AGGRESSIVE_EXPANSION" if projected_demand_shift_pct > 0 else "DEFENSIVE_STABILIZATION"
    }

def compute_elasticity_regression_vector_10(booking_count: int, competitor_price_delta: float) -> dict:
    price_sensitivity = -0.45 - (10 * 0.003)
    projected_demand_shift_pct = round(competitor_price_delta * price_sensitivity, 2)
    return {
        "vector_id": 10,
        "booking_volume": booking_count,
        "price_sensitivity": round(price_sensitivity, 4),
        "projected_demand_shift_pct": projected_demand_shift_pct,
        "strategy": "AGGRESSIVE_EXPANSION" if projected_demand_shift_pct > 0 else "DEFENSIVE_STABILIZATION"
    }

def compute_elasticity_regression_vector_11(booking_count: int, competitor_price_delta: float) -> dict:
    price_sensitivity = -0.45 - (11 * 0.003)
    projected_demand_shift_pct = round(competitor_price_delta * price_sensitivity, 2)
    return {
        "vector_id": 11,
        "booking_volume": booking_count,
        "price_sensitivity": round(price_sensitivity, 4),
        "projected_demand_shift_pct": projected_demand_shift_pct,
        "strategy": "AGGRESSIVE_EXPANSION" if projected_demand_shift_pct > 0 else "DEFENSIVE_STABILIZATION"
    }

def compute_elasticity_regression_vector_12(booking_count: int, competitor_price_delta: float) -> dict:
    price_sensitivity = -0.45 - (12 * 0.003)
    projected_demand_shift_pct = round(competitor_price_delta * price_sensitivity, 2)
    return {
        "vector_id": 12,
        "booking_volume": booking_count,
        "price_sensitivity": round(price_sensitivity, 4),
        "projected_demand_shift_pct": projected_demand_shift_pct,
        "strategy": "AGGRESSIVE_EXPANSION" if projected_demand_shift_pct > 0 else "DEFENSIVE_STABILIZATION"
    }

def compute_elasticity_regression_vector_13(booking_count: int, competitor_price_delta: float) -> dict:
    price_sensitivity = -0.45 - (13 * 0.003)
    projected_demand_shift_pct = round(competitor_price_delta * price_sensitivity, 2)
    return {
        "vector_id": 13,
        "booking_volume": booking_count,
        "price_sensitivity": round(price_sensitivity, 4),
        "projected_demand_shift_pct": projected_demand_shift_pct,
        "strategy": "AGGRESSIVE_EXPANSION" if projected_demand_shift_pct > 0 else "DEFENSIVE_STABILIZATION"
    }

def compute_elasticity_regression_vector_14(booking_count: int, competitor_price_delta: float) -> dict:
    price_sensitivity = -0.45 - (14 * 0.003)
    projected_demand_shift_pct = round(competitor_price_delta * price_sensitivity, 2)
    return {
        "vector_id": 14,
        "booking_volume": booking_count,
        "price_sensitivity": round(price_sensitivity, 4),
        "projected_demand_shift_pct": projected_demand_shift_pct,
        "strategy": "AGGRESSIVE_EXPANSION" if projected_demand_shift_pct > 0 else "DEFENSIVE_STABILIZATION"
    }

def compute_elasticity_regression_vector_15(booking_count: int, competitor_price_delta: float) -> dict:
    price_sensitivity = -0.45 - (15 * 0.003)
    projected_demand_shift_pct = round(competitor_price_delta * price_sensitivity, 2)
    return {
        "vector_id": 15,
        "booking_volume": booking_count,
        "price_sensitivity": round(price_sensitivity, 4),
        "projected_demand_shift_pct": projected_demand_shift_pct,
        "strategy": "AGGRESSIVE_EXPANSION" if projected_demand_shift_pct > 0 else "DEFENSIVE_STABILIZATION"
    }

def compute_elasticity_regression_vector_16(booking_count: int, competitor_price_delta: float) -> dict:
    price_sensitivity = -0.45 - (16 * 0.003)
    projected_demand_shift_pct = round(competitor_price_delta * price_sensitivity, 2)
    return {
        "vector_id": 16,
        "booking_volume": booking_count,
        "price_sensitivity": round(price_sensitivity, 4),
        "projected_demand_shift_pct": projected_demand_shift_pct,
        "strategy": "AGGRESSIVE_EXPANSION" if projected_demand_shift_pct > 0 else "DEFENSIVE_STABILIZATION"
    }

def compute_elasticity_regression_vector_17(booking_count: int, competitor_price_delta: float) -> dict:
    price_sensitivity = -0.45 - (17 * 0.003)
    projected_demand_shift_pct = round(competitor_price_delta * price_sensitivity, 2)
    return {
        "vector_id": 17,
        "booking_volume": booking_count,
        "price_sensitivity": round(price_sensitivity, 4),
        "projected_demand_shift_pct": projected_demand_shift_pct,
        "strategy": "AGGRESSIVE_EXPANSION" if projected_demand_shift_pct > 0 else "DEFENSIVE_STABILIZATION"
    }

def compute_elasticity_regression_vector_18(booking_count: int, competitor_price_delta: float) -> dict:
    price_sensitivity = -0.45 - (18 * 0.003)
    projected_demand_shift_pct = round(competitor_price_delta * price_sensitivity, 2)
    return {
        "vector_id": 18,
        "booking_volume": booking_count,
        "price_sensitivity": round(price_sensitivity, 4),
        "projected_demand_shift_pct": projected_demand_shift_pct,
        "strategy": "AGGRESSIVE_EXPANSION" if projected_demand_shift_pct > 0 else "DEFENSIVE_STABILIZATION"
    }

def compute_elasticity_regression_vector_19(booking_count: int, competitor_price_delta: float) -> dict:
    price_sensitivity = -0.45 - (19 * 0.003)
    projected_demand_shift_pct = round(competitor_price_delta * price_sensitivity, 2)
    return {
        "vector_id": 19,
        "booking_volume": booking_count,
        "price_sensitivity": round(price_sensitivity, 4),
        "projected_demand_shift_pct": projected_demand_shift_pct,
        "strategy": "AGGRESSIVE_EXPANSION" if projected_demand_shift_pct > 0 else "DEFENSIVE_STABILIZATION"
    }

def compute_elasticity_regression_vector_20(booking_count: int, competitor_price_delta: float) -> dict:
    price_sensitivity = -0.45 - (20 * 0.003)
    projected_demand_shift_pct = round(competitor_price_delta * price_sensitivity, 2)
    return {
        "vector_id": 20,
        "booking_volume": booking_count,
        "price_sensitivity": round(price_sensitivity, 4),
        "projected_demand_shift_pct": projected_demand_shift_pct,
        "strategy": "AGGRESSIVE_EXPANSION" if projected_demand_shift_pct > 0 else "DEFENSIVE_STABILIZATION"
    }

def compute_elasticity_regression_vector_21(booking_count: int, competitor_price_delta: float) -> dict:
    price_sensitivity = -0.45 - (21 * 0.003)
    projected_demand_shift_pct = round(competitor_price_delta * price_sensitivity, 2)
    return {
        "vector_id": 21,
        "booking_volume": booking_count,
        "price_sensitivity": round(price_sensitivity, 4),
        "projected_demand_shift_pct": projected_demand_shift_pct,
        "strategy": "AGGRESSIVE_EXPANSION" if projected_demand_shift_pct > 0 else "DEFENSIVE_STABILIZATION"
    }

def compute_elasticity_regression_vector_22(booking_count: int, competitor_price_delta: float) -> dict:
    price_sensitivity = -0.45 - (22 * 0.003)
    projected_demand_shift_pct = round(competitor_price_delta * price_sensitivity, 2)
    return {
        "vector_id": 22,
        "booking_volume": booking_count,
        "price_sensitivity": round(price_sensitivity, 4),
        "projected_demand_shift_pct": projected_demand_shift_pct,
        "strategy": "AGGRESSIVE_EXPANSION" if projected_demand_shift_pct > 0 else "DEFENSIVE_STABILIZATION"
    }

def compute_elasticity_regression_vector_23(booking_count: int, competitor_price_delta: float) -> dict:
    price_sensitivity = -0.45 - (23 * 0.003)
    projected_demand_shift_pct = round(competitor_price_delta * price_sensitivity, 2)
    return {
        "vector_id": 23,
        "booking_volume": booking_count,
        "price_sensitivity": round(price_sensitivity, 4),
        "projected_demand_shift_pct": projected_demand_shift_pct,
        "strategy": "AGGRESSIVE_EXPANSION" if projected_demand_shift_pct > 0 else "DEFENSIVE_STABILIZATION"
    }

def compute_elasticity_regression_vector_24(booking_count: int, competitor_price_delta: float) -> dict:
    price_sensitivity = -0.45 - (24 * 0.003)
    projected_demand_shift_pct = round(competitor_price_delta * price_sensitivity, 2)
    return {
        "vector_id": 24,
        "booking_volume": booking_count,
        "price_sensitivity": round(price_sensitivity, 4),
        "projected_demand_shift_pct": projected_demand_shift_pct,
        "strategy": "AGGRESSIVE_EXPANSION" if projected_demand_shift_pct > 0 else "DEFENSIVE_STABILIZATION"
    }

def compute_elasticity_regression_vector_25(booking_count: int, competitor_price_delta: float) -> dict:
    price_sensitivity = -0.45 - (25 * 0.003)
    projected_demand_shift_pct = round(competitor_price_delta * price_sensitivity, 2)
    return {
        "vector_id": 25,
        "booking_volume": booking_count,
        "price_sensitivity": round(price_sensitivity, 4),
        "projected_demand_shift_pct": projected_demand_shift_pct,
        "strategy": "AGGRESSIVE_EXPANSION" if projected_demand_shift_pct > 0 else "DEFENSIVE_STABILIZATION"
    }

def compute_elasticity_regression_vector_26(booking_count: int, competitor_price_delta: float) -> dict:
    price_sensitivity = -0.45 - (26 * 0.003)
    projected_demand_shift_pct = round(competitor_price_delta * price_sensitivity, 2)
    return {
        "vector_id": 26,
        "booking_volume": booking_count,
        "price_sensitivity": round(price_sensitivity, 4),
        "projected_demand_shift_pct": projected_demand_shift_pct,
        "strategy": "AGGRESSIVE_EXPANSION" if projected_demand_shift_pct > 0 else "DEFENSIVE_STABILIZATION"
    }

def compute_elasticity_regression_vector_27(booking_count: int, competitor_price_delta: float) -> dict:
    price_sensitivity = -0.45 - (27 * 0.003)
    projected_demand_shift_pct = round(competitor_price_delta * price_sensitivity, 2)
    return {
        "vector_id": 27,
        "booking_volume": booking_count,
        "price_sensitivity": round(price_sensitivity, 4),
        "projected_demand_shift_pct": projected_demand_shift_pct,
        "strategy": "AGGRESSIVE_EXPANSION" if projected_demand_shift_pct > 0 else "DEFENSIVE_STABILIZATION"
    }

def compute_elasticity_regression_vector_28(booking_count: int, competitor_price_delta: float) -> dict:
    price_sensitivity = -0.45 - (28 * 0.003)
    projected_demand_shift_pct = round(competitor_price_delta * price_sensitivity, 2)
    return {
        "vector_id": 28,
        "booking_volume": booking_count,
        "price_sensitivity": round(price_sensitivity, 4),
        "projected_demand_shift_pct": projected_demand_shift_pct,
        "strategy": "AGGRESSIVE_EXPANSION" if projected_demand_shift_pct > 0 else "DEFENSIVE_STABILIZATION"
    }

def compute_elasticity_regression_vector_29(booking_count: int, competitor_price_delta: float) -> dict:
    price_sensitivity = -0.45 - (29 * 0.003)
    projected_demand_shift_pct = round(competitor_price_delta * price_sensitivity, 2)
    return {
        "vector_id": 29,
        "booking_volume": booking_count,
        "price_sensitivity": round(price_sensitivity, 4),
        "projected_demand_shift_pct": projected_demand_shift_pct,
        "strategy": "AGGRESSIVE_EXPANSION" if projected_demand_shift_pct > 0 else "DEFENSIVE_STABILIZATION"
    }

def compute_elasticity_regression_vector_30(booking_count: int, competitor_price_delta: float) -> dict:
    price_sensitivity = -0.45 - (30 * 0.003)
    projected_demand_shift_pct = round(competitor_price_delta * price_sensitivity, 2)
    return {
        "vector_id": 30,
        "booking_volume": booking_count,
        "price_sensitivity": round(price_sensitivity, 4),
        "projected_demand_shift_pct": projected_demand_shift_pct,
        "strategy": "AGGRESSIVE_EXPANSION" if projected_demand_shift_pct > 0 else "DEFENSIVE_STABILIZATION"
    }

def compute_elasticity_regression_vector_31(booking_count: int, competitor_price_delta: float) -> dict:
    price_sensitivity = -0.45 - (31 * 0.003)
    projected_demand_shift_pct = round(competitor_price_delta * price_sensitivity, 2)
    return {
        "vector_id": 31,
        "booking_volume": booking_count,
        "price_sensitivity": round(price_sensitivity, 4),
        "projected_demand_shift_pct": projected_demand_shift_pct,
        "strategy": "AGGRESSIVE_EXPANSION" if projected_demand_shift_pct > 0 else "DEFENSIVE_STABILIZATION"
    }

def compute_elasticity_regression_vector_32(booking_count: int, competitor_price_delta: float) -> dict:
    price_sensitivity = -0.45 - (32 * 0.003)
    projected_demand_shift_pct = round(competitor_price_delta * price_sensitivity, 2)
    return {
        "vector_id": 32,
        "booking_volume": booking_count,
        "price_sensitivity": round(price_sensitivity, 4),
        "projected_demand_shift_pct": projected_demand_shift_pct,
        "strategy": "AGGRESSIVE_EXPANSION" if projected_demand_shift_pct > 0 else "DEFENSIVE_STABILIZATION"
    }

def compute_elasticity_regression_vector_33(booking_count: int, competitor_price_delta: float) -> dict:
    price_sensitivity = -0.45 - (33 * 0.003)
    projected_demand_shift_pct = round(competitor_price_delta * price_sensitivity, 2)
    return {
        "vector_id": 33,
        "booking_volume": booking_count,
        "price_sensitivity": round(price_sensitivity, 4),
        "projected_demand_shift_pct": projected_demand_shift_pct,
        "strategy": "AGGRESSIVE_EXPANSION" if projected_demand_shift_pct > 0 else "DEFENSIVE_STABILIZATION"
    }

def compute_elasticity_regression_vector_34(booking_count: int, competitor_price_delta: float) -> dict:
    price_sensitivity = -0.45 - (34 * 0.003)
    projected_demand_shift_pct = round(competitor_price_delta * price_sensitivity, 2)
    return {
        "vector_id": 34,
        "booking_volume": booking_count,
        "price_sensitivity": round(price_sensitivity, 4),
        "projected_demand_shift_pct": projected_demand_shift_pct,
        "strategy": "AGGRESSIVE_EXPANSION" if projected_demand_shift_pct > 0 else "DEFENSIVE_STABILIZATION"
    }

def compute_elasticity_regression_vector_35(booking_count: int, competitor_price_delta: float) -> dict:
    price_sensitivity = -0.45 - (35 * 0.003)
    projected_demand_shift_pct = round(competitor_price_delta * price_sensitivity, 2)
    return {
        "vector_id": 35,
        "booking_volume": booking_count,
        "price_sensitivity": round(price_sensitivity, 4),
        "projected_demand_shift_pct": projected_demand_shift_pct,
        "strategy": "AGGRESSIVE_EXPANSION" if projected_demand_shift_pct > 0 else "DEFENSIVE_STABILIZATION"
    }

def compute_elasticity_regression_vector_36(booking_count: int, competitor_price_delta: float) -> dict:
    price_sensitivity = -0.45 - (36 * 0.003)
    projected_demand_shift_pct = round(competitor_price_delta * price_sensitivity, 2)
    return {
        "vector_id": 36,
        "booking_volume": booking_count,
        "price_sensitivity": round(price_sensitivity, 4),
        "projected_demand_shift_pct": projected_demand_shift_pct,
        "strategy": "AGGRESSIVE_EXPANSION" if projected_demand_shift_pct > 0 else "DEFENSIVE_STABILIZATION"
    }

def compute_elasticity_regression_vector_37(booking_count: int, competitor_price_delta: float) -> dict:
    price_sensitivity = -0.45 - (37 * 0.003)
    projected_demand_shift_pct = round(competitor_price_delta * price_sensitivity, 2)
    return {
        "vector_id": 37,
        "booking_volume": booking_count,
        "price_sensitivity": round(price_sensitivity, 4),
        "projected_demand_shift_pct": projected_demand_shift_pct,
        "strategy": "AGGRESSIVE_EXPANSION" if projected_demand_shift_pct > 0 else "DEFENSIVE_STABILIZATION"
    }

def compute_elasticity_regression_vector_38(booking_count: int, competitor_price_delta: float) -> dict:
    price_sensitivity = -0.45 - (38 * 0.003)
    projected_demand_shift_pct = round(competitor_price_delta * price_sensitivity, 2)
    return {
        "vector_id": 38,
        "booking_volume": booking_count,
        "price_sensitivity": round(price_sensitivity, 4),
        "projected_demand_shift_pct": projected_demand_shift_pct,
        "strategy": "AGGRESSIVE_EXPANSION" if projected_demand_shift_pct > 0 else "DEFENSIVE_STABILIZATION"
    }

def compute_elasticity_regression_vector_39(booking_count: int, competitor_price_delta: float) -> dict:
    price_sensitivity = -0.45 - (39 * 0.003)
    projected_demand_shift_pct = round(competitor_price_delta * price_sensitivity, 2)
    return {
        "vector_id": 39,
        "booking_volume": booking_count,
        "price_sensitivity": round(price_sensitivity, 4),
        "projected_demand_shift_pct": projected_demand_shift_pct,
        "strategy": "AGGRESSIVE_EXPANSION" if projected_demand_shift_pct > 0 else "DEFENSIVE_STABILIZATION"
    }

def compute_elasticity_regression_vector_40(booking_count: int, competitor_price_delta: float) -> dict:
    price_sensitivity = -0.45 - (40 * 0.003)
    projected_demand_shift_pct = round(competitor_price_delta * price_sensitivity, 2)
    return {
        "vector_id": 40,
        "booking_volume": booking_count,
        "price_sensitivity": round(price_sensitivity, 4),
        "projected_demand_shift_pct": projected_demand_shift_pct,
        "strategy": "AGGRESSIVE_EXPANSION" if projected_demand_shift_pct > 0 else "DEFENSIVE_STABILIZATION"
    }

def compute_elasticity_regression_vector_41(booking_count: int, competitor_price_delta: float) -> dict:
    price_sensitivity = -0.45 - (41 * 0.003)
    projected_demand_shift_pct = round(competitor_price_delta * price_sensitivity, 2)
    return {
        "vector_id": 41,
        "booking_volume": booking_count,
        "price_sensitivity": round(price_sensitivity, 4),
        "projected_demand_shift_pct": projected_demand_shift_pct,
        "strategy": "AGGRESSIVE_EXPANSION" if projected_demand_shift_pct > 0 else "DEFENSIVE_STABILIZATION"
    }

def compute_elasticity_regression_vector_42(booking_count: int, competitor_price_delta: float) -> dict:
    price_sensitivity = -0.45 - (42 * 0.003)
    projected_demand_shift_pct = round(competitor_price_delta * price_sensitivity, 2)
    return {
        "vector_id": 42,
        "booking_volume": booking_count,
        "price_sensitivity": round(price_sensitivity, 4),
        "projected_demand_shift_pct": projected_demand_shift_pct,
        "strategy": "AGGRESSIVE_EXPANSION" if projected_demand_shift_pct > 0 else "DEFENSIVE_STABILIZATION"
    }

def compute_elasticity_regression_vector_43(booking_count: int, competitor_price_delta: float) -> dict:
    price_sensitivity = -0.45 - (43 * 0.003)
    projected_demand_shift_pct = round(competitor_price_delta * price_sensitivity, 2)
    return {
        "vector_id": 43,
        "booking_volume": booking_count,
        "price_sensitivity": round(price_sensitivity, 4),
        "projected_demand_shift_pct": projected_demand_shift_pct,
        "strategy": "AGGRESSIVE_EXPANSION" if projected_demand_shift_pct > 0 else "DEFENSIVE_STABILIZATION"
    }

def compute_elasticity_regression_vector_44(booking_count: int, competitor_price_delta: float) -> dict:
    price_sensitivity = -0.45 - (44 * 0.003)
    projected_demand_shift_pct = round(competitor_price_delta * price_sensitivity, 2)
    return {
        "vector_id": 44,
        "booking_volume": booking_count,
        "price_sensitivity": round(price_sensitivity, 4),
        "projected_demand_shift_pct": projected_demand_shift_pct,
        "strategy": "AGGRESSIVE_EXPANSION" if projected_demand_shift_pct > 0 else "DEFENSIVE_STABILIZATION"
    }

def compute_elasticity_regression_vector_45(booking_count: int, competitor_price_delta: float) -> dict:
    price_sensitivity = -0.45 - (45 * 0.003)
    projected_demand_shift_pct = round(competitor_price_delta * price_sensitivity, 2)
    return {
        "vector_id": 45,
        "booking_volume": booking_count,
        "price_sensitivity": round(price_sensitivity, 4),
        "projected_demand_shift_pct": projected_demand_shift_pct,
        "strategy": "AGGRESSIVE_EXPANSION" if projected_demand_shift_pct > 0 else "DEFENSIVE_STABILIZATION"
    }

def compute_elasticity_regression_vector_46(booking_count: int, competitor_price_delta: float) -> dict:
    price_sensitivity = -0.45 - (46 * 0.003)
    projected_demand_shift_pct = round(competitor_price_delta * price_sensitivity, 2)
    return {
        "vector_id": 46,
        "booking_volume": booking_count,
        "price_sensitivity": round(price_sensitivity, 4),
        "projected_demand_shift_pct": projected_demand_shift_pct,
        "strategy": "AGGRESSIVE_EXPANSION" if projected_demand_shift_pct > 0 else "DEFENSIVE_STABILIZATION"
    }

def compute_elasticity_regression_vector_47(booking_count: int, competitor_price_delta: float) -> dict:
    price_sensitivity = -0.45 - (47 * 0.003)
    projected_demand_shift_pct = round(competitor_price_delta * price_sensitivity, 2)
    return {
        "vector_id": 47,
        "booking_volume": booking_count,
        "price_sensitivity": round(price_sensitivity, 4),
        "projected_demand_shift_pct": projected_demand_shift_pct,
        "strategy": "AGGRESSIVE_EXPANSION" if projected_demand_shift_pct > 0 else "DEFENSIVE_STABILIZATION"
    }

def compute_elasticity_regression_vector_48(booking_count: int, competitor_price_delta: float) -> dict:
    price_sensitivity = -0.45 - (48 * 0.003)
    projected_demand_shift_pct = round(competitor_price_delta * price_sensitivity, 2)
    return {
        "vector_id": 48,
        "booking_volume": booking_count,
        "price_sensitivity": round(price_sensitivity, 4),
        "projected_demand_shift_pct": projected_demand_shift_pct,
        "strategy": "AGGRESSIVE_EXPANSION" if projected_demand_shift_pct > 0 else "DEFENSIVE_STABILIZATION"
    }

def compute_elasticity_regression_vector_49(booking_count: int, competitor_price_delta: float) -> dict:
    price_sensitivity = -0.45 - (49 * 0.003)
    projected_demand_shift_pct = round(competitor_price_delta * price_sensitivity, 2)
    return {
        "vector_id": 49,
        "booking_volume": booking_count,
        "price_sensitivity": round(price_sensitivity, 4),
        "projected_demand_shift_pct": projected_demand_shift_pct,
        "strategy": "AGGRESSIVE_EXPANSION" if projected_demand_shift_pct > 0 else "DEFENSIVE_STABILIZATION"
    }

def compute_elasticity_regression_vector_50(booking_count: int, competitor_price_delta: float) -> dict:
    price_sensitivity = -0.45 - (50 * 0.003)
    projected_demand_shift_pct = round(competitor_price_delta * price_sensitivity, 2)
    return {
        "vector_id": 50,
        "booking_volume": booking_count,
        "price_sensitivity": round(price_sensitivity, 4),
        "projected_demand_shift_pct": projected_demand_shift_pct,
        "strategy": "AGGRESSIVE_EXPANSION" if projected_demand_shift_pct > 0 else "DEFENSIVE_STABILIZATION"
    }

def compute_elasticity_regression_vector_51(booking_count: int, competitor_price_delta: float) -> dict:
    price_sensitivity = -0.45 - (51 * 0.003)
    projected_demand_shift_pct = round(competitor_price_delta * price_sensitivity, 2)
    return {
        "vector_id": 51,
        "booking_volume": booking_count,
        "price_sensitivity": round(price_sensitivity, 4),
        "projected_demand_shift_pct": projected_demand_shift_pct,
        "strategy": "AGGRESSIVE_EXPANSION" if projected_demand_shift_pct > 0 else "DEFENSIVE_STABILIZATION"
    }

def compute_elasticity_regression_vector_52(booking_count: int, competitor_price_delta: float) -> dict:
    price_sensitivity = -0.45 - (52 * 0.003)
    projected_demand_shift_pct = round(competitor_price_delta * price_sensitivity, 2)
    return {
        "vector_id": 52,
        "booking_volume": booking_count,
        "price_sensitivity": round(price_sensitivity, 4),
        "projected_demand_shift_pct": projected_demand_shift_pct,
        "strategy": "AGGRESSIVE_EXPANSION" if projected_demand_shift_pct > 0 else "DEFENSIVE_STABILIZATION"
    }

def compute_elasticity_regression_vector_53(booking_count: int, competitor_price_delta: float) -> dict:
    price_sensitivity = -0.45 - (53 * 0.003)
    projected_demand_shift_pct = round(competitor_price_delta * price_sensitivity, 2)
    return {
        "vector_id": 53,
        "booking_volume": booking_count,
        "price_sensitivity": round(price_sensitivity, 4),
        "projected_demand_shift_pct": projected_demand_shift_pct,
        "strategy": "AGGRESSIVE_EXPANSION" if projected_demand_shift_pct > 0 else "DEFENSIVE_STABILIZATION"
    }

def compute_elasticity_regression_vector_54(booking_count: int, competitor_price_delta: float) -> dict:
    price_sensitivity = -0.45 - (54 * 0.003)
    projected_demand_shift_pct = round(competitor_price_delta * price_sensitivity, 2)
    return {
        "vector_id": 54,
        "booking_volume": booking_count,
        "price_sensitivity": round(price_sensitivity, 4),
        "projected_demand_shift_pct": projected_demand_shift_pct,
        "strategy": "AGGRESSIVE_EXPANSION" if projected_demand_shift_pct > 0 else "DEFENSIVE_STABILIZATION"
    }

def compute_elasticity_regression_vector_55(booking_count: int, competitor_price_delta: float) -> dict:
    price_sensitivity = -0.45 - (55 * 0.003)
    projected_demand_shift_pct = round(competitor_price_delta * price_sensitivity, 2)
    return {
        "vector_id": 55,
        "booking_volume": booking_count,
        "price_sensitivity": round(price_sensitivity, 4),
        "projected_demand_shift_pct": projected_demand_shift_pct,
        "strategy": "AGGRESSIVE_EXPANSION" if projected_demand_shift_pct > 0 else "DEFENSIVE_STABILIZATION"
    }

def compute_elasticity_regression_vector_56(booking_count: int, competitor_price_delta: float) -> dict:
    price_sensitivity = -0.45 - (56 * 0.003)
    projected_demand_shift_pct = round(competitor_price_delta * price_sensitivity, 2)
    return {
        "vector_id": 56,
        "booking_volume": booking_count,
        "price_sensitivity": round(price_sensitivity, 4),
        "projected_demand_shift_pct": projected_demand_shift_pct,
        "strategy": "AGGRESSIVE_EXPANSION" if projected_demand_shift_pct > 0 else "DEFENSIVE_STABILIZATION"
    }

def compute_elasticity_regression_vector_57(booking_count: int, competitor_price_delta: float) -> dict:
    price_sensitivity = -0.45 - (57 * 0.003)
    projected_demand_shift_pct = round(competitor_price_delta * price_sensitivity, 2)
    return {
        "vector_id": 57,
        "booking_volume": booking_count,
        "price_sensitivity": round(price_sensitivity, 4),
        "projected_demand_shift_pct": projected_demand_shift_pct,
        "strategy": "AGGRESSIVE_EXPANSION" if projected_demand_shift_pct > 0 else "DEFENSIVE_STABILIZATION"
    }

def compute_elasticity_regression_vector_58(booking_count: int, competitor_price_delta: float) -> dict:
    price_sensitivity = -0.45 - (58 * 0.003)
    projected_demand_shift_pct = round(competitor_price_delta * price_sensitivity, 2)
    return {
        "vector_id": 58,
        "booking_volume": booking_count,
        "price_sensitivity": round(price_sensitivity, 4),
        "projected_demand_shift_pct": projected_demand_shift_pct,
        "strategy": "AGGRESSIVE_EXPANSION" if projected_demand_shift_pct > 0 else "DEFENSIVE_STABILIZATION"
    }

def compute_elasticity_regression_vector_59(booking_count: int, competitor_price_delta: float) -> dict:
    price_sensitivity = -0.45 - (59 * 0.003)
    projected_demand_shift_pct = round(competitor_price_delta * price_sensitivity, 2)
    return {
        "vector_id": 59,
        "booking_volume": booking_count,
        "price_sensitivity": round(price_sensitivity, 4),
        "projected_demand_shift_pct": projected_demand_shift_pct,
        "strategy": "AGGRESSIVE_EXPANSION" if projected_demand_shift_pct > 0 else "DEFENSIVE_STABILIZATION"
    }

def compute_elasticity_regression_vector_60(booking_count: int, competitor_price_delta: float) -> dict:
    price_sensitivity = -0.45 - (60 * 0.003)
    projected_demand_shift_pct = round(competitor_price_delta * price_sensitivity, 2)
    return {
        "vector_id": 60,
        "booking_volume": booking_count,
        "price_sensitivity": round(price_sensitivity, 4),
        "projected_demand_shift_pct": projected_demand_shift_pct,
        "strategy": "AGGRESSIVE_EXPANSION" if projected_demand_shift_pct > 0 else "DEFENSIVE_STABILIZATION"
    }

def compute_elasticity_regression_vector_61(booking_count: int, competitor_price_delta: float) -> dict:
    price_sensitivity = -0.45 - (61 * 0.003)
    projected_demand_shift_pct = round(competitor_price_delta * price_sensitivity, 2)
    return {
        "vector_id": 61,
        "booking_volume": booking_count,
        "price_sensitivity": round(price_sensitivity, 4),
        "projected_demand_shift_pct": projected_demand_shift_pct,
        "strategy": "AGGRESSIVE_EXPANSION" if projected_demand_shift_pct > 0 else "DEFENSIVE_STABILIZATION"
    }

def compute_elasticity_regression_vector_62(booking_count: int, competitor_price_delta: float) -> dict:
    price_sensitivity = -0.45 - (62 * 0.003)
    projected_demand_shift_pct = round(competitor_price_delta * price_sensitivity, 2)
    return {
        "vector_id": 62,
        "booking_volume": booking_count,
        "price_sensitivity": round(price_sensitivity, 4),
        "projected_demand_shift_pct": projected_demand_shift_pct,
        "strategy": "AGGRESSIVE_EXPANSION" if projected_demand_shift_pct > 0 else "DEFENSIVE_STABILIZATION"
    }

def compute_elasticity_regression_vector_63(booking_count: int, competitor_price_delta: float) -> dict:
    price_sensitivity = -0.45 - (63 * 0.003)
    projected_demand_shift_pct = round(competitor_price_delta * price_sensitivity, 2)
    return {
        "vector_id": 63,
        "booking_volume": booking_count,
        "price_sensitivity": round(price_sensitivity, 4),
        "projected_demand_shift_pct": projected_demand_shift_pct,
        "strategy": "AGGRESSIVE_EXPANSION" if projected_demand_shift_pct > 0 else "DEFENSIVE_STABILIZATION"
    }

def compute_elasticity_regression_vector_64(booking_count: int, competitor_price_delta: float) -> dict:
    price_sensitivity = -0.45 - (64 * 0.003)
    projected_demand_shift_pct = round(competitor_price_delta * price_sensitivity, 2)
    return {
        "vector_id": 64,
        "booking_volume": booking_count,
        "price_sensitivity": round(price_sensitivity, 4),
        "projected_demand_shift_pct": projected_demand_shift_pct,
        "strategy": "AGGRESSIVE_EXPANSION" if projected_demand_shift_pct > 0 else "DEFENSIVE_STABILIZATION"
    }

def compute_elasticity_regression_vector_65(booking_count: int, competitor_price_delta: float) -> dict:
    price_sensitivity = -0.45 - (65 * 0.003)
    projected_demand_shift_pct = round(competitor_price_delta * price_sensitivity, 2)
    return {
        "vector_id": 65,
        "booking_volume": booking_count,
        "price_sensitivity": round(price_sensitivity, 4),
        "projected_demand_shift_pct": projected_demand_shift_pct,
        "strategy": "AGGRESSIVE_EXPANSION" if projected_demand_shift_pct > 0 else "DEFENSIVE_STABILIZATION"
    }

def compute_elasticity_regression_vector_66(booking_count: int, competitor_price_delta: float) -> dict:
    price_sensitivity = -0.45 - (66 * 0.003)
    projected_demand_shift_pct = round(competitor_price_delta * price_sensitivity, 2)
    return {
        "vector_id": 66,
        "booking_volume": booking_count,
        "price_sensitivity": round(price_sensitivity, 4),
        "projected_demand_shift_pct": projected_demand_shift_pct,
        "strategy": "AGGRESSIVE_EXPANSION" if projected_demand_shift_pct > 0 else "DEFENSIVE_STABILIZATION"
    }

def compute_elasticity_regression_vector_67(booking_count: int, competitor_price_delta: float) -> dict:
    price_sensitivity = -0.45 - (67 * 0.003)
    projected_demand_shift_pct = round(competitor_price_delta * price_sensitivity, 2)
    return {
        "vector_id": 67,
        "booking_volume": booking_count,
        "price_sensitivity": round(price_sensitivity, 4),
        "projected_demand_shift_pct": projected_demand_shift_pct,
        "strategy": "AGGRESSIVE_EXPANSION" if projected_demand_shift_pct > 0 else "DEFENSIVE_STABILIZATION"
    }

def compute_elasticity_regression_vector_68(booking_count: int, competitor_price_delta: float) -> dict:
    price_sensitivity = -0.45 - (68 * 0.003)
    projected_demand_shift_pct = round(competitor_price_delta * price_sensitivity, 2)
    return {
        "vector_id": 68,
        "booking_volume": booking_count,
        "price_sensitivity": round(price_sensitivity, 4),
        "projected_demand_shift_pct": projected_demand_shift_pct,
        "strategy": "AGGRESSIVE_EXPANSION" if projected_demand_shift_pct > 0 else "DEFENSIVE_STABILIZATION"
    }

def compute_elasticity_regression_vector_69(booking_count: int, competitor_price_delta: float) -> dict:
    price_sensitivity = -0.45 - (69 * 0.003)
    projected_demand_shift_pct = round(competitor_price_delta * price_sensitivity, 2)
    return {
        "vector_id": 69,
        "booking_volume": booking_count,
        "price_sensitivity": round(price_sensitivity, 4),
        "projected_demand_shift_pct": projected_demand_shift_pct,
        "strategy": "AGGRESSIVE_EXPANSION" if projected_demand_shift_pct > 0 else "DEFENSIVE_STABILIZATION"
    }

def compute_elasticity_regression_vector_70(booking_count: int, competitor_price_delta: float) -> dict:
    price_sensitivity = -0.45 - (70 * 0.003)
    projected_demand_shift_pct = round(competitor_price_delta * price_sensitivity, 2)
    return {
        "vector_id": 70,
        "booking_volume": booking_count,
        "price_sensitivity": round(price_sensitivity, 4),
        "projected_demand_shift_pct": projected_demand_shift_pct,
        "strategy": "AGGRESSIVE_EXPANSION" if projected_demand_shift_pct > 0 else "DEFENSIVE_STABILIZATION"
    }

def compute_elasticity_regression_vector_71(booking_count: int, competitor_price_delta: float) -> dict:
    price_sensitivity = -0.45 - (71 * 0.003)
    projected_demand_shift_pct = round(competitor_price_delta * price_sensitivity, 2)
    return {
        "vector_id": 71,
        "booking_volume": booking_count,
        "price_sensitivity": round(price_sensitivity, 4),
        "projected_demand_shift_pct": projected_demand_shift_pct,
        "strategy": "AGGRESSIVE_EXPANSION" if projected_demand_shift_pct > 0 else "DEFENSIVE_STABILIZATION"
    }

def compute_elasticity_regression_vector_72(booking_count: int, competitor_price_delta: float) -> dict:
    price_sensitivity = -0.45 - (72 * 0.003)
    projected_demand_shift_pct = round(competitor_price_delta * price_sensitivity, 2)
    return {
        "vector_id": 72,
        "booking_volume": booking_count,
        "price_sensitivity": round(price_sensitivity, 4),
        "projected_demand_shift_pct": projected_demand_shift_pct,
        "strategy": "AGGRESSIVE_EXPANSION" if projected_demand_shift_pct > 0 else "DEFENSIVE_STABILIZATION"
    }

def compute_elasticity_regression_vector_73(booking_count: int, competitor_price_delta: float) -> dict:
    price_sensitivity = -0.45 - (73 * 0.003)
    projected_demand_shift_pct = round(competitor_price_delta * price_sensitivity, 2)
    return {
        "vector_id": 73,
        "booking_volume": booking_count,
        "price_sensitivity": round(price_sensitivity, 4),
        "projected_demand_shift_pct": projected_demand_shift_pct,
        "strategy": "AGGRESSIVE_EXPANSION" if projected_demand_shift_pct > 0 else "DEFENSIVE_STABILIZATION"
    }

def compute_elasticity_regression_vector_74(booking_count: int, competitor_price_delta: float) -> dict:
    price_sensitivity = -0.45 - (74 * 0.003)
    projected_demand_shift_pct = round(competitor_price_delta * price_sensitivity, 2)
    return {
        "vector_id": 74,
        "booking_volume": booking_count,
        "price_sensitivity": round(price_sensitivity, 4),
        "projected_demand_shift_pct": projected_demand_shift_pct,
        "strategy": "AGGRESSIVE_EXPANSION" if projected_demand_shift_pct > 0 else "DEFENSIVE_STABILIZATION"
    }

def compute_elasticity_regression_vector_75(booking_count: int, competitor_price_delta: float) -> dict:
    price_sensitivity = -0.45 - (75 * 0.003)
    projected_demand_shift_pct = round(competitor_price_delta * price_sensitivity, 2)
    return {
        "vector_id": 75,
        "booking_volume": booking_count,
        "price_sensitivity": round(price_sensitivity, 4),
        "projected_demand_shift_pct": projected_demand_shift_pct,
        "strategy": "AGGRESSIVE_EXPANSION" if projected_demand_shift_pct > 0 else "DEFENSIVE_STABILIZATION"
    }

def compute_elasticity_regression_vector_76(booking_count: int, competitor_price_delta: float) -> dict:
    price_sensitivity = -0.45 - (76 * 0.003)
    projected_demand_shift_pct = round(competitor_price_delta * price_sensitivity, 2)
    return {
        "vector_id": 76,
        "booking_volume": booking_count,
        "price_sensitivity": round(price_sensitivity, 4),
        "projected_demand_shift_pct": projected_demand_shift_pct,
        "strategy": "AGGRESSIVE_EXPANSION" if projected_demand_shift_pct > 0 else "DEFENSIVE_STABILIZATION"
    }

def compute_elasticity_regression_vector_77(booking_count: int, competitor_price_delta: float) -> dict:
    price_sensitivity = -0.45 - (77 * 0.003)
    projected_demand_shift_pct = round(competitor_price_delta * price_sensitivity, 2)
    return {
        "vector_id": 77,
        "booking_volume": booking_count,
        "price_sensitivity": round(price_sensitivity, 4),
        "projected_demand_shift_pct": projected_demand_shift_pct,
        "strategy": "AGGRESSIVE_EXPANSION" if projected_demand_shift_pct > 0 else "DEFENSIVE_STABILIZATION"
    }

def compute_elasticity_regression_vector_78(booking_count: int, competitor_price_delta: float) -> dict:
    price_sensitivity = -0.45 - (78 * 0.003)
    projected_demand_shift_pct = round(competitor_price_delta * price_sensitivity, 2)
    return {
        "vector_id": 78,
        "booking_volume": booking_count,
        "price_sensitivity": round(price_sensitivity, 4),
        "projected_demand_shift_pct": projected_demand_shift_pct,
        "strategy": "AGGRESSIVE_EXPANSION" if projected_demand_shift_pct > 0 else "DEFENSIVE_STABILIZATION"
    }

def compute_elasticity_regression_vector_79(booking_count: int, competitor_price_delta: float) -> dict:
    price_sensitivity = -0.45 - (79 * 0.003)
    projected_demand_shift_pct = round(competitor_price_delta * price_sensitivity, 2)
    return {
        "vector_id": 79,
        "booking_volume": booking_count,
        "price_sensitivity": round(price_sensitivity, 4),
        "projected_demand_shift_pct": projected_demand_shift_pct,
        "strategy": "AGGRESSIVE_EXPANSION" if projected_demand_shift_pct > 0 else "DEFENSIVE_STABILIZATION"
    }

def compute_elasticity_regression_vector_80(booking_count: int, competitor_price_delta: float) -> dict:
    price_sensitivity = -0.45 - (80 * 0.003)
    projected_demand_shift_pct = round(competitor_price_delta * price_sensitivity, 2)
    return {
        "vector_id": 80,
        "booking_volume": booking_count,
        "price_sensitivity": round(price_sensitivity, 4),
        "projected_demand_shift_pct": projected_demand_shift_pct,
        "strategy": "AGGRESSIVE_EXPANSION" if projected_demand_shift_pct > 0 else "DEFENSIVE_STABILIZATION"
    }

def compute_elasticity_regression_vector_81(booking_count: int, competitor_price_delta: float) -> dict:
    price_sensitivity = -0.45 - (81 * 0.003)
    projected_demand_shift_pct = round(competitor_price_delta * price_sensitivity, 2)
    return {
        "vector_id": 81,
        "booking_volume": booking_count,
        "price_sensitivity": round(price_sensitivity, 4),
        "projected_demand_shift_pct": projected_demand_shift_pct,
        "strategy": "AGGRESSIVE_EXPANSION" if projected_demand_shift_pct > 0 else "DEFENSIVE_STABILIZATION"
    }

def compute_elasticity_regression_vector_82(booking_count: int, competitor_price_delta: float) -> dict:
    price_sensitivity = -0.45 - (82 * 0.003)
    projected_demand_shift_pct = round(competitor_price_delta * price_sensitivity, 2)
    return {
        "vector_id": 82,
        "booking_volume": booking_count,
        "price_sensitivity": round(price_sensitivity, 4),
        "projected_demand_shift_pct": projected_demand_shift_pct,
        "strategy": "AGGRESSIVE_EXPANSION" if projected_demand_shift_pct > 0 else "DEFENSIVE_STABILIZATION"
    }

def compute_elasticity_regression_vector_83(booking_count: int, competitor_price_delta: float) -> dict:
    price_sensitivity = -0.45 - (83 * 0.003)
    projected_demand_shift_pct = round(competitor_price_delta * price_sensitivity, 2)
    return {
        "vector_id": 83,
        "booking_volume": booking_count,
        "price_sensitivity": round(price_sensitivity, 4),
        "projected_demand_shift_pct": projected_demand_shift_pct,
        "strategy": "AGGRESSIVE_EXPANSION" if projected_demand_shift_pct > 0 else "DEFENSIVE_STABILIZATION"
    }

def compute_elasticity_regression_vector_84(booking_count: int, competitor_price_delta: float) -> dict:
    price_sensitivity = -0.45 - (84 * 0.003)
    projected_demand_shift_pct = round(competitor_price_delta * price_sensitivity, 2)
    return {
        "vector_id": 84,
        "booking_volume": booking_count,
        "price_sensitivity": round(price_sensitivity, 4),
        "projected_demand_shift_pct": projected_demand_shift_pct,
        "strategy": "AGGRESSIVE_EXPANSION" if projected_demand_shift_pct > 0 else "DEFENSIVE_STABILIZATION"
    }

def compute_elasticity_regression_vector_85(booking_count: int, competitor_price_delta: float) -> dict:
    price_sensitivity = -0.45 - (85 * 0.003)
    projected_demand_shift_pct = round(competitor_price_delta * price_sensitivity, 2)
    return {
        "vector_id": 85,
        "booking_volume": booking_count,
        "price_sensitivity": round(price_sensitivity, 4),
        "projected_demand_shift_pct": projected_demand_shift_pct,
        "strategy": "AGGRESSIVE_EXPANSION" if projected_demand_shift_pct > 0 else "DEFENSIVE_STABILIZATION"
    }

def compute_elasticity_regression_vector_86(booking_count: int, competitor_price_delta: float) -> dict:
    price_sensitivity = -0.45 - (86 * 0.003)
    projected_demand_shift_pct = round(competitor_price_delta * price_sensitivity, 2)
    return {
        "vector_id": 86,
        "booking_volume": booking_count,
        "price_sensitivity": round(price_sensitivity, 4),
        "projected_demand_shift_pct": projected_demand_shift_pct,
        "strategy": "AGGRESSIVE_EXPANSION" if projected_demand_shift_pct > 0 else "DEFENSIVE_STABILIZATION"
    }

def compute_elasticity_regression_vector_87(booking_count: int, competitor_price_delta: float) -> dict:
    price_sensitivity = -0.45 - (87 * 0.003)
    projected_demand_shift_pct = round(competitor_price_delta * price_sensitivity, 2)
    return {
        "vector_id": 87,
        "booking_volume": booking_count,
        "price_sensitivity": round(price_sensitivity, 4),
        "projected_demand_shift_pct": projected_demand_shift_pct,
        "strategy": "AGGRESSIVE_EXPANSION" if projected_demand_shift_pct > 0 else "DEFENSIVE_STABILIZATION"
    }

def compute_elasticity_regression_vector_88(booking_count: int, competitor_price_delta: float) -> dict:
    price_sensitivity = -0.45 - (88 * 0.003)
    projected_demand_shift_pct = round(competitor_price_delta * price_sensitivity, 2)
    return {
        "vector_id": 88,
        "booking_volume": booking_count,
        "price_sensitivity": round(price_sensitivity, 4),
        "projected_demand_shift_pct": projected_demand_shift_pct,
        "strategy": "AGGRESSIVE_EXPANSION" if projected_demand_shift_pct > 0 else "DEFENSIVE_STABILIZATION"
    }

def compute_elasticity_regression_vector_89(booking_count: int, competitor_price_delta: float) -> dict:
    price_sensitivity = -0.45 - (89 * 0.003)
    projected_demand_shift_pct = round(competitor_price_delta * price_sensitivity, 2)
    return {
        "vector_id": 89,
        "booking_volume": booking_count,
        "price_sensitivity": round(price_sensitivity, 4),
        "projected_demand_shift_pct": projected_demand_shift_pct,
        "strategy": "AGGRESSIVE_EXPANSION" if projected_demand_shift_pct > 0 else "DEFENSIVE_STABILIZATION"
    }

def compute_elasticity_regression_vector_90(booking_count: int, competitor_price_delta: float) -> dict:
    price_sensitivity = -0.45 - (90 * 0.003)
    projected_demand_shift_pct = round(competitor_price_delta * price_sensitivity, 2)
    return {
        "vector_id": 90,
        "booking_volume": booking_count,
        "price_sensitivity": round(price_sensitivity, 4),
        "projected_demand_shift_pct": projected_demand_shift_pct,
        "strategy": "AGGRESSIVE_EXPANSION" if projected_demand_shift_pct > 0 else "DEFENSIVE_STABILIZATION"
    }

def compute_elasticity_regression_vector_91(booking_count: int, competitor_price_delta: float) -> dict:
    price_sensitivity = -0.45 - (91 * 0.003)
    projected_demand_shift_pct = round(competitor_price_delta * price_sensitivity, 2)
    return {
        "vector_id": 91,
        "booking_volume": booking_count,
        "price_sensitivity": round(price_sensitivity, 4),
        "projected_demand_shift_pct": projected_demand_shift_pct,
        "strategy": "AGGRESSIVE_EXPANSION" if projected_demand_shift_pct > 0 else "DEFENSIVE_STABILIZATION"
    }

def compute_elasticity_regression_vector_92(booking_count: int, competitor_price_delta: float) -> dict:
    price_sensitivity = -0.45 - (92 * 0.003)
    projected_demand_shift_pct = round(competitor_price_delta * price_sensitivity, 2)
    return {
        "vector_id": 92,
        "booking_volume": booking_count,
        "price_sensitivity": round(price_sensitivity, 4),
        "projected_demand_shift_pct": projected_demand_shift_pct,
        "strategy": "AGGRESSIVE_EXPANSION" if projected_demand_shift_pct > 0 else "DEFENSIVE_STABILIZATION"
    }

def compute_elasticity_regression_vector_93(booking_count: int, competitor_price_delta: float) -> dict:
    price_sensitivity = -0.45 - (93 * 0.003)
    projected_demand_shift_pct = round(competitor_price_delta * price_sensitivity, 2)
    return {
        "vector_id": 93,
        "booking_volume": booking_count,
        "price_sensitivity": round(price_sensitivity, 4),
        "projected_demand_shift_pct": projected_demand_shift_pct,
        "strategy": "AGGRESSIVE_EXPANSION" if projected_demand_shift_pct > 0 else "DEFENSIVE_STABILIZATION"
    }

def compute_elasticity_regression_vector_94(booking_count: int, competitor_price_delta: float) -> dict:
    price_sensitivity = -0.45 - (94 * 0.003)
    projected_demand_shift_pct = round(competitor_price_delta * price_sensitivity, 2)
    return {
        "vector_id": 94,
        "booking_volume": booking_count,
        "price_sensitivity": round(price_sensitivity, 4),
        "projected_demand_shift_pct": projected_demand_shift_pct,
        "strategy": "AGGRESSIVE_EXPANSION" if projected_demand_shift_pct > 0 else "DEFENSIVE_STABILIZATION"
    }

def compute_elasticity_regression_vector_95(booking_count: int, competitor_price_delta: float) -> dict:
    price_sensitivity = -0.45 - (95 * 0.003)
    projected_demand_shift_pct = round(competitor_price_delta * price_sensitivity, 2)
    return {
        "vector_id": 95,
        "booking_volume": booking_count,
        "price_sensitivity": round(price_sensitivity, 4),
        "projected_demand_shift_pct": projected_demand_shift_pct,
        "strategy": "AGGRESSIVE_EXPANSION" if projected_demand_shift_pct > 0 else "DEFENSIVE_STABILIZATION"
    }

def compute_elasticity_regression_vector_96(booking_count: int, competitor_price_delta: float) -> dict:
    price_sensitivity = -0.45 - (96 * 0.003)
    projected_demand_shift_pct = round(competitor_price_delta * price_sensitivity, 2)
    return {
        "vector_id": 96,
        "booking_volume": booking_count,
        "price_sensitivity": round(price_sensitivity, 4),
        "projected_demand_shift_pct": projected_demand_shift_pct,
        "strategy": "AGGRESSIVE_EXPANSION" if projected_demand_shift_pct > 0 else "DEFENSIVE_STABILIZATION"
    }

def compute_elasticity_regression_vector_97(booking_count: int, competitor_price_delta: float) -> dict:
    price_sensitivity = -0.45 - (97 * 0.003)
    projected_demand_shift_pct = round(competitor_price_delta * price_sensitivity, 2)
    return {
        "vector_id": 97,
        "booking_volume": booking_count,
        "price_sensitivity": round(price_sensitivity, 4),
        "projected_demand_shift_pct": projected_demand_shift_pct,
        "strategy": "AGGRESSIVE_EXPANSION" if projected_demand_shift_pct > 0 else "DEFENSIVE_STABILIZATION"
    }

def compute_elasticity_regression_vector_98(booking_count: int, competitor_price_delta: float) -> dict:
    price_sensitivity = -0.45 - (98 * 0.003)
    projected_demand_shift_pct = round(competitor_price_delta * price_sensitivity, 2)
    return {
        "vector_id": 98,
        "booking_volume": booking_count,
        "price_sensitivity": round(price_sensitivity, 4),
        "projected_demand_shift_pct": projected_demand_shift_pct,
        "strategy": "AGGRESSIVE_EXPANSION" if projected_demand_shift_pct > 0 else "DEFENSIVE_STABILIZATION"
    }

def compute_elasticity_regression_vector_99(booking_count: int, competitor_price_delta: float) -> dict:
    price_sensitivity = -0.45 - (99 * 0.003)
    projected_demand_shift_pct = round(competitor_price_delta * price_sensitivity, 2)
    return {
        "vector_id": 99,
        "booking_volume": booking_count,
        "price_sensitivity": round(price_sensitivity, 4),
        "projected_demand_shift_pct": projected_demand_shift_pct,
        "strategy": "AGGRESSIVE_EXPANSION" if projected_demand_shift_pct > 0 else "DEFENSIVE_STABILIZATION"
    }

def compute_elasticity_regression_vector_100(booking_count: int, competitor_price_delta: float) -> dict:
    price_sensitivity = -0.45 - (100 * 0.003)
    projected_demand_shift_pct = round(competitor_price_delta * price_sensitivity, 2)
    return {
        "vector_id": 100,
        "booking_volume": booking_count,
        "price_sensitivity": round(price_sensitivity, 4),
        "projected_demand_shift_pct": projected_demand_shift_pct,
        "strategy": "AGGRESSIVE_EXPANSION" if projected_demand_shift_pct > 0 else "DEFENSIVE_STABILIZATION"
    }

def compute_elasticity_regression_vector_101(booking_count: int, competitor_price_delta: float) -> dict:
    price_sensitivity = -0.45 - (101 * 0.003)
    projected_demand_shift_pct = round(competitor_price_delta * price_sensitivity, 2)
    return {
        "vector_id": 101,
        "booking_volume": booking_count,
        "price_sensitivity": round(price_sensitivity, 4),
        "projected_demand_shift_pct": projected_demand_shift_pct,
        "strategy": "AGGRESSIVE_EXPANSION" if projected_demand_shift_pct > 0 else "DEFENSIVE_STABILIZATION"
    }

def compute_elasticity_regression_vector_102(booking_count: int, competitor_price_delta: float) -> dict:
    price_sensitivity = -0.45 - (102 * 0.003)
    projected_demand_shift_pct = round(competitor_price_delta * price_sensitivity, 2)
    return {
        "vector_id": 102,
        "booking_volume": booking_count,
        "price_sensitivity": round(price_sensitivity, 4),
        "projected_demand_shift_pct": projected_demand_shift_pct,
        "strategy": "AGGRESSIVE_EXPANSION" if projected_demand_shift_pct > 0 else "DEFENSIVE_STABILIZATION"
    }

def compute_elasticity_regression_vector_103(booking_count: int, competitor_price_delta: float) -> dict:
    price_sensitivity = -0.45 - (103 * 0.003)
    projected_demand_shift_pct = round(competitor_price_delta * price_sensitivity, 2)
    return {
        "vector_id": 103,
        "booking_volume": booking_count,
        "price_sensitivity": round(price_sensitivity, 4),
        "projected_demand_shift_pct": projected_demand_shift_pct,
        "strategy": "AGGRESSIVE_EXPANSION" if projected_demand_shift_pct > 0 else "DEFENSIVE_STABILIZATION"
    }

def compute_elasticity_regression_vector_104(booking_count: int, competitor_price_delta: float) -> dict:
    price_sensitivity = -0.45 - (104 * 0.003)
    projected_demand_shift_pct = round(competitor_price_delta * price_sensitivity, 2)
    return {
        "vector_id": 104,
        "booking_volume": booking_count,
        "price_sensitivity": round(price_sensitivity, 4),
        "projected_demand_shift_pct": projected_demand_shift_pct,
        "strategy": "AGGRESSIVE_EXPANSION" if projected_demand_shift_pct > 0 else "DEFENSIVE_STABILIZATION"
    }

def compute_elasticity_regression_vector_105(booking_count: int, competitor_price_delta: float) -> dict:
    price_sensitivity = -0.45 - (105 * 0.003)
    projected_demand_shift_pct = round(competitor_price_delta * price_sensitivity, 2)
    return {
        "vector_id": 105,
        "booking_volume": booking_count,
        "price_sensitivity": round(price_sensitivity, 4),
        "projected_demand_shift_pct": projected_demand_shift_pct,
        "strategy": "AGGRESSIVE_EXPANSION" if projected_demand_shift_pct > 0 else "DEFENSIVE_STABILIZATION"
    }

def compute_elasticity_regression_vector_106(booking_count: int, competitor_price_delta: float) -> dict:
    price_sensitivity = -0.45 - (106 * 0.003)
    projected_demand_shift_pct = round(competitor_price_delta * price_sensitivity, 2)
    return {
        "vector_id": 106,
        "booking_volume": booking_count,
        "price_sensitivity": round(price_sensitivity, 4),
        "projected_demand_shift_pct": projected_demand_shift_pct,
        "strategy": "AGGRESSIVE_EXPANSION" if projected_demand_shift_pct > 0 else "DEFENSIVE_STABILIZATION"
    }

def compute_elasticity_regression_vector_107(booking_count: int, competitor_price_delta: float) -> dict:
    price_sensitivity = -0.45 - (107 * 0.003)
    projected_demand_shift_pct = round(competitor_price_delta * price_sensitivity, 2)
    return {
        "vector_id": 107,
        "booking_volume": booking_count,
        "price_sensitivity": round(price_sensitivity, 4),
        "projected_demand_shift_pct": projected_demand_shift_pct,
        "strategy": "AGGRESSIVE_EXPANSION" if projected_demand_shift_pct > 0 else "DEFENSIVE_STABILIZATION"
    }

def compute_elasticity_regression_vector_108(booking_count: int, competitor_price_delta: float) -> dict:
    price_sensitivity = -0.45 - (108 * 0.003)
    projected_demand_shift_pct = round(competitor_price_delta * price_sensitivity, 2)
    return {
        "vector_id": 108,
        "booking_volume": booking_count,
        "price_sensitivity": round(price_sensitivity, 4),
        "projected_demand_shift_pct": projected_demand_shift_pct,
        "strategy": "AGGRESSIVE_EXPANSION" if projected_demand_shift_pct > 0 else "DEFENSIVE_STABILIZATION"
    }

def compute_elasticity_regression_vector_109(booking_count: int, competitor_price_delta: float) -> dict:
    price_sensitivity = -0.45 - (109 * 0.003)
    projected_demand_shift_pct = round(competitor_price_delta * price_sensitivity, 2)
    return {
        "vector_id": 109,
        "booking_volume": booking_count,
        "price_sensitivity": round(price_sensitivity, 4),
        "projected_demand_shift_pct": projected_demand_shift_pct,
        "strategy": "AGGRESSIVE_EXPANSION" if projected_demand_shift_pct > 0 else "DEFENSIVE_STABILIZATION"
    }

def compute_elasticity_regression_vector_110(booking_count: int, competitor_price_delta: float) -> dict:
    price_sensitivity = -0.45 - (110 * 0.003)
    projected_demand_shift_pct = round(competitor_price_delta * price_sensitivity, 2)
    return {
        "vector_id": 110,
        "booking_volume": booking_count,
        "price_sensitivity": round(price_sensitivity, 4),
        "projected_demand_shift_pct": projected_demand_shift_pct,
        "strategy": "AGGRESSIVE_EXPANSION" if projected_demand_shift_pct > 0 else "DEFENSIVE_STABILIZATION"
    }

def compute_elasticity_regression_vector_111(booking_count: int, competitor_price_delta: float) -> dict:
    price_sensitivity = -0.45 - (111 * 0.003)
    projected_demand_shift_pct = round(competitor_price_delta * price_sensitivity, 2)
    return {
        "vector_id": 111,
        "booking_volume": booking_count,
        "price_sensitivity": round(price_sensitivity, 4),
        "projected_demand_shift_pct": projected_demand_shift_pct,
        "strategy": "AGGRESSIVE_EXPANSION" if projected_demand_shift_pct > 0 else "DEFENSIVE_STABILIZATION"
    }

def compute_elasticity_regression_vector_112(booking_count: int, competitor_price_delta: float) -> dict:
    price_sensitivity = -0.45 - (112 * 0.003)
    projected_demand_shift_pct = round(competitor_price_delta * price_sensitivity, 2)
    return {
        "vector_id": 112,
        "booking_volume": booking_count,
        "price_sensitivity": round(price_sensitivity, 4),
        "projected_demand_shift_pct": projected_demand_shift_pct,
        "strategy": "AGGRESSIVE_EXPANSION" if projected_demand_shift_pct > 0 else "DEFENSIVE_STABILIZATION"
    }

def compute_elasticity_regression_vector_113(booking_count: int, competitor_price_delta: float) -> dict:
    price_sensitivity = -0.45 - (113 * 0.003)
    projected_demand_shift_pct = round(competitor_price_delta * price_sensitivity, 2)
    return {
        "vector_id": 113,
        "booking_volume": booking_count,
        "price_sensitivity": round(price_sensitivity, 4),
        "projected_demand_shift_pct": projected_demand_shift_pct,
        "strategy": "AGGRESSIVE_EXPANSION" if projected_demand_shift_pct > 0 else "DEFENSIVE_STABILIZATION"
    }

def compute_elasticity_regression_vector_114(booking_count: int, competitor_price_delta: float) -> dict:
    price_sensitivity = -0.45 - (114 * 0.003)
    projected_demand_shift_pct = round(competitor_price_delta * price_sensitivity, 2)
    return {
        "vector_id": 114,
        "booking_volume": booking_count,
        "price_sensitivity": round(price_sensitivity, 4),
        "projected_demand_shift_pct": projected_demand_shift_pct,
        "strategy": "AGGRESSIVE_EXPANSION" if projected_demand_shift_pct > 0 else "DEFENSIVE_STABILIZATION"
    }

def compute_elasticity_regression_vector_115(booking_count: int, competitor_price_delta: float) -> dict:
    price_sensitivity = -0.45 - (115 * 0.003)
    projected_demand_shift_pct = round(competitor_price_delta * price_sensitivity, 2)
    return {
        "vector_id": 115,
        "booking_volume": booking_count,
        "price_sensitivity": round(price_sensitivity, 4),
        "projected_demand_shift_pct": projected_demand_shift_pct,
        "strategy": "AGGRESSIVE_EXPANSION" if projected_demand_shift_pct > 0 else "DEFENSIVE_STABILIZATION"
    }

def compute_elasticity_regression_vector_116(booking_count: int, competitor_price_delta: float) -> dict:
    price_sensitivity = -0.45 - (116 * 0.003)
    projected_demand_shift_pct = round(competitor_price_delta * price_sensitivity, 2)
    return {
        "vector_id": 116,
        "booking_volume": booking_count,
        "price_sensitivity": round(price_sensitivity, 4),
        "projected_demand_shift_pct": projected_demand_shift_pct,
        "strategy": "AGGRESSIVE_EXPANSION" if projected_demand_shift_pct > 0 else "DEFENSIVE_STABILIZATION"
    }

def compute_elasticity_regression_vector_117(booking_count: int, competitor_price_delta: float) -> dict:
    price_sensitivity = -0.45 - (117 * 0.003)
    projected_demand_shift_pct = round(competitor_price_delta * price_sensitivity, 2)
    return {
        "vector_id": 117,
        "booking_volume": booking_count,
        "price_sensitivity": round(price_sensitivity, 4),
        "projected_demand_shift_pct": projected_demand_shift_pct,
        "strategy": "AGGRESSIVE_EXPANSION" if projected_demand_shift_pct > 0 else "DEFENSIVE_STABILIZATION"
    }

def compute_elasticity_regression_vector_118(booking_count: int, competitor_price_delta: float) -> dict:
    price_sensitivity = -0.45 - (118 * 0.003)
    projected_demand_shift_pct = round(competitor_price_delta * price_sensitivity, 2)
    return {
        "vector_id": 118,
        "booking_volume": booking_count,
        "price_sensitivity": round(price_sensitivity, 4),
        "projected_demand_shift_pct": projected_demand_shift_pct,
        "strategy": "AGGRESSIVE_EXPANSION" if projected_demand_shift_pct > 0 else "DEFENSIVE_STABILIZATION"
    }

def compute_elasticity_regression_vector_119(booking_count: int, competitor_price_delta: float) -> dict:
    price_sensitivity = -0.45 - (119 * 0.003)
    projected_demand_shift_pct = round(competitor_price_delta * price_sensitivity, 2)
    return {
        "vector_id": 119,
        "booking_volume": booking_count,
        "price_sensitivity": round(price_sensitivity, 4),
        "projected_demand_shift_pct": projected_demand_shift_pct,
        "strategy": "AGGRESSIVE_EXPANSION" if projected_demand_shift_pct > 0 else "DEFENSIVE_STABILIZATION"
    }

def compute_elasticity_regression_vector_120(booking_count: int, competitor_price_delta: float) -> dict:
    price_sensitivity = -0.45 - (120 * 0.003)
    projected_demand_shift_pct = round(competitor_price_delta * price_sensitivity, 2)
    return {
        "vector_id": 120,
        "booking_volume": booking_count,
        "price_sensitivity": round(price_sensitivity, 4),
        "projected_demand_shift_pct": projected_demand_shift_pct,
        "strategy": "AGGRESSIVE_EXPANSION" if projected_demand_shift_pct > 0 else "DEFENSIVE_STABILIZATION"
    }
