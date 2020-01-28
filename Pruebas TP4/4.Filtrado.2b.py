#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 02:59:14 2020

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

ww, hh = sig.freqz(np.array([1, -1]), np.array([-1, 0]))
ww = ww / np.pi

plt.figure(1)
plt.plot(ww, (abs(hh)), label='Modulo')
plt.title('Modulo para h(k) = (-1,1)')
plt.xlabel('Frequencia normalizada')
plt.ylabel('Modulo [dB]')
plt.grid(which='both', axis='both')
axes_hdl = plt.gca()
axes_hdl.legend()
plt.show()

plt.figure(2)
plt.plot(ww, np.angle(hh), label='Fase')
plt.title('Fase para h(k) = (-1,1)')
plt.xlabel('Frequencia normalizada')
plt.ylabel('Modulo [dB]')
plt.grid(which='both', axis='both')
axes_hdl = plt.gca()
axes_hdl.legend()
plt.show()