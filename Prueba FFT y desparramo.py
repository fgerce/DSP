# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 21:06:34 2019

@author: IVAN.GERCENSZTEIN
"""
from Modulos.instrumentos import *


N  = 1000 # muestras
fs = 1000 # Hz

a0 = 1 # Volts
p0 = 0 # radianes

f0 = 400
f1 = 400 + 0.1
f2 = 400 + 0.2
f3 = 400 + 0.3
f4 = 400 + 0.4
f5 = 400 + 0.5   
"Generador de señal"
tt0, signal0 = generador_senoidal (fs, f0, N, a0, p0)
tt1, signal1 = generador_senoidal (fs, f1, N, a0, p0)
tt2, signal2 = generador_senoidal (fs, f2, N, a0, p0)
tt3, signal3 = generador_senoidal (fs, f3, N, a0, p0)
tt4, signal4 = generador_senoidal (fs, f4, N, a0, p0)
tt5, signal5 = generador_senoidal (fs, f5, N, a0, p0)

"Graficador temporal, esto solo tiene sentido para frecuencias muy bajas."
"En el orden de fs/10 ya se rompe todo"
"""
plt.plot(tt,signal)
plt.legend(loc='upper right')
plt.xlabel('Tiempo [t]')
plt.ylabel('Amplitud [V]')
plt.title("Señal: Senoidal")
"""

plt.figure("Analizador espectro")

plt.subplot(2,1,1)
plt.title("Modulo y fase señal")

modulo0, fase0, ww0 = analizador_espectro(signal0, fs)
modulo1, fase1, ww1 = analizador_espectro(signal1, fs)
modulo2, fase2, ww2 = analizador_espectro(signal2, fs)
modulo3, fase3, ww3 = analizador_espectro(signal3, fs)
modulo4, fase4, ww4 = analizador_espectro(signal4, fs)
modulo5, fase5, ww5 = analizador_espectro(signal5, fs)

plt.plot(ww0, modulo0, label='fs')
plt.plot(ww1, modulo1, label='+ 0.1')
plt.plot(ww2, modulo2, label='+ 0.2')
plt.plot(ww3, modulo3, label='+ 0.3')
plt.plot(ww4, modulo4, label='+ 0.4')
plt.plot(ww5, modulo5, label='+ 0.5')

plt.legend(loc='upper right')
plt.grid()
plt.xlabel("Frecuencia")
plt.ylabel("Amplitud")

plt.subplot(2,1,2)
plt.xlabel("Frecuencia")
plt.ylabel("Fase")
plt.plot(ww, fase0, "co")
plt.plot(ww, fase1, "go")
plt.plot(ww, fase2, "bo")
plt.plot(ww, fase3, "ro")
plt.plot(ww, fase4, "yo")
plt.plot(ww, fase5, "mo")
plt.legend(loc='upper right')
plt.grid()
plt.tight_layout()



