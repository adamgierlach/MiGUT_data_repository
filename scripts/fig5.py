#%% Main script to run for data analysis of MiGUT data (figure 5)
#%% Written By: Adam Gierlach
#%% Last Modified: 2024-02-26
#%% This Code:
#   (0) Imports and sets hyperparamaters
#   (1) Creates Figure 5a: raw eight channel data stream with behaviours labeled for 3.5hours
#   (2) Creates Figure 5b: Spectrogram of data
#   (3) Creates Figure 5c: Comparison of different behaviours


#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%% (0) Imports

import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
import math
import glob
import matplotlib as mpl
# from tqdm.notebook import tqdm
from datetime import datetime
from os.path import exists
from scipy import signal
from pathlib import Path
import scipy
import time
import datetime

from Plot_EGG import *

#%%

output_type = '.pdf'
out_path = './Output/fig5/'

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%% (1) Figure 5a: raw eight channel data stream with behaviours labeled for 3.5hours

path_d0='../data/2022.08.17_Full.txt'
data0=read_egg_v3(path_d0,scale=600, interp=1)

#%% Plot Figure 5a
fig1,fig1_ax,filtered_data0=signalplot(data0,freq=[0.01, 0.25], vline=[120, 3720, 4320,5100, 7620, 10020, 11700])
plt.show()
fig1.savefig(out_path + 'fig5a_longmeas.pdf',bbox_inches='tight',transparent=True)

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%% (2) Figure 5b: Spectrogram of data

#%% Load previous plotting files
import Plot_EGG_20230924 as egg_orig

path_d0='../data/2022.08.17_Full.txt'
data0_orig = egg_orig.read_egg_v3(path_d0, scale=600) # Interpolates differently for better fft

#%% Plot
final_time = data0_orig["timestamps"].iloc[-1]
f,a,d=egg_orig.egg_freq_heatplot(data0_orig, xlim=[0,11000], freqlim=[1,8], freq=[0.02,0.2], seg_length=400, n=2,max_scale=.5)
plt.show()
f.savefig(out_path + 'fig5b_freq.pdf',bbox_inches='tight',transparent=True)


#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%% (3) Figure 5c: Comparison of different behaviours

fig_size_aa = None#(15,3)

# Feeding
fig1, fig1_ax, filtered_data0 = signalplot(data0, freq=[0.01, 0.25], xlim=[1750,2000],  spacer=50, skip_chan=[0,1,2,3,4,5,6], figsize=fig_size_aa)
plt.title("Feeding")
plt.show()
time_string = datetime.datetime.now().strftime("%y%m%d-%H%S%f")
fig1.savefig(out_path + 'f5c_eating_notitle_' + time_string + output_type, bbox_inches='tight', transparent=True)

# Sleeping
fig1, fig1_ax, filtered_data0 = signalplot(data0, freq=[0.01, 0.25], xlim=[8000,8250],  spacer=50, skip_chan=[0,1,2,3,4,5,6], figsize=fig_size_aa)
plt.title("Sleeping")
plt.show()
time_string = datetime.datetime.now().strftime("%y%m%d-%H%S%f")
fig1.savefig(out_path + 'f5c_sleeping_notitle_' + time_string + output_type, bbox_inches='tight', transparent=True)


# fig1, fig1_ax, filtered_data0 = signalplot(data0, freq=[0.01, 0.25], xlim=[8000,8250],  spacer=60)
fig1, fig1_ax, filtered_data0 = signalplot(data0, freq=[0.01, 0.25], xlim=[6000,6250],  spacer=50, skip_chan=[0,1,2,3,4,5,6], figsize=fig_size_aa)
plt.title("Ambulating")
plt.show()
time_string = datetime.datetime.now().strftime("%y%m%d-%H%S%f")
fig1.savefig(out_path + 'f5c_amb_notitle_' + time_string + output_type, bbox_inches='tight', transparent=True)

