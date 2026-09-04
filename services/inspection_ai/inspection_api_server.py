"""
Inspection AI microservice entry point
"""

from damage_vision_comparator import DamageVisionComparator

if __name__ == "__main__":
    comparator = DamageVisionComparator()
    print("Inspection AI Comparator initialized successfully.")
