#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 15:30:20 2019

@author: fede
"""
from Modulos import instrumentos as ins

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

N  = 1000 # muestras
fs = 1000 # Hz
Ts = 1/fs

f0 = 9*fs/N
p0 = 0     # radianes
a0 = 1      # Volts
a1 = 5
a2 = 3

tt0, signal0 = ins.generador_senoidal(fs, f0, N, a0, p0)
tt1, signal1 = ins.generador_senoidal(fs, f0, N, a1, p0)
tt2, signal2 = ins.generador_senoidal(fs, f0, N, a2, p0)

signal0 = np.concatenate((signal0[0:int(fs/f0)], np.zeros(N-int(fs/f0))),axis=0)

signal1 = np.concatenate((np.zeros(int(fs/f0)), signal1[0:int(fs/f0)]))
signal1 = np.concatenate((signal1, np.zeros(N-2*int(fs/f0))),axis=0)

signal2 = np.concatenate((np.zeros(2*int(fs/f0)), signal2[0:int(fs/f0)]))
signal2 = np.concatenate((signal2, np.zeros(N-3*int(fs/f0))),axis=0)

signal0 = signal0 + signal1 + signal2
signal0 = signal0[0:3*int(fs/f0)]

signal0 = np.concatenate((signal0, signal0, signal0, np.zeros(1
                                                              )), axis=0)

modulo0, fase0, ww0 = ins.analizador_espectro(signal0, fs)

plt.plot(tt0, signal0, label='fs')
Ps = ins.sumatoria_modulo_cuadrado(modulo0[0:int(fs/2)])

Pf0 = np.abs(modulo0[int(f0)])
Pf0 = Pf0 * Pf0

maxE = np.power(ins.get_max_point(modulo0)[1],2)
