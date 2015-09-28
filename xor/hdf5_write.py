#!/usr/bin/env python
import h5py
import numpy as np

data_input = [[0,0],[0,1],[1,0],[1,1]]
data_label = [0,1,1,0]

with h5py.File("xor_data.hdf5", "w") as f:
	f['data'] = np.array(data_input,dtype=np.float)
	f['label'] = np.array(data_label,dtype=np.float)