# -*- coding: utf-8 -*-
"""

Lag et (lite) Python-program der du bruker time og sleep (f.eks. kan programmet brukes til
 ̊a sjekke om sleep faktisk fungerer som forventet). Tips: Koden t0 = time.time() gir
variabelen t0 verdi lik antall sekunder som har g ̊att fra det s ̊akalte epoch-tidspunktet, som
er definert i dokumentasjonen for time-funksjonen. Obs: For  ̊a gjøre modulen time
tilgjengelig i dine programmer m ̊a du importere modulen.

"""
import time

"""Returns the current time in seconds since the Unix epoch (January 1, 1970)"""
t0 = time.time()
print(t0, "sekunder siden 1. jan. 1970")
print("Hello...")

""""The sleep function pauses the program for x amount of seconds"""
time.sleep(3)
print("... Are you there?")
