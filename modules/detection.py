import numpy as np


def extract_features(image):
    """
    Extract simple image features.
    """

    mean_red = float(np.mean(image[:, :, 0]))
    mean_green = float(np.mean(image[:, :, 1]))
    mean_blue = float(np.mean(image[:, :, 2]))

    std_red = float(np.std(image[:, :, 0]))
    std_green = float(np.std(image[:, :, 1]))
    std_blue = float(np.std(image[:, :, 2]))

    brightness = float(np.mean(image))

    return [
        mean_red,
        mean_green,
        mean_blue,
        std_red,
        std_green,
        std_blue,
        brightness
    ]