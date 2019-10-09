#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 15:00:25 2019

@author: fede
"""
from Modulos import instrumentos as ins

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# NO modifiques este bloque
############################

N  = 1000 # muestras
fs = 1000 # Hz
Ts = 1/fs

a0 = 1     # Volts
p0 = 0     # radianes
f0 = fs/4 + 0.5# Hz


tt0, signal0 = ins.generador_senoidal (fs, f0, N, a0, p0)
tt1, signal1 = ins.generador_senoidal (fs, f0, N, a0, p0)
tt2, signal2 = ins.generador_senoidal (fs, f0, N, a0, p0)
tt3, signal3 = ins.generador_senoidal (fs, f0, N, a0, p0)


extra_zeros = int(N/10)
signal0 = np.concatenate((signal0, np.zeros(extra_zeros)),axis=0)
tt0 = np.linspace(0, (N-1)*Ts, N+extra_zeros)

extra_zeros = N
signal1 = np.concatenate((signal1, np.zeros(extra_zeros)),axis=0)
tt1 = np.linspace(0, (N-1)*Ts, N+extra_zeros)

extra_zeros = 10*N
signal2 = np.concatenate((signal2, np.zeros(extra_zeros)),axis=0)
tt2 = np.linspace(0, (N-1)*Ts, N+extra_zeros)


plt.figure("Analizador espectro")

plt.title("Modulo y fase señal")

modulo0, fase0, ww0 = ins.analizador_espectro(signal0, fs)
modulo1, fase1, ww1 = ins.analizador_espectro(signal1, fs)
modulo2, fase2, ww2 = ins.analizador_espectro(signal2, fs)
modulo3, fase3, ww3 = ins.analizador_espectro(signal3, fs)

plt.plot(ww0, modulo0, label='+N/10 muestras')
plt.plot(ww1, modulo1, label='+N muestras')
plt.plot(ww2, modulo2, label='+10N muestras')
plt.plot(ww3, modulo3, label='+0 muestras')

plt.legend(loc='upper right')
plt.grid()
plt.xlabel("Frecuencia")
plt.ylabel("Amplitud")
plt.xlim(245.5,255.5)

e0 = ((ww0[ins.get_max_index(modulo0)[0]] - f0) / f0) * 100
e1 = ((ww1[ins.get_max_index(modulo1)[0]] - f0) / f0) * 100
e2 = ((ww2[ins.get_max_index(modulo2)[0]] - f0) / f0) * 100
e3 = ((ww3[ins.get_max_index(modulo3)[0]] - f0) / f0) * 100