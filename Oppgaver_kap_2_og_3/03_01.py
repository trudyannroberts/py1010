# -*- coding: utf-8 -*-
"""
En Freia-sjokoladeplate veier 200g, og sjokoladeplaten består av 24 ruter. Freia
oppgir følgende næringsinnhold på pakningen: fett = 33, mettet_fett = 19, 
karb = 55, sukker = 54
Skriv et program som ber brukeren oppgi antall sjokoladeruter man har spist, ved
ant_biter = int(input("Skriv inn antall ruter du har spist: "))
Programmet skal regne ut, og så skrive antall kalorier (kcal) man da har fått i seg
til skjerm.

@author: trudy
"""
kcal_per_plate = 552*2
kcal_per_rute = kcal_per_plate/24
ant_biter = int(input("Skriv inn antall ruter du har spist: "))

kcal = kcal_per_rute*ant_biter
print(kcal)