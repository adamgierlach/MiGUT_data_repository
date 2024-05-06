#%% Main script to run for data analysis of MiGUT data (figure 6)
#%% Written By: Adam Gierlach
#%% Last Modified: 2024-02-28
#%% This Code:
#   (0) Imports and sets hyperparamaters
#   (1) Creates Figure 6a: extracts frequency information
#   (2) Creates Figure 6b: plots representative window from dat 2 of recording, behaviours labeled
#   (3) Creates Figure 6c: plots long term recording and snippets


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
from datetime import datetime, time
import datetime as dt
from os.path import exists
from scipy import signal
from pathlib import Path
import scipy
import time
import datetime

from Plot_EGG import *

#%%

output_type = '.pdf'
out_path = './Output/fig6/'

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%% (1) Figure 6a

path_d0 = '../data/20230419_Day0_data_laptop.txt'
path_d1 = '../data/20230420_day1_data_laptop.txt'
path_d2 = '../data/20230421_day2_laptop.txt'
path_d3 = '../data/20230422_day3_laptop.txt'

data0 = read_egg_v3(path_d0, scale=600, interp=0)
data1 = read_egg_v3(path_d1, scale=600, interp=0)
data2 = read_egg_v3(path_d2, scale=600, interp=0)
data3 = read_egg_v3(path_d3, scale=600, interp=0)

#%% Final day 0
fig_size_aa = (15/2+2,5/2)

fig1, fig1_ax, filtered_data0 = signalplot(data0, freq=[0.01, 0.25], xlim=[1620, 1620+60*13])
fig1, fig1_ax,freq_data0 = egg_signalfreq(filtered_data0, rate=60.7, freqlim=[1.5,10],chan_to_plot=[2], figsize_val=fig_size_aa)
plt.title("Day 0")
plt.show()
time_string = datetime.datetime.now().strftime("%y%m%d-%H%S%f")
fig1.savefig(out_path + 'f6aa_day0_' + time_string + output_type, bbox_inches='tight', transparent=True)

#%% Final day 1

fig1, fig1_ax, filtered_data1 = signalplot(data1, freq=[0.01, 0.25], xlim=[1892, 2672]) #xlim=[2520, 2520+60*13]
plt.show()
fig1, fig1_ax,freq_data1 = egg_signalfreq(filtered_data1,
               chan_to_plot=[0],
               figsize_val=fig_size_aa,
               freqlim=[1.5,10],
               rate=60.7
               )
plt.title("Day 1")

plt.show()
time_string = datetime.datetime.now().strftime("%y%m%d-%H%S%f")
fig1.savefig(out_path + 'f6aa_day1_' + time_string + output_type, bbox_inches='tight', transparent=True)

#%% Final day 2

fig1, fig1_ax, filtered_data2 = signalplot(data2, freq=[0.01, 0.25], xlim=[1620-60*3, 1620+60*10])
plt.show()
fig1, fig1_ax,freq_data2 = egg_signalfreq(filtered_data2,
               chan_to_plot=[1],
               figsize_val=fig_size_aa,
               freqlim=[1.5,10],
               rate=60.7
               )
plt.title("Day 2")

plt.show()
time_string = datetime.datetime.now().strftime("%y%m%d-%H%S%f")
fig1.savefig(out_path + 'f6aa_day2_' + time_string + output_type, bbox_inches='tight', transparent=True)

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%% (2) Figure 6b

space_value = 35
min_to_plot = 3
fig_size_value = (10,15)
# index = 6
fig1, fig1_ax, filtered_data0 = signalplot(data2,
                                               xlim=[1080, 1800],
                                               # xlim=[0+index*60*min_to_plot, 60*min_to_plot*(1+index)],
                                               freq=[0.01, 0.25],
                                               title="Day 2 Measurment",
                                               spacer = space_value,
                                               textsize=32,
                                               scale_text_position_yoffset=-4,
                                               vline=[595, 743, 945,1297, 1415, 1538, 2158], figsize=fig_size_value)
plt.show()
time_string = datetime.datetime.now().strftime("%y%m%d-%H%S%f")
fig1.savefig(out_path + 'f6ab_main3_20230422day2_' + time_string + output_type, bbox_inches='tight', transparent=True)

fig1_ax.set_title("Day 2 Measurment", fontweight="normal")

plt.show()
time_string = datetime.datetime.now().strftime("%y%m%d-%H%S%f")
fig1.savefig(out_path + 'f6ab_main3_20230422day2_' + time_string + output_type, bbox_inches='tight', transparent=True)

#%% Amp comparrison of Day 2 T=1080 to 1800

chan_to_analyze = 5

fig1, fig1_ax, pre_eating_filtered_data = signalplot(data2,
                                               xlim=[1080, 1297],
                                               # xlim=[0+index*60*min_to_plot, 60*min_to_plot*(1+index)],
                                               freq=[0.01, 0.25],
                                               title="Day 2 Measurment",
                                               spacer = space_value,
                                               textsize=32,
                                               vline=[595, 743, 945,1297, 1415, 1538, 2158], figsize=fig_size_value)
plt.show()
print("Post Amb / Anticipation")
t_pre, d_pre = signal_peakcalculate(pre_eating_filtered_data,width=175,trim=[1000,1000],channel=chan_to_analyze) #slow

fig1, fig1_ax, amb_filtered_data = signalplot(data2,
                                               xlim=[1297, 1415],
                                               # xlim=[0+index*60*min_to_plot, 60*min_to_plot*(1+index)],
                                               freq=[0.01, 0.25],
                                               title="Day 2 Measurment",
                                               spacer = space_value,
                                               textsize=32,
                                               vline=[595, 743, 945,1297, 1415, 1538, 2158], figsize=fig_size_value)

plt.show()
print("Ambulatory Anticipation")
t_amb, d_amb = signal_peakcalculate(amb_filtered_data,width=175,trim=[1000,1000],channel=chan_to_analyze) #slow

fig1, fig1_ax, feeding_filtered_data = signalplot(data2,
                                               xlim=[1415, 1538],
                                               # xlim=[0+index*60*min_to_plot, 60*min_to_plot*(1+index)],
                                               freq=[0.01, 0.25],
                                               title="Day 2 Measurment",
                                               spacer = space_value,
                                               textsize=32,
                                               vline=[595, 743, 945,1297, 1415, 1538, 2158], figsize=fig_size_value)

plt.show()
print("Eating")
t_eat, d_eat = signal_peakcalculate(feeding_filtered_data,width=175,trim=[1000,1000],channel=chan_to_analyze) #slow

fig1, fig1_ax, post_filtered_data = signalplot(data2,
                                               xlim=[1538, 1800],
                                               # xlim=[0+index*60*min_to_plot, 60*min_to_plot*(1+index)],
                                               freq=[0.01, 0.25],
                                               title="Day 2 Measurment",
                                               spacer = space_value,
                                               textsize=32,
                                               vline=[595, 743, 945,1297, 1415, 1538, 2158], figsize=fig_size_value)

plt.show()
print("Post")
t_post, d_post = signal_peakcalculate(post_filtered_data,width=175,trim=[1000,1000],channel=chan_to_analyze) #slow


amb_diff = d_amb.mean() / d_pre.mean()
eat_diff = d_eat.mean() / d_pre.mean()
post_diff = d_post.mean() / d_pre.mean()

print("Channel ", chan_to_analyze)
print("Ambulation / Anticipation Difference: ", amb_diff)
print("Feeding Difference: ", eat_diff)
print("Post Feeding Difference: ", post_diff)

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%% (3) Figure 6C

#%% Load data

path_s5='../data/20230828_Ambulation.txt'
path_s5_beh='../data/20230828_behaviours_simplified.txt'

datas5=read_egg_v3_burst(path_s5,scale=600)

datas5.drop(datas5.tail(560).index, inplace=True)

datas5["datetime"]=get_datetime(datas5)
datas5["timestamps_hours"]=datas5["timestamps"]/(60*60)

#%% Get behaviour times

beh_df = pd.read_csv(path_s5_beh)
beh_df["datetime"] = get_datetime(beh_df)

start_rec_time = datas5["datetime"].iloc[0]

beh_df["time (s)"] = beh_df['datetime'].apply(lambda x: (x-start_rec_time).total_seconds())

#%% MAIN Updated plot with behaviour labels (Beh not shown in preview, but in saved fig)

fontsize_value = 32
fs = 60.7
tdiv = 60*60
f, ax, d = signalplot(datas5,
                      freq=[0.01, 0.25],
                      skip_chan=[0,1,2,3,4,5,6],
                      figsize= (80/2,10/2),
                      textsize=fontsize_value,
                      scale_bar_position_xoffset=0.8,
                      scale_bar_position_yoffset=8,
                      # vline=[29*3*60/tdiv,59*3*60/tdiv,214*3*60/tdiv,761*3*60/tdiv, 552*3*60/tdiv],
                      time_divider=tdiv)

plt.rcParams.update({'font.size': fontsize_value})
plt.xlabel("Time (hours)")

# Add behaviour
xlim_max = ax.get_xlim()[1]
second_xaxis_offset = 60
rect_ypos = xlim_max + second_xaxis_offset
start_xy = (0,rect_ypos)
rect_height = 10

for idx, time in enumerate(beh_df["time (s)"][:-1]):
    behaviour = beh_df["behaviour"].iloc[idx].strip()

    start_pos = time/tdiv
    end_pos = beh_df["time (s)"].iloc[idx+1]/tdiv

    start_rect_pos = (start_pos, rect_ypos)
    rect_width = end_pos - start_pos

    # print("Rect ",idx,": ", start_rect_pos[0], " - ", end_pos, "; width: ",rect_width) #debug
    facecolor_value = 'red'
    if behaviour == "Feeding":
        facecolor_value = 'darkgreen'
    elif behaviour == "Ambulating":
        facecolor_value = 'darkblue'
    elif behaviour == "Sedintary":
        facecolor_value = 'gold'
    else:
        print("Unknown label:", behaviour,"; at index ", idx)

    ax.add_patch(plt.Rectangle(start_rect_pos, rect_width, rect_height,
                               facecolor=facecolor_value,
                               clip_on=False, linewidth=0))

x_tick_locs, x_tick_lables = plt.xticks()


# Add time to second xaxis
ax2 = ax.twiny()
ax2.set_xlim(ax.get_xlim())

tick_positions_hours = x_tick_locs #np.arange(0,45,5)


label_strings = []
for tp in tick_positions_hours:
    over_times = datas5["datetime"].loc[datas5["timestamps_hours"]>=tp]
    if len(over_times) > 1:
        dt = over_times.iloc[0]
        tick_hour_string = dt.strftime("%H:%M")

    else:
        tick_hour_string = "N/A"

    label_strings.append(tick_hour_string)

ax2.set_xticklabels(label_strings)

# Add sleep times
ylims = ax.get_ylim()
ystart = ylims[0]
yheight = ylims[1]-ylims[0]

s=4.32577
w=16.45965-4.32577
ax.add_patch(plt.Rectangle((s,ystart), w, yheight,
                               facecolor='lightgray',
                               clip_on=False, linewidth=0))

s=28.45938
w=40.45910-28.45938
ax.add_patch(plt.Rectangle((s,ystart), w, yheight,
                               facecolor='lightgray',
                               clip_on=False, linewidth=0))

s=28.45938
w=40.45910-28.45938
ax.add_patch(plt.Rectangle((s,ystart), w, yheight,
                               facecolor='lightgray',
                               clip_on=False, linewidth=0))

#save
time_string = datetime.datetime.now().strftime("%y%m%d-%H%S%f")
f.savefig(out_path + 'f6bb_long_' + time_string + output_type, bbox_inches='tight', transparent=True)
plt.show()

print("finished at ", datetime.datetime.now().strftime("%y%m%d-%H%S%f"))


#%% Plot zoomed in sections

tdiv=1
# index=29
index=59
min_to_plot=3
index_to_plot = [29,214,552,761]
# index_to_plot = [0]

for index in index_to_plot:
    hours_to_sec = 60*60
    fig1, ax, filtered_data0 = signalplot(datas5,
                                                   xlim=[0+index*60*min_to_plot, 60*min_to_plot*(1+index)],
                                                   freq=[0.01, 0.25],
                                                   skip_chan=[0,1,2,3,4,5,6],
                                                   # title="Day 0 Measurment",
                                                   # spacer = space_value,
                                                   tilt_value=45,
                                                   textsize=32,
                                                   figsize=(15,5))


    # Add time to second xaxis
    x_tick_locs, x_tick_lables = plt.xticks()

    ax2 = ax.twiny()
    ax2.set_xlim(ax.get_xlim())

    tick_positions_hours = x_tick_locs #np.arange(0,45,5)

    label_strings = []
    for tp in tick_positions_hours:
        over_times = datas5["datetime"].loc[datas5["timestamps"]>=tp]
        if len(over_times) > 1:
            dt = over_times.iloc[0]
            tick_hour_string = dt.strftime("%H:%M:%S")

        else:
            tick_hour_string = "N/A"

        label_strings.append(tick_hour_string)


    ax2.set_xticklabels(label_strings)
    ax2.tick_params(labelrotation=45)

    #save
    time_string = datetime.datetime.now().strftime("%y%m%d-%H%S%f")
    fig1.savefig(out_path + 'f6bb_zoom_wtime' + time_string + output_type, bbox_inches='tight', transparent=True)
    plt.show()
