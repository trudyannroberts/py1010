# -*- coding: utf-8 -*-
"""
Finn informasjon om numpy-funksjonene ceil og floor. Skriv en kort forklaring, og vis ved et
kort kodeeksempel hva disse funksjonen gjør.

@author: trudy
"""
import numpy as np

arr = [.5, 1.5, 2.5, 3.5, 4.5, 10.1] 
print ("Input array : \n", arr) 
  
ceiloff_values = np.ceil(arr)
print ("\nRounded up (ceil) : \n", ceiloff_values) 

flooroff_values = np.floor(arr)
print (" Rounded down (floor): \n", flooroff_values)
