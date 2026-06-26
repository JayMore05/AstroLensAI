import os
import shutil
import numpy as np
import pandas as pd

from lightkurve import search_lightcurve


# ======================================================
# CACHE DIRECTORY
# ======================================================

CACHE_FOLDER = "data/nasa"

os.makedirs(
    CACHE_FOLDER,
    exist_ok=True
)


# ======================================================
# NASA LOADER
# ======================================================

def load_nasa_lightcurve(target):

    filename = (
        target.lower()
        .replace("-", "")
        .replace(" ", "")
        + ".csv"
    )

    filepath = os.path.join(
        CACHE_FOLDER,
        filename
    )

    # ==================================================
    # USE LOCAL CACHE
    # ==================================================

    if os.path.exists(filepath):

        df = pd.read_csv(filepath)

        if (
            "time" in df.columns
            and
            "flux" in df.columns
            and
            len(df) > 100
        ):

            print("Loaded from Local Cache")

            return (

                np.array(df["time"]),

                np.array(df["flux"])

            )

    # ==================================================
    # LIVE NASA DOWNLOAD
    # ==================================================

    print(f"Downloading {target} from NASA...")

    try:

        search = search_lightcurve(

            target,

            author="Kepler"

        )

        if len(search) == 0:

            search = search_lightcurve(target)

        if len(search) == 0:

            raise Exception(
                "No NASA observations found."
            )

        print(
            f"Found {len(search)} observations."
        )

        lc = search[0].download()

        if lc is None:

            raise Exception(
                "NASA download returned empty data."
            )

        lc = lc.remove_nans()

        time = np.array(
            lc.time.value
        )

        flux = np.array(
            lc.flux.value
        )

        if len(time) < 100:

            raise Exception(
                "Downloaded light curve is too small."
            )

        df = pd.DataFrame({

            "time": time,

            "flux": flux

        })

        df.to_csv(
            filepath,
            index=False
        )

        print(
            "Saved to Local Cache"
        )

        return (
            time,
            flux
        )

    except Exception as e:

        # ==============================================
        # REMOVE CORRUPTED LIGHTKURVE CACHE
        # ==============================================

        try:

            cache_path = os.path.join(

                os.path.expanduser("~"),

                ".cache",

                "lightkurve"

            )

            if os.path.exists(cache_path):

                shutil.rmtree(cache_path)

                print(
                    "Corrupted Lightkurve cache removed."
                )

        except Exception:

            pass

        raise Exception(

            f"NASA Download Failed:\n{e}"

        )