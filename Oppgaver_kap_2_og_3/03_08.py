# -*- coding: utf-8 -*-
"""
I Python vil 1 < 4 < 5 være True, mens 4 < 1 < 5 er False. Lag et program som ber
bruker taste inn et 3-sifferet-tall i konsollen ved bruk av følgende kommando:
bruker_liste = list(input("skriv inn et 3-sifferet tall: "))
I programmet skal man så undersøke om det er True eller False om sifrene er
oppgitt i stigende rekkefølge, og svaret skrives til skjerm med passende tekst.
Merk: dersom brukeren nå taster inn tallet 527 blir bruker_liste= ['5', '2', '7'].

@author: trudy
"""
bruker_liste = list(input("skriv inn et 3-sifret tall: "))

resultat = bruker_liste[0] < bruker_liste[1] < bruker_liste[2]

print("Står sifrene i stigende rekkefølge?", resultat)