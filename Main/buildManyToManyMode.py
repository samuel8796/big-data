import tensorflow as tf
from tensorflow import keras
from keras.optimizers import Adam


def buildManyToManyModel(shape):
    model = tf.keras.Sequential()
    model.add(layers.LSTM(17, input_length=shape[1], input_dim=shape[2]))
  # output shape: (5, 1)
    model.add(layers.Dense(1))
    model.compile(loss="mse", optimizer="adam")
    model.summary()
    return model
