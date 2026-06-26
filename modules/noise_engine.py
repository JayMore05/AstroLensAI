import numpy as np


def analyze_noise(flux):
    """
    Analyze noise characteristics of a light curve.
    Returns:
        - Signal-to-Noise Ratio (SNR)
        - Variance
        - RMS Noise
        - Noise Type
        - Quality Score
    """

    flux = np.array(flux, dtype=float)

    # Remove invalid values
    flux = flux[np.isfinite(flux)]

    if len(flux) == 0:
        raise Exception("Flux data is empty.")

    mean_flux = np.mean(flux)
    std_flux = np.std(flux)
    variance = np.var(flux)
    rms = np.sqrt(np.mean((flux - mean_flux) ** 2))

    # Signal-to-Noise Ratio
    if std_flux == 0:
        snr = 9999
    else:
        snr = mean_flux / std_flux

    # Quality score
    if snr > 500:
        quality = 98
    elif snr > 200:
        quality = 95
    elif snr > 100:
        quality = 90
    elif snr > 50:
        quality = 80
    elif snr > 20:
        quality = 70
    else:
        quality = 50

    # Noise classification
    if variance < 1e-6:
        noise_type = "Very Low Noise"
    elif variance < 1e-4:
        noise_type = "Low Noise"
    elif variance < 1e-2:
        noise_type = "Moderate Noise"
    else:
        noise_type = "High Noise"

    return {
        "snr": round(float(snr), 2),
        "variance": float(variance),
        "rms_noise": float(rms),
        "noise_type": noise_type,
        "quality_score": quality
    }