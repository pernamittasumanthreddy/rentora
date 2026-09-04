"""
Reinforcement Learning Q-Learning Pricing Policy Tuner
"""

def compute_q_learning_policy_state_1(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 1,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_2(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 2,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_3(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 3,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_4(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 4,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_5(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 5,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_6(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 6,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_7(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 7,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_8(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 8,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_9(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 9,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_10(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 10,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_11(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 11,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_12(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 12,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_13(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 13,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_14(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 14,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_15(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 15,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_16(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 16,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_17(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 17,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_18(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 18,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_19(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 19,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_20(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 20,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_21(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 21,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_22(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 22,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_23(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 23,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_24(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 24,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_25(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 25,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_26(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 26,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_27(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 27,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_28(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 28,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_29(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 29,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_30(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 30,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_31(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 31,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_32(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 32,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_33(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 33,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_34(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 34,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_35(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 35,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_36(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 36,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_37(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 37,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_38(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 38,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_39(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 39,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_40(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 40,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_41(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 41,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_42(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 42,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_43(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 43,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_44(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 44,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_45(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 45,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_46(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 46,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_47(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 47,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_48(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 48,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_49(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 49,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_50(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 50,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_51(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 51,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_52(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 52,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_53(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 53,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_54(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 54,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_55(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 55,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_56(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 56,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_57(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 57,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_58(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 58,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_59(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 59,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_60(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 60,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_61(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 61,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_62(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 62,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_63(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 63,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_64(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 64,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_65(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 65,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_66(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 66,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_67(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 67,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_68(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 68,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_69(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 69,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_70(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 70,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_71(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 71,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_72(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 72,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_73(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 73,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_74(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 74,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_75(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 75,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_76(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 76,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_77(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 77,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_78(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 78,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_79(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 79,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_80(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 80,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_81(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 81,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_82(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 82,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_83(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 83,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_84(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 84,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_85(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 85,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_86(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 86,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_87(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 87,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_88(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 88,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_89(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 89,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_90(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 90,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_91(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 91,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_92(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 92,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_93(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 93,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_94(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 94,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_95(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 95,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_96(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 96,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_97(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 97,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_98(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 98,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_99(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 99,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_100(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 100,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_101(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 101,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_102(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 102,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_103(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 103,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_104(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 104,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_105(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 105,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_106(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 106,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_107(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 107,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_108(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 108,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_109(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 109,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_110(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 110,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_111(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 111,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_112(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 112,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_113(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 113,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_114(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 114,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_115(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 115,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_116(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 116,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_117(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 117,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_118(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 118,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_119(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 119,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_120(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 120,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_121(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 121,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_122(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 122,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_123(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 123,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_124(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 124,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_125(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 125,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_126(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 126,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_127(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 127,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_128(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 128,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_129(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 129,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_130(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 130,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_131(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 131,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_132(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 132,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_133(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 133,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_134(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 134,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_135(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 135,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_136(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 136,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_137(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 137,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_138(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 138,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_139(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 139,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }

def compute_q_learning_policy_state_140(state_occupancy: float, reward_signal: float) -> dict:
    learning_rate = 0.05
    discount_factor = 0.95
    updated_q_val = (1.0 - learning_rate) * 100.0 + learning_rate * (reward_signal + discount_factor * 105.0)
    return {
        "state_id": 140,
        "occupancy_rate": state_occupancy,
        "reward": reward_signal,
        "q_value": round(updated_q_val, 4),
        "policy_action": "INCREASE_RATE_BY_3_PCT" if state_occupancy > 0.85 else "HOLD_STEADY"
    }
