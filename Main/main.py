import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import backend,layers
from keras.layers.normalization import BatchNormalization
from keras.optimizers import Adam
import matplotlib.pyplot as plt

row_data = load_row_dataset("A(塑化).xlsx")
#load dataset
row_data = missing_value(row_data)
#dealing missing value
train_norm = normalize(row_data)
#normalize data
X_train, Y_train = buildTrain(train_norm, 10, 1)
#build training data set (pastday,futureday)
X_train, Y_train = shuffle(X_train, Y_train,10)
#shuffle traing data set (X,Y,seed)
X_train, Y_train, X_val, Y_val = splitData(X_train, Y_train, 0.7)
#create validation data set (X,Y,ratio)

model = buildModel(X_train.shape)
callback = [tf.keras.callbacks.EarlyStopping(monitor="loss", patience=10, verbose=1, mode="auto")]

model.fit(X_train, Y_train, epochs=1000, batch_size=128,callbacks=callback)

interact_manual(show,number = (0,len(result)-1))
