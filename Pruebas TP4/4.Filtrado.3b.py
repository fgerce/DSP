#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 03:26:09 2020

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


ww, hh = sig.freqz(np.array([1, 0, -1]), np.array([1, 0, 0]))
ww = ww / np.pi

plt.figure(1)
plt.plot(ww, (abs(hh)), label='Modulo para N=2 y b=-1')
plt.title('Modulo Modulo para N=2 y b=-1')
plt.xlabel('Frequencia normalizada')
plt.ylabel('Modulo [dB]')
plt.grid(which='both', axis='both')
axes_hdl = plt.gca()
axes_hdl.legend()
plt.show()

plt.figure(2)
plt.plot(ww, np.angle(hh), label='Fase para N=2 y b=-1')
plt.title('Fase para N=2 y b=-1')
plt.xlabel('Frequencia normalizada')
plt.ylabel('Modulo [dB]')
plt.grid(which='both', axis='both')
axes_hdl = plt.gca()
axes_hdl.legend()
plt.show()


ww2, hh2 = sig.freqz(np.array([1, 0, 0, 0, -1]), np.array([1, 0, 0, 0, 0]))
ww2 = ww2 / np.pi

plt.figure(3)
plt.plot(ww2, 20 * np.log10(abs(hh2)), label='Modulo para N=4 y b=-1')
plt.title('Modulo para N=4 y b=-1')
plt.xlabel('Frequencia normalizada')
plt.ylabel('Modulo [dB]')
plt.grid(which='both', axis='both')
axes_hdl = plt.gca()
axes_hdl.legend()
plt.show()

plt.figure(4)
plt.plot(ww2, np.angle(hh2), label='Fase para N=4 y b=-1')
plt.title('Fase para N=4 y b=-1')
plt.xlabel('Frequencia normalizada')
plt.ylabel('Fase [rad]')
plt.grid(which='both', axis='both')
axes_hdl = plt.gca()
axes_hdl.legend()
plt.show()