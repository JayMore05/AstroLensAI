"""
CNN Model Training
"""

from tensorflow.keras.models import Sequential

from tensorflow.keras.layers import (
    Conv2D,
    MaxPooling2D,
    Flatten,
    Dense,
    Dropout
)

from tensorflow.keras.utils import to_categorical

from scripts.prepare_dataset import DatasetBuilder

IMAGE_SIZE = (224,224)

NUM_CLASSES = 5


builder = DatasetBuilder("datasets")

X_train, X_test, y_train, y_test = builder.split()

y_train = to_categorical(
    y_train,
    NUM_CLASSES
)

y_test = to_categorical(
    y_test,
    NUM_CLASSES
)


model = Sequential([

    Conv2D(
        32,
        (3,3),
        activation="relu",
        input_shape=(224,224,3)
    ),

    MaxPooling2D(),

    Conv2D(
        64,
        (3,3),
        activation="relu"
    ),

    MaxPooling2D(),

    Conv2D(
        128,
        (3,3),
        activation="relu"
    ),

    MaxPooling2D(),

    Flatten(),

    Dense(
        256,
        activation="relu"
    ),

    Dropout(0.4),

    Dense(
        NUM_CLASSES,
        activation="softmax"
    )

])


model.compile(

    optimizer="adam",

    loss="categorical_crossentropy",

    metrics=["accuracy"]

)


model.fit(

    X_train,

    y_train,

    validation_data=(

        X_test,

        y_test

    ),

    epochs=10,

    batch_size=16

)


model.save("astro_model.keras")

print()

print("="*50)

print("Model Saved Successfully!")

print("="*50)