"""
Simple exoplanet transit detector
"""

import numpy as np


class TransitDetector:

    def detect(self, brightness_values):

        brightness_values = np.array(brightness_values)

        average = np.mean(brightness_values)

        minimum = np.min(brightness_values)

        drop = average - minimum

        if drop > average * 0.03:

            return {
                "transit_detected": True,
                "brightness_drop": float(drop)
            }

        return {
            "transit_detected": False,
            "brightness_drop": float(drop)
        }