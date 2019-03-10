
import h5py
import numpy as np
import pandas as pd

class ETL:
    '''
    ETL relevant processing methods
    '''

    def generate_clean_data(self, filename, batch_size=1000, start_index=0):
        with h5py.File(filename, 'r') as hf:
            i = start_index
            while True:
                data_x = hf['x'][i:i+batch_size]
                data_y = hf['y'][i:i+batch_size]
                i += batch_size
                yield(data_x, data_y)
