import numpy as np

from modules.nasa_loader import load_nasa_lightcurve
from modules.feature_extractor import extract_features


def build_dataset():

    targets = [

    "Kepler-10"

]

    X = []

    y = []

    for target, label in targets:

        try:

            print(f"Processing {target}")

            time, flux = load_nasa_lightcurve(
                target
            )

            features = extract_features(
                time,
                flux
            )

            X.append(features)

            y.append(label)

        except Exception as e:

            print(
                f"Skipped {target}: {e}"
            )

    return np.array(X), np.array(y)