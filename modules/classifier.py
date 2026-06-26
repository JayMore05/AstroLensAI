import random


CLASSES = [
    "Galaxy",
    "Nebula",
    "Star",
    "Planet",
    "Unknown Object"
]


def classify_image(image):
    """
    Placeholder classifier.
    Will later load the trained TensorFlow model.
    """

    prediction = random.choice(CLASSES)

    confidence = random.uniform(75, 99)

    return prediction, confidence