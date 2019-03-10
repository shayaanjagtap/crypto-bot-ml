import os
import time
import json
import warnings
import numpy as np
from numpy import newaxis
from keras.layers.core import Dense, Activation, Dropout
from keras.layers.recurrent import LSTM
from keras.models import Sequential
from keras.models import load_model

def build_network(layers):
    model = Sequential()

    model.add(LSTM(
        input_dim=layers[0],
        output_dim=layers[1],
        return_sequences=True))
    model.add(Dropout(0.2))

    model.add(LSTM(
        layers[2],
        return_sequences=False))
    model.add(Dropout(0.2))

    model.add(LSTM(
        output_dim=layers[3]
    ))
    model.add(Activation('relu'))

    start=time.time()
    model.compile(
        loss='mse',
        optimizer='adam')

    print(f"Compilation time : {time.time() - start}")

def load_network(file):
    if(os.path.isfile(file)):
        return load_model(file)
    else:
        print(f'No file at {file}')
        return None
