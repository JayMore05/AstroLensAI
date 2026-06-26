import random


LABELS = [

    "Galaxy",

    "Nebula",

    "Planet",

    "Star"

]


def random_prediction():

    label = random.choice(LABELS)

    confidence = round(

        random.uniform(90, 99.9),

        2

    )

    return label, confidence