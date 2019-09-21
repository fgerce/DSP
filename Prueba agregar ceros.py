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
##################
# a.4) Senoidal #
#################

a0 = 1     # Volts
p0 = 0     # radianes
f0 = fs+10 # Hz

# Insertar aquí el código para generar y visualizar la señal
##############################################################
tt, signal = ins.generador_senoidal (fs, f0, N, a0, p0)
extra_zeros = 1000
#new_signal = np.concatenate((signal, np.zeros(extra_zeros)),axis=0)
new_signal = ins.generador_ruido(10, 1, 2000)
new_tt = np.linspace(0, (N-1)*Ts, N+extra_zeros)
plt.plot(new_tt,new_signal, label='fs+10 Hz')
plt.legend(loc='upper right')
plt.xlabel('Tiempo [t]')
plt.ylabel('Amplitud [V]')
plt.title("Señal: Senoidal")
