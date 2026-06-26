NASA_DATABASE = {

    "Galaxy":
        "Galaxies are enormous systems containing billions of stars, gas, dust and dark matter.",

    "Nebula":
        "Nebulae are giant clouds of gas and dust where stars are born.",

    "Planet":
        "Planets orbit stars and reflect their light.",

    "Star":
        "Stars are massive luminous spheres of hot plasma.",

    "Unknown":
        "No NASA information available."

}


def get_nasa_information(label):

    return NASA_DATABASE.get(
        label,
        NASA_DATABASE["Unknown"]
    )