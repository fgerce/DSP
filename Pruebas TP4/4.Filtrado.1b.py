#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 19:25:28 2020

@author: fede
"""

import numpy as np
from pandas import DataFrame
from IPython.display import HTML
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as sig
from scipy.fftpack import fft, fftshift
import scipy.io as sio
from time import time
import control

num = np.array([1, 1, 1])
den = np.array([3, 0, 0])

ww, hh = sig.freqz(num,den)
ww = ww / np.pi

plt.figure(1)
plt.plot(ww, 20 * np.log10(abs(hh)), label='Modulo para N=3')
plt.title('Modulo para N=3')
plt.xlabel('Frequencia normalizada')
plt.ylabel('Modulo [dB]')
plt.grid(which='both', axis='both')
axes_hdl = plt.gca()
axes_hdl.legend()
plt.show()

plt.figure(2)
plt.plot(ww, np.angle(hh), label='Fase para N=3')
plt.title('Fase para N=3')
plt.xlabel('Frequencia normalizada')
plt.ylabel('Fase [rad]')
plt.grid(which='both', axis='both')
axes_hdl = plt.gca()
axes_hdl.legend()
plt.show()
plt.tight_layout()

tf = control.TransferFunction(num,den, 1)
print (tf)
control.pzmap(tf, Plot=True, title='Pole Zero Map', grid=True)

plt.figure(3)
num = np.array([1, 1, 1, 1, 1])
den = np.array([5, 0, 0, 0, 0])


ww2, hh2 = sig.freqz(num, den)
ww2 = ww2 / np.pi

plt.figure(4)
plt.plot(ww2, 20 * np.log10(abs(hh2)), label='Modulo para N=5')
plt.title('Modulo para N=5')
plt.xlabel('Frequencia normalizada')
plt.ylabel('Modulo [dB]')
plt.grid(which='both', axis='both')
axes_hdl = plt.gca()
axes_hdl.legend()
plt.show()

plt.figure(5)
plt.plot(ww2, np.angle(hh2), label='Fase para N=5')
plt.title('Fase para N=5')
plt.xlabel('Frequencia normalizada')
plt.ylabel('Fase [rad]')
plt.grid(which='both', axis='both')
axes_hdl = plt.gca()
axes_hdl.legend()
plt.show()


tf = control.TransferFunction(num,den, 1)
print (tf)
control.pzmap(tf, Plot=True, title='Pole Zero Map', grid=True)