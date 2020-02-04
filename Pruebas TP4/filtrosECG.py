#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 18:45:20 2020

@author: fede
"""

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import scipy.signal as sig
from scipy.fftpack import fft, fftshift
from spectrum import CORRELOGRAMPSD
from spectrum.tools import cshift
import scipy.io as sio
eps = np.finfo(float).eps
fig_sz_x = 14
fig_sz_y = 13
fig_dpi = 80 # dpi

fig_font_family = 'Ubuntu'
fig_font_size = 16

mat_struct = sio.loadmat('ECG_TP4.mat')

ecg_one_lead = mat_struct['ecg_lead']
ecg_one_lead = ecg_one_lead.flatten()
cant_muestras = len(ecg_one_lead)

fs = 1000 # Hz
nyq_frec = fs/2

# filter design
ripple = 0.5 # dB
atenuacion = 40 # dB

ws1 = 2 #Hz
wp1 = 5 #Hz
wp2 = 35 #Hz
ws2 = 45 #Hz

frecs = np.array([0.0, ws1, wp1, wp2, ws2, nyq_frec]) / nyq_frec
gains = np.array([-atenuacion, -atenuacion, -ripple, -ripple, -atenuacion, -atenuacion])
gains = 10**(gains/20) #Convierto el vector de dB a veces

cant_coef = 501
cant_coef2 = 5001
#FIR Design
num_firBlackmanHarris = sig.firwin2(cant_coef, frecs, gains , window='blackmanharris' )
num_firHamming = sig.firwin2(cant_coef2, frecs, gains, window='hamming')

den = 1.0
#IIR Design
bp_sos_butter = sig.iirdesign(wp=np.array([wp1, wp2]) / nyq_frec, ws=np.array([ws1, ws2]) / nyq_frec, gpass=ripple, gstop=atenuacion, analog=False, ftype='butter', output='sos')
bp_sos_cheby = sig.iirdesign(wp=np.array([wp1, wp2]) / nyq_frec, ws=np.array([ws1, ws2]) / nyq_frec, gpass=ripple, gstop=atenuacion, analog=False, ftype='cheby2', output='sos')

#FIR Construct
_, hh_BlackmanHarris = sig.freqz(num_firBlackmanHarris, den)
_, hh_Hamming = sig.freqz(num_firHamming, den)

#IIR Construct
w, h_butter = sig.sosfreqz(bp_sos_butter)
_, h_cheby  = sig.sosfreqz(bp_sos_cheby)

w = w / np.pi * nyq_frec
plt.figure(1)

plt.plot(w, 20 * np.log10(abs(hh_BlackmanHarris)+eps), label='FIR: Blackman-Harris 5001 coeficientes')
plt.plot(w, 20 * np.log10(abs(hh_Hamming)+eps), label='FIR: Hamming 50001 coeficientes')
plt.plot(frecs * nyq_frec, 20*np.log10(gains+eps), 'rx', label='plantilla' )

plt.title('Plantillas FIR')
plt.xlabel('Frequencia [Hz]')
plt.ylabel('Modulo [dB]')
plt.axis([0, nyq_frec/5, -60, 5 ]);

plt.grid()

axes_hdl = plt.gca()
axes_hdl.legend()

rect_stop1 = plt.Rectangle((0, -atenuacion), ws1, -(2*atenuacion), facecolor="#00FF00", alpha=0.5)
plt.gca().add_patch(rect_stop1)
plt.text(0 , -50, "Banda \n de \n stop 1", verticalalignment='center', style='italic', color='black', bbox={'facecolor': '#00FF00', 'alpha': 0.6, 'pad': 2})

rect_trans1 = plt.Rectangle((ws1, 0), wp1-ws1, -3*atenuacion, facecolor="#FCE514", alpha=0.5)
plt.gca().add_patch(rect_trans1)
plt.text(ws1 + (wp1-ws1)/2, -10, "Banda \n de \n transicion 1", verticalalignment='center', style='italic', color='black', bbox={'facecolor': '#00FF00', 'alpha': 0.6, 'pad': 2})
                                                                               
rect_pass = plt.Rectangle((wp1, 0), wp2 - wp1, -ripple, facecolor="#00FF00", alpha=0.5)
plt.gca().add_patch(rect_pass)
plt.text(wp1 + (wp2-wp1)/2 , -ripple, "Banda de paso", verticalalignment='center', style='italic', color='black', bbox={'facecolor': '#00FF00', 'alpha': 0.6, 'pad': 2})
       
rect_trans2 = plt.Rectangle((wp2, 0), ws2-wp2, -3*atenuacion, facecolor="#FCE514", alpha=0.5)
plt.gca().add_patch(rect_trans2)
plt.text(wp2 + (ws2-wp2)/2, -10, "Banda \n de \n transicion 2", verticalalignment='center', style='italic', color='black', bbox={'facecolor': '#00FF00', 'alpha': 0.6, 'pad': 2})
                                                                                                           
rect_stop2 = plt.Rectangle((ws2, -atenuacion), fs/2 - ws2, -(2*atenuacion), facecolor="#00FF00", alpha=0.5)
plt.gca().add_patch(rect_stop2)
plt.text(ws2 , -50, "Banda \n de \n stop 2", verticalalignment='center', style='italic', color='black', bbox={'facecolor': '#00FF00', 'alpha': 0.6, 'pad': 2})

                                                                                                             
plt.show()

plt.figure(2)
plt.plot(w, 20*np.log10(np.abs(h_butter)+eps), label='IIR-Butter' )
plt.plot(w, 20*np.log10(np.abs(h_cheby)+eps), label='IIR-Cheby 2' )

plt.plot(frecs * nyq_frec, 20*np.log10(gains+eps), 'rx', label='plantilla' )

plt.title('Plantillas IIR')
plt.xlabel('Frequencia [Hz]')
plt.ylabel('Modulo [dB]')
plt.axis([0, nyq_frec/5, -60, 5 ]);

plt.grid()

axes_hdl = plt.gca()
axes_hdl.legend()

rect_stop1 = plt.Rectangle((0, -atenuacion), ws1, -(2*atenuacion), facecolor="#00FF00", alpha=0.5)
plt.gca().add_patch(rect_stop1)
plt.text(0 , -50, "Banda \n de \n stop 1", verticalalignment='center', style='italic', color='black', bbox={'facecolor': '#00FF00', 'alpha': 0.6, 'pad': 2})

rect_trans1 = plt.Rectangle((ws1, 0), wp1-ws1, -3*atenuacion, facecolor="#FCE514", alpha=0.5)
plt.gca().add_patch(rect_trans1)
plt.text(ws1 + (wp1-ws1)/2, -10, "Banda \n de \n transicion 1", verticalalignment='center', style='italic', color='black', bbox={'facecolor': '#00FF00', 'alpha': 0.6, 'pad': 2})
                                                                               
rect_pass = plt.Rectangle((wp1, 0), wp2 - wp1, -ripple, facecolor="#00FF00", alpha=0.5)
plt.gca().add_patch(rect_pass)
plt.text(wp1 + (wp2-wp1)/2 , -ripple, "Banda de paso", verticalalignment='center', style='italic', color='black', bbox={'facecolor': '#00FF00', 'alpha': 0.6, 'pad': 2})
       
rect_trans2 = plt.Rectangle((wp2, 0), ws2-wp2, -3*atenuacion, facecolor="#FCE514", alpha=0.5)
plt.gca().add_patch(rect_trans2)
plt.text(wp2 + (ws2-wp2)/2, -10, "Banda \n de \n transicion 2", verticalalignment='center', style='italic', color='black', bbox={'facecolor': '#00FF00', 'alpha': 0.6, 'pad': 2})
                                                                                                           
rect_stop2 = plt.Rectangle((ws2, -atenuacion), fs/2 - ws2, -(2*atenuacion), facecolor="#00FF00", alpha=0.5)
plt.gca().add_patch(rect_stop2)
plt.text(ws2 , -50, "Banda \n de \n stop 2", verticalalignment='center', style='italic', color='black', bbox={'facecolor': '#00FF00', 'alpha': 0.6, 'pad': 2})
                                                                                                   
plt.show()


#Filtrado de señal
ECG_f_butt = sig.sosfiltfilt(bp_sos_butter, ecg_one_lead)
ECG_f_cheb = sig.sosfiltfilt(bp_sos_cheby, ecg_one_lead)

ECG_f_firBlackmanHarris = sig.filtfilt(num_firBlackmanHarris, den, ecg_one_lead)
ECG_f_firHamming = sig.filtfilt(num_firHamming, den, ecg_one_lead)

zonas_con_interf_baja_frec = ( 
        np.array([12, 12.4]) *60*fs, # minutos a muestras
        np.array([15, 15.2]) *60*fs, # minutos a muestras
        )


zonas_sin_interf = ( 
        np.array([5, 5.2]) *60*fs, # minutos a muestras
        [4000, 5500], # muestras
        [10e3, 11e3], # muestras
        )

for ii in zonas_con_interf_baja_frec:
# intervalo limitado de 0 a cant_muestras
    zoom_region = np.arange(np.max([0, ii[0]]), np.min([cant_muestras, ii[1]]), dtype='uint')
    
    plt.figure(figsize=(fig_sz_x, fig_sz_y), dpi= fig_dpi, facecolor='w', edgecolor='k')
    plt.plot(zoom_region, ecg_one_lead[zoom_region], label='ECG', lw=2)
    plt.plot(zoom_region, ECG_f_butt[zoom_region], label='Butter')
    plt.plot(zoom_region, ECG_f_cheb[zoom_region], label='Cheby2')
    
    plt.plot(zoom_region, ECG_f_firBlackmanHarris[zoom_region], label='FIR BlackmanHarris')
    plt.plot(zoom_region, ECG_f_firHamming[zoom_region], label='FIR Hamming')
    
    plt.title('ECG filtering example from ' + str(ii[0]) + ' to ' + str(ii[1]) )
    plt.ylabel('Adimensional')
    plt.xlabel('Muestras (#)')
    
    axes_hdl = plt.gca()
    axes_hdl.legend()
    axes_hdl.set_yticks(())
            
    plt.show()
    
for ii in zonas_sin_interf:
# intervalo limitado de 0 a cant_muestras
    zoom_region = np.arange(np.max([0, ii[0]]), np.min([cant_muestras, ii[1]]), dtype='uint')
    
    plt.figure(figsize=(fig_sz_x, fig_sz_y), dpi= fig_dpi, facecolor='w', edgecolor='k')
    plt.plot(zoom_region, ecg_one_lead[zoom_region], label='ECG', lw=2)
    plt.plot(zoom_region, ECG_f_butt[zoom_region], label='Butter')
    plt.plot(zoom_region, ECG_f_cheb[zoom_region], label='Cheby2')
    
    plt.plot(zoom_region, ECG_f_firBlackmanHarris[zoom_region], label='FIR BlackmanHarris')
    plt.plot(zoom_region, ECG_f_firHamming[zoom_region], label='FIR Hamming')
    
    plt.title('ECG filtering example from ' + str(ii[0]) + ' to ' + str(ii[1]) )
    plt.ylabel('Adimensional')
    plt.xlabel('Muestras (#)')
    
    axes_hdl = plt.gca()
    axes_hdl.legend()
    axes_hdl.set_yticks(())
            
    plt.show()