#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 16:57:46 2019

@author: fede
"""
from Modulos import instrumentos as ins

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

N  = 1000 # muestras
fs = 1000 # Hz
Ts = 1/fs

f0 = 9*fs/N
p0 = 0     # radianes
a0 = 1      # Volts
f1 = 8*fs/N

tt0, signal0 = ins.generador_senoidal(fs, f0, N, a0, p0)
tt1, signal1 = ins.generador_senoidal(fs, f1, N, a0, p0)

signal3 = np.concatenate((signal1[0:int(fs/f1)], np.zeros(N-int(fs/f1))),axis=0)
  
signal4 = np.concatenate((np.zeros(2*int(fs/f1)), signal0[0:int(fs/f0)]))
signal4 = np.concatenate((signal4, np.zeros(N - 2*int(fs/f1) - int(fs/f0))),axis=0)

signal0 = signal3 + signal4

modulo0, fase0, ww0 = ins.analizador_espectro(signal0, fs)

plt.figure(figsize=(10,10))
plt.subplot(2,1,1)
plt.title("FFT 1 ciclo más otro de otra frecuencia desplazado pero invertidos")
plt.plot(ww0, modulo0, label='fs')
plt.grid()
plt.xlabel("Frecuencia")
plt.ylabel("Amplitud")
plt.xlim(0,30)
plt.subplot(2,1,2)
plt.plot(ww0, fase0, label='fs')
plt.grid()
plt.xlabel("Frecuencia")
plt.ylabel("Fase")

Ps = ins.sumatoria_modulo_cuadrado(modulo0[0:int(fs/2)])

Pf0 = np.abs(modulo0[int(f0)])
Pf0 = Pf0 * Pf0

Pf1 = np.abs(modulo0[int(f1)])
Pf1 = Pf1 * Pf1

maxE = ww0[np.argmax(modulo0)]
