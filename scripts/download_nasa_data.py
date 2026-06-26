from modules.nasa_loader import load_nasa_lightcurve

targets = [

    "Kepler-10",
    "Kepler-22",
    "Kepler-62",
    "Kepler-69",
    "Kepler-90",

    "Kepler-16",
    "HD 189733",

    "KIC 8462852",

    "TIC 25155310",
    "TIC 349480507"

]

print("=" * 60)
print("Downloading NASA Datasets")
print("=" * 60)

for target in targets:

    try:

        print(f"\nDownloading {target}")

        time, flux = load_nasa_lightcurve(target)

        print(f"Downloaded {len(time)} observations")

    except Exception as e:

        print(f"Failed: {e}")

print("\nFinished!")