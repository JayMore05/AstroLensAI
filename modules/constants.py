"""
Global constants for AstroLensAI
"""

IMAGE_SIZE = (224, 224)

CLASS_NAMES = [
    "Galaxy",
    "Nebula",
    "Star Cluster",
    "Exoplanet Transit",
    "Unknown"
]

MODEL_PATH = "models/astro_model.keras"

CONFIDENCE_THRESHOLD = 0.70