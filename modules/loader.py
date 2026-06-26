"""
Image Loader for AstroLensAI
Supports JPG, PNG and FITS astronomical images.
"""

import os
import cv2
from astropy.io import fits
import numpy as np


class ImageLoader:

    def __init__(self):
        self.supported_formats = [".jpg", ".jpeg", ".png", ".fits"]

    def is_supported(self, filepath):
        ext = os.path.splitext(filepath)[1].lower()
        return ext in self.supported_formats

    def load(self, filepath):

        if not self.is_supported(filepath):
            raise ValueError(
                f"Unsupported file format: {filepath}"
            )

        ext = os.path.splitext(filepath)[1].lower()

        if ext == ".fits":
            return self.load_fits(filepath)

        return self.load_image(filepath)

    def load_image(self, filepath):

        image = cv2.imread(filepath)

        if image is None:
            raise FileNotFoundError(filepath)

        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        return image

    def load_fits(self, filepath):

        with fits.open(filepath) as hdul:

            data = hdul[0].data

            data = np.nan_to_num(data)

            data = data.astype(np.float32)

            data -= data.min()

            if data.max() > 0:
                data /= data.max()

            image = (255 * data).astype(np.uint8)

            return image