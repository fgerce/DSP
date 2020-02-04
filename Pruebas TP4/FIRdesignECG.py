#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 13:46:16 2020

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

def mfreqz(b,a=1):
    w,h = sig.freqz(b,a)
    h_dB = 20 * np.log10 (abs(h))
    plt.subplot(211)
    plt.plot(w/max(w),h_dB)
    plt.ylim(-150, 5)
    plt.ylabel('Magnitude (db)')
    plt.xlabel(r'Normalized Frequency (x$\pi$rad/sample)')
    plt.title(r'Frequency response')
    plt.subplot(212)
    h_Phase = np.unwrap(np.arctan2(np.imag(h),np.real(h)))
    plt.plot(w/max(w),h_Phase)
    plt.ylabel('Phase (radians)')
    plt.xlabel(r'Normalized Frequency (x$\pi$rad/sample)')
    plt.title(r'Phase response')
    plt.subplots_adjust(hspace=0.5)
    
fs = 1000 # Hz
nyq_frec = fs/2

n=500
d = sig.firwin(n, cutoff=[0.3, 0.5], window='blackmanharris', pass_zero=False)

mfreqz(d)
plt.show()