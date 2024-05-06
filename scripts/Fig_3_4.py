# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 15:05:12 2023

@author: seany

Instructions - Set directory to Figures 3 and 4 directory. Note this requires a particular version of Plot_EGG library that has keywords for name_dict and color_dict

Each cell can be run seperately. Requires the following data files:
    '2021.12.15_Euth.txt' This is a euthansia experiment with MIGUT in eggv2 file format
    '2022.05.02_Combined.txt' This is a experiment with MIGUT in egg_v3 file format.
    '2023.09.21' This is a folder containing all data files for the simultanous serosa, mucosal and MIGUT recording. See name_dict assignments below for each channel

"""

import sys
from Plot_EGG import *
import Plot_EGG_2024 as egg_updated


from Shimmer_Lib import *
import scipy.signal as sig
import os

if not os.path.exists('Output'): os.makedirs('Output') # make output directory 

#%% Import Data of representative recording for Figure 3

dat=read_egg_v3('../data/2022.05.02_Combined.txt',scale=150)


#%% Figure 3B

fheat,axheat,c=heatplot(dat,freq=[0.0005,15],xlim=[500,5000])
fheat.savefig('Output/3B.svg',bbox_inches='tight',transparent=True)


#%%
#These are the plots for Figure 3C

f_slow,an_slow,c1=signalplot(dat,freq=[.01,.25],xlim=[700,900],skip_chan=[0,2,3,4,5,6,7],figsize=(10,4),hide_y=True,spacer=10)
f_res,an_res,c2=signalplot(dat,freq=[.25,5],xlim=[700,730],skip_chan=[0,2,3,4,5,6,7],figsize=(10,4),hide_y=True,spacer=2)
f_ekg,an_ekg,c3=signalplot(dat,freq=[5,1000],xlim=[700,710],skip_chan=[0,2,3,4,5,6,7],figsize=(10,4),spacer=.15,hide_y=True)
f_raw,an_raw,c4=signalplot(dat,xlim=[700,900],skip_chan=[0,2,3,4,5,6,7],figsize=(10,4),hide_y=True, spacer=20)
f_pylorus,an_pylorus,d=signalplot(dat,freq=[0.0005,15],xlim=[500,5000],skip_chan=[3,4,5,6,7],figsize=(10,7.5),spacer=40)


f_slow.savefig('Output/SlowWave.svg',bbox_inches='tight',transparent=True)
f_res.savefig('Output/Res.svg',bbox_inches='tight',transparent=True)
f_ekg.savefig('Output/EKG.svg',bbox_inches='tight',transparent=True)
f_raw.savefig('Output/Raw.svg',bbox_inches='tight',transparent=True)
f_pylorus.savefig('Output/MMC.svg',bbox_inches='tight',transparent=True)


#%% Figure 3D
chan_n=2
rate=32
skipnum=100
dat_euth=read_egg_v2('../data/2021.12.15_Euth.txt', channels=3, rate=rate)

dat_chan=dat_euth[chan_n]
datcut=np.copy(dat_chan[:,skipnum:])

f_data=egg_filter(datcut,rate=32,freq=[0.01,15])
fig=plt.figure(figsize=(12,3))
ax_dat=fig.add_subplot(1,1,1)
ax_dat.plot(f_data[0,:],f_data[1,:])

ax_dat.set_xlabel('Time (s)')
ax_dat.set_ylabel('Electrical Activity (mV)')
ax_dat.vlines(125,-5,5, linestyles='dashed',colors='r')

fig.savefig('3D_Terminal.svg')

#%% Import Data for Figure 4B and 4C

data_092123_m=read_egg_v3('../data/2023.09.21_Terminal.txt',scale=300,rate=61.07)
data_092123_m=settime_egg_v3(data_092123_m,year=2023,month=9,day=21)

data_092123_s1=read_shimmer('../data/2023.09.21_Shimmer_68ED.csv')
data_092123_s2=read_shimmer('../data/2023.09.21_Shimmer_69CE.csv')
data_092123_s3=read_shimmer('../data/2023.09.21_Shimmer_7970.csv')

data_092123_full=migut_shimmer_merge_interpolate(data_092123_m,data_092123_s1,str_match='ExG',new_chan='SA')

data_092123_full=migut_shimmer_merge_interpolate(data_092123_full,data_092123_s3,str_match='ExG',new_chan='C')

data_092123_full=migut_shimmer_merge_interpolate(data_092123_full,data_092123_s2,str_match='ExG',new_chan='SB')


#%% Fig 4 B

color_dict={"Channel 4":"#00B914","Channel 7":"#00B914",'Channel SA2':'#6800E7','Channel SB0':'#6800E7','Channel SA0':'#FF3900', 'Channel 0':'Cutaneous'}

name_dict={'Channel SB0':'Serosal (A-REF)','Channel SA0':'Cutaneous','Channel SA2':'Serosal (C-REF)','Channel C0':'Cutaneous'}

data_092123_full = data_092123_full[[col for col in data_092123_full.columns if col != 'Channel SA0'] + ['Channel SA0']]
data_092123_full = data_092123_full[[col for col in data_092123_full.columns if col != 'Channel C0'] + ['Channel C0']]

fig4b,b,c=egg_updated.signalplot(data_092123_full,time='Synctime',xlim=[3800,4000],freq=[0.02,15],skip_chan=[0,1,2,3,5,6,'SA1','SB2','SB1','C1','C2','C0'],figsize=(15,12),Normalize_channels=False,output='PD',spacer=4,name_dict=name_dict,color_dict=color_dict,textsize=30)
#fig4b,b,c=eggs.signalplot(data_092123_full,time='Synctime',xlim=[3800,4000],freq=[0.02,15],skip_chan=[0,1,2,3,5,6,'SA1','SB2','SB1','C1','C2','C0'],figsize=(15,12),Normalize_channels=False,output='PD',spacer=4,textsize=30)

fig4b.savefig('Output/Compare.svg')

#%% Fig 4 C

#
a,b,c=egg_updated.signalplot(data_092123_full,time='Synctime',xlim=[3500,4200],freq=[0.02,15],skip_chan=[0,1,2,3,5,6,'SB0','SB2','SB1','C1','C2','SA1','SA0','C0',7],figsize=(15,10),Normalize_channels=True,output='PD')
fig1,ax1,d1=egg_updated.egg_signalfreq(c,freqlim=[1,100],figsize=(10,8),mode='fft',ylog=True,vline=[18,18*2,18*3],vline_color='red',name_dict=name_dict,textsize=30)
fig2,ax2,d2=egg_updated.egg_signalfreq(c,freqlim=[1,8],figsize=(10,8),mode='fft',ylog=False,vline=[3.1,3.1*2],vline_color='black',name_dict=name_dict,textsize=30)
fig3,ax3,d3=egg_updated.egg_signalfreq(c,freqlim=[80,200],figsize=(10,8),mode='fft',ylog=False,vline_color='green',vline=[85,85*2],name_dict=name_dict,textsize=30)

fig1.savefig('Output/1_100.svg',bbox_inches='tight',transparent=True)
fig2.savefig('Output/1_8.svg',bbox_inches='tight',transparent=True)
fig3.savefig('Output/80_200.svg',bbox_inches='tight',transparent=True)

