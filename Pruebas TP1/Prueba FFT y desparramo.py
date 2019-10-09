#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 21:06:34 2019

@author: fede
"""
from Modulos import instrumentos as ins

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

N  = 1000 # muestras
fs = 1000 # Hz

a0 = 1 # Volts
p0 = 0 # radianes

f0 = fs/4
f1 = f0 + 0.01
f2 = f0 + 0.25
f3 = f0 + 0.5
   
"Generador de señal"
tt0, signal0 = ins.generador_senoidal (fs, f0, N, a0, p0)
tt1, signal1 = ins.generador_senoidal (fs, f1, N, a0, p0)
tt2, signal2 = ins.generador_senoidal (fs, f2, N, a0, p0)
tt3, signal3 = ins.generador_senoidal (fs, f3, N, a0, p0)

"Graficador temporal, esto solo tiene sentido para frecuencias muy bajas."
"En el orden de fs/10 ya se rompe todo"
"""
plt.plot(tt,signal)
plt.legend(loc='upper right')
plt.xlabel('Tiempo [t]')
plt.ylabel('Amplitud [V]')
plt.title("Señal: Senoidal")
"""
modulo0, fase0, ww0 = ins.analizador_espectro(signal0, fs)
modulo1, fase1, ww1 = ins.analizador_espectro(signal1, fs)
modulo2, fase2, ww2 = ins.analizador_espectro(signal2, fs)
modulo3, fase3, ww3 = ins.analizador_espectro(signal3, fs)

f0_0 = 20*np.log10(modulo0[int(f0)])
f0_1 = 20*np.log10(modulo1[int(f0)])
f0_2 = 20*np.log10(modulo2[int(f0)])
f0_3 = 20*np.log10(modulo3[int(f0)])

fady_0 = 20*np.log10(modulo0[int(f0+1)])
fady_1 = 20*np.log10(modulo1[int(f0+1)])
fady_2 = 20*np.log10(modulo2[int(f0+1)])
fady_3 = 20*np.log10(modulo3[int(f0+1)])

sum_resto_frecuencias0 = ins.sumatoria_modulo_cuadrado(modulo0) - modulo0[int(f0)]
sum_resto_frecuencias1 = ins.sumatoria_modulo_cuadrado(modulo1) - modulo1[int(f0)]
sum_resto_frecuencias2 = ins.sumatoria_modulo_cuadrado(modulo2) - modulo2[int(f0)]
sum_resto_frecuencias3 = ins.sumatoria_modulo_cuadrado(modulo3) - modulo3[int(f0)]


plt.figure("Analizador espectro")

plt.subplot(2,1,1)
plt.title("Modulo y fase señal")

plt.plot(ww0, modulo0, label='fs')
plt.plot(ww1, modulo1, label='+ 0.1')
plt.plot(ww2, modulo2, label='+ 0.2')
plt.plot(ww3, modulo3, label='+ 0.3')

plt.legend(loc='upper right')
plt.grid()
plt.xlabel("Frecuencia")
plt.ylabel("Amplitud")

plt.subplot(2,1,2)
plt.xlabel("Frecuencia")
plt.ylabel("Fase")
plt.plot(ww0, fase0, "co")
plt.plot(ww1, fase1, "go")
plt.plot(ww2, fase2, "bo")
plt.plot(ww3, fase3, "ro")
plt.legend(loc='upper right')
plt.grid()
plt.tight_layout()



