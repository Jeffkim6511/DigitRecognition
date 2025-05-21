import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import tensorflow as tf
import numpy as np
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.datasets import mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Check how many examples do we have in our train and test sets
# print(f"We have {len(x_train)} images in the training set and {len(x_test)} images in the test set.")

# add another parameter for color_channels
x_train = x_train.reshape(x_train.shape + (1,))
x_test = x_test.reshape(x_test.shape + (1,))

# normalize and change to float32
x_train = x_train/255.0
x_test = x_test/255.0

x_train = x_train.astype(np.float32)
x_test = x_test.astype(np.float32)

# model
model = tf.keras.Sequential([
    layers.Conv2D(filters=10,
                  kernel_size=3,
                  activation='relu',
                  input_shape=(28, 28, 1)),
    layers.Conv2D(10, 3, activation='relu'),
    layers.MaxPool2D(),
    layers.Conv2D(10, 3, activation='relu'),
    layers.Conv2D(10, 3, activation='relu'),
    layers.MaxPool2D(),
    layers.Flatten(),
    layers.Dense(10, activation='softmax')
])

#model.summary()

model.compile(
    loss='sparse_categorical_crossentropy',
    optimizer=keras.optimizers.Adam(),
    metrics=['accuracy'],
)

model.fit(x_train, y_train, batch_size=64, epochs=11, verbose=2)

model.evaluate(x_test, y_test)

model.save("digit_recognizer.h5")