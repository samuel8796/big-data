import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import backend,layers
from keras.layers.normalization import BatchNormalization
from keras.optimizers import Adam
import matplotlib.pyplot as plt
%matplotlib inline

train_norm = normalize(row_data)
# change the last day and next day 
X_train, Y_train = buildTrain(train_norm, 5, 1)
X_train, Y_train = shuffle(X_train, Y_train)
X_train, Y_train, X_val, Y_val = splitData(X_train, Y_train, 0.2)


model = buildManyToManyModel(X_train.shape)
callback = [tf.keras.callbacks.EarlyStopping(monitor="loss", patience=10, verbose=1, mode="auto")]

model.fit(X_train, Y_train, epochs=1000, batch_size=128, validation_data=(X_val, Y_val),callbacks=callback)
