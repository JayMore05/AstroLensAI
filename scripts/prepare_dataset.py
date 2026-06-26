"""
Prepare image dataset for CNN training.
"""

import os
import cv2
import numpy as np
from sklearn.model_selection import train_test_split

IMAGE_SIZE = (224, 224)

CLASS_NAMES = [
    "Galaxy",
    "Nebula",
    "Planet",
    "Star",
    "Unknown"
]


class DatasetBuilder:

    def __init__(self, dataset_path):

        self.dataset_path = dataset_path

    def load_dataset(self):

        images = []

        labels = []

        for index, class_name in enumerate(CLASS_NAMES):

            folder = os.path.join(
                self.dataset_path,
                class_name
            )

            if not os.path.exists(folder):
                continue

            for file in os.listdir(folder):

                path = os.path.join(folder, file)

                image = cv2.imread(path)

                if image is None:
                    continue

                image = cv2.cvtColor(
                    image,
                    cv2.COLOR_BGR2RGB
                )

                image = cv2.resize(
                    image,
                    IMAGE_SIZE
                )

                image = image.astype(np.float32) / 255.0

                images.append(image)

                labels.append(index)

        return (
            np.array(images),
            np.array(labels)
        )

    def split(self):

        X, y = self.load_dataset()

        return train_test_split(
            X,
            y,
            test_size=0.2,
            random_state=42
        )


if __name__ == "__main__":

    builder = DatasetBuilder("datasets")

    X_train, X_test, y_train, y_test = builder.split()

    print("Training Images :", len(X_train))
    print("Testing Images :", len(X_test))