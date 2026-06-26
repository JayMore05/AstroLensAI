"""
Extract image features for AI model.
"""

import cv2
import numpy as np


class FeatureExtractor:

    def __init__(self):
        pass

    def extract_edges(self, image):

        gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

        edges = cv2.Canny(gray, 50, 150)

        return edges

    def histogram(self, image):

        hist = cv2.calcHist(
            [image],
            [0],
            None,
            [256],
            [0, 256]
        )

        hist = cv2.normalize(hist, hist).flatten()

        return hist

    def extract(self, image):

        edges = self.extract_edges(image)

        histogram = self.histogram(image)

        return {
            "edges": edges,
            "histogram": histogram
        }