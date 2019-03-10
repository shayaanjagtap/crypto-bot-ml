import time
import json
import h5py
import threading
import lstm, etl

import numpy as np
import pandas as pd
import seaborn as sns

import matplotlib.pyplot as plt

start = time.time()

def plot_results(pred, true):
    fig=sns.figure(figsize(18,12), dpi=80, facecolor='w', edgecolor='k')
    ax = fig.add_subplot(111)
    ax.plot(true_data, label='True Data')
    plt.plot(predicted_data, label='Prediction')
    plt.legend()
    plt.show()

def predict_sequences_multiple(model, data, window_size, prediction_len):
    prediction_seqs= []
    for i in range(int(len(data)/prediction_len)):
        
