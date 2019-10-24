#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 00:54:03 2019

@author: fede
"""
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from numpy.fft import fft, fftshift
import scipy.signal as sig

N = 60 # muestras
fftSize = 2048

ventanas = [sig.boxcar(N), sig.bartlett(N), sig.hann(N), sig.blackman(N), sig.flattop(N)]
ventanas_names = ["rectangular", "bartlett", "hanning", "blackman", "flattop"]
V = len(ventanas_names)
plt.figure("Ventanas", figsize = (10,10))

for (vv, this_win) in zip(ventanas_names, ventanas):
       plt.plot(this_win, label=vv)
plt.legend()
plt.grid()       
plt.xlabel("Numero de muestra")
plt.ylabel("Amplitud de la ventana")
plt.title("Forma de ventanas")


complexMat = np.transpose(np.vstack([fft(thisWin,fftSize, axis=0) for thisWin in ventanas]))
#fft(signal, size) Si size > len(signal) la FFT le hace zero padding automaticamente :)
moduleMat = np.abs(complexMat)
for ii in range (V):
       moduleMat[:,ii] = moduleMat[:,ii] / np.max(moduleMat[:,ii])
#Aplico un fftshift para que quede centrada en el 0, y obtengo el modulo del resultado
freq = np.linspace(-0.5, 0.5, len(moduleMat[:,0]))

#Genero el vector de frecuencias normalizadas, entre -0.5 y 0.5 de longitud de mi vector
response = 20*np.log10(moduleMat)
#Escalo a dB
response = np.clip(response, -200, 10)
#Recorto valores por debajo de los -200dB
plt.figure("Modulo de las ventanas", figsize = (10,10))
plt.title("Respuesta en frecuencia de las ventanas")

lim = int(np.floor(fftSize/2))
response = response[0:lim, :]
freq = freq[lim:fftSize]

BW = np.zeros(V)
for ii in range (V):
       plt.plot(freq, response[:,ii], label=ventanas_names[ii])
#       Obtengo los anchos de banda buscando los valores menores al max*raiz(2)/2
#       Y luego me quedo con el primer elemento, por eso el [0][0]
       BW[ii] = np.where(moduleMat[:,ii] <= np.max(moduleMat[:,ii])*np.sqrt(2)/2)[0][0]
       BW[ii] = freq[int(BW[ii])]

plt.legend()
plt.grid()
plt.ylim(-150,10)
plt.xlabel("Frecuencia normalizada")
plt.ylabel("Modulo normalizado [dB]")  


#for ii in range(V):
#       peaks = sig.find_peaks(response[:, ii])[0][:]
#       peaks = peaks/fftSize
#       ww = np.ones(len(peaks))
#       plt.figure("Modulo de las ventanas")
#       plt.plot(peaks, ww, '-X')
#       
#      

#diff = np.diff(moduleMat, axis=0)
#
#first_zero = np.zeros(V)
#second_max = np.zeros(V)
#frec_zero = np.zeros(V)
#
#for ii in range(V):
#       first_zero[ii] = np.where(diff[:,ii] > 0)[0][20]
#       plt.figure("3")
#       plt.plot(freq[int(np.floor(first_zero[ii])):lim], response[int(np.floor(first_zero[ii])):lim, :])
#       second_max[ii] = np.max(response[int(np.floor(first_zero[ii])):lim, :])
        