#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 21:06:34 2019

@author: IVAN.GERCENSZTEIN
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


modulo0, fase0, ww0 = ins.analizador_espectro(signal0, fs)
modulo1, fase1, ww1 = ins.analizador_espectro(signal1, fs)
modulo2, fase2, ww2 = ins.analizador_espectro(signal2, fs)
modulo3, fase3, ww3 = ins.analizador_espectro(signal3, fs)


sum0 = ins.sumatoria_modulo_cuadrado(np.delete(modulo0, 250))
sum1 = ins.sumatoria_modulo_cuadrado(np.delete(modulo1, 250))
sum2 = ins.sumatoria_modulo_cuadrado(np.delete(modulo2, 250))
sum3 = ins.sumatoria_modulo_cuadrado(np.delete(modulo3, 250))



#x0,y0 = ins.get_max_index(modulo0)
#x1,y1 = ins.get_max_index(modulo1)
#x2,y2 = ins.get_max_index(modulo2)
#x3,y3 = ins.get_max_index(modulo3)



#plt.figure("Analizador espectro")
#
#plt.subplot(2,1,1)
#plt.title("Modulo y fase señal")
#
#plt.plot(ww0, modulo0, label='fs/4')
#plt.plot(ww1, modulo1, label='+ 0.1')
#plt.plot(ww2, modulo2, label='+ 0.25')
#plt.plot(ww3, modulo3, label='+ 0.5')
#
#plt.legend(loc='upper right')
#plt.grid()
#plt.xlabel("Frecuencia")
#plt.ylabel("Amplitud")
#
#plt.subplot(2,1,2)
#plt.xlabel("Frecuencia")
#plt.ylabel("Fase")
#plt.plot(ww0, fase0, "co", label='fs/4')
#plt.plot(ww1, fase1, "go", label='+ 0.1')
#plt.plot(ww2, fase2, "bo", label='+ 0.25')
#plt.plot(ww3, fase3, "ro", label='+ 0.5')
#plt.legend(loc='upper right')
#plt.grid()
#plt.tight_layout()



