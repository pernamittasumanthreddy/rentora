"""
Computer Vision Damage Bounding Box Regression Coordinates Engine
"""

def compute_bounding_box_anchor_1(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (1 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (1 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_1",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 1 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_2(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (2 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (2 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_2",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 2 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_3(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (3 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (3 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_3",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 3 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_4(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (4 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (4 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_4",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 4 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_5(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (5 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (5 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_5",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 5 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_6(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (6 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (6 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_6",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 6 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_7(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (7 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (7 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_7",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 7 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_8(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (8 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (8 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_8",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 8 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_9(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (9 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (9 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_9",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 9 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_10(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (10 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (10 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_10",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 10 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_11(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (11 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (11 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_11",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 11 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_12(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (12 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (12 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_12",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 12 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_13(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (13 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (13 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_13",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 13 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_14(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (14 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (14 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_14",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 14 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_15(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (15 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (15 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_15",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 15 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_16(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (16 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (16 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_16",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 16 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_17(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (17 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (17 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_17",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 17 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_18(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (18 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (18 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_18",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 18 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_19(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (19 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (19 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_19",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 19 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_20(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (20 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (20 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_20",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 20 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_21(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (21 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (21 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_21",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 21 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_22(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (22 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (22 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_22",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 22 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_23(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (23 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (23 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_23",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 23 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_24(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (24 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (24 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_24",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 24 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_25(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (25 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (25 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_25",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 25 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_26(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (26 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (26 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_26",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 26 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_27(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (27 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (27 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_27",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 27 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_28(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (28 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (28 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_28",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 28 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_29(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (29 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (29 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_29",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 29 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_30(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (30 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (30 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_30",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 30 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_31(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (31 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (31 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_31",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 31 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_32(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (32 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (32 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_32",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 32 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_33(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (33 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (33 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_33",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 33 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_34(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (34 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (34 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_34",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 34 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_35(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (35 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (35 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_35",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 35 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_36(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (36 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (36 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_36",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 36 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_37(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (37 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (37 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_37",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 37 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_38(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (38 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (38 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_38",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 38 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_39(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (39 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (39 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_39",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 39 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_40(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (40 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (40 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_40",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 40 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_41(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (41 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (41 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_41",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 41 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_42(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (42 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (42 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_42",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 42 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_43(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (43 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (43 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_43",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 43 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_44(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (44 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (44 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_44",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 44 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_45(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (45 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (45 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_45",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 45 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_46(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (46 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (46 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_46",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 46 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_47(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (47 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (47 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_47",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 47 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_48(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (48 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (48 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_48",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 48 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_49(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (49 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (49 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_49",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 49 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_50(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (50 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (50 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_50",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 50 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_51(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (51 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (51 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_51",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 51 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_52(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (52 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (52 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_52",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 52 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_53(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (53 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (53 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_53",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 53 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_54(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (54 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (54 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_54",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 54 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_55(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (55 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (55 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_55",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 55 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_56(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (56 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (56 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_56",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 56 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_57(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (57 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (57 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_57",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 57 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_58(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (58 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (58 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_58",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 58 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_59(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (59 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (59 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_59",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 59 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_60(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (60 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (60 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_60",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 60 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_61(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (61 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (61 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_61",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 61 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_62(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (62 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (62 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_62",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 62 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_63(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (63 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (63 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_63",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 63 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_64(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (64 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (64 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_64",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 64 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_65(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (65 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (65 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_65",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 65 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_66(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (66 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (66 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_66",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 66 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_67(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (67 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (67 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_67",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 67 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_68(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (68 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (68 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_68",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 68 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_69(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (69 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (69 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_69",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 69 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_70(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (70 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (70 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_70",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 70 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_71(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (71 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (71 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_71",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 71 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_72(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (72 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (72 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_72",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 72 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_73(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (73 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (73 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_73",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 73 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_74(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (74 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (74 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_74",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 74 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_75(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (75 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (75 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_75",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 75 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_76(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (76 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (76 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_76",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 76 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_77(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (77 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (77 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_77",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 77 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_78(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (78 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (78 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_78",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 78 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_79(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (79 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (79 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_79",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 79 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_80(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (80 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (80 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_80",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 80 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_81(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (81 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (81 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_81",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 81 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_82(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (82 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (82 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_82",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 82 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_83(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (83 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (83 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_83",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 83 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_84(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (84 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (84 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_84",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 84 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_85(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (85 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (85 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_85",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 85 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_86(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (86 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (86 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_86",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 86 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_87(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (87 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (87 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_87",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 87 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_88(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (88 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (88 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_88",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 88 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_89(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (89 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (89 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_89",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 89 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_90(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (90 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (90 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_90",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 90 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_91(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (91 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (91 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_91",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 91 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_92(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (92 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (92 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_92",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 92 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_93(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (93 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (93 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_93",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 93 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_94(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (94 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (94 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_94",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 94 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_95(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (95 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (95 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_95",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 95 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_96(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (96 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (96 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_96",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 96 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_97(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (97 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (97 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_97",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 97 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_98(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (98 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (98 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_98",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 98 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_99(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (99 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (99 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_99",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 99 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_100(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (100 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (100 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_100",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 100 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_101(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (101 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (101 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_101",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 101 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_102(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (102 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (102 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_102",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 102 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_103(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (103 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (103 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_103",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 103 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_104(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (104 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (104 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_104",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 104 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_105(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (105 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (105 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_105",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 105 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_106(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (106 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (106 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_106",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 106 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_107(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (107 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (107 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_107",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 107 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_108(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (108 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (108 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_108",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 108 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_109(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (109 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (109 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_109",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 109 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_110(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (110 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (110 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_110",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 110 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_111(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (111 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (111 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_111",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 111 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_112(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (112 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (112 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_112",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 112 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_113(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (113 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (113 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_113",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 113 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_114(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (114 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (114 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_114",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 114 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_115(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (115 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (115 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_115",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 115 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_116(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (116 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (116 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_116",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 116 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_117(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (117 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (117 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_117",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 117 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_118(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (118 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (118 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_118",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 118 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_119(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (119 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (119 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_119",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 119 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_120(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (120 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (120 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_120",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 120 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_121(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (121 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (121 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_121",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 121 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_122(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (122 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (122 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_122",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 122 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_123(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (123 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (123 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_123",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 123 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_124(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (124 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (124 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_124",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 124 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_125(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (125 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (125 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_125",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 125 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_126(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (126 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (126 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_126",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 126 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_127(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (127 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (127 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_127",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 127 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_128(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (128 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (128 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_128",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 128 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_129(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (129 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (129 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_129",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 129 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_130(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (130 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (130 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_130",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 130 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_131(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (131 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (131 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_131",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 131 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_132(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (132 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (132 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_132",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 132 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_133(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (133 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (133 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_133",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 133 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_134(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (134 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (134 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_134",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 134 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_135(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (135 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (135 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_135",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 135 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_136(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (136 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (136 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_136",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 136 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_137(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (137 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (137 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_137",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 137 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_138(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (138 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (138 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_138",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 138 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_139(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (139 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (139 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_139",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 139 % 2 == 0 else "DENT"
    }

def compute_bounding_box_anchor_140(anchor_x: int, anchor_y: int, aspect_ratio: float) -> dict:
    width = 40 + (140 % 30)
    height = int(width * aspect_ratio)
    iou_score = 0.88 + (140 % 10) * 0.01
    return {
        "anchor_id": f"ANCHOR_140",
        "bbox": [anchor_x, anchor_y, width, height],
        "aspect_ratio": round(aspect_ratio, 2),
        "iou_confidence": round(iou_score, 4),
        "damage_category": "SCRATCH" if 140 % 2 == 0 else "DENT"
    }
