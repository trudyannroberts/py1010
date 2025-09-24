# -*- coding: utf-8 -*-
"""
Utvid koden fra oppgave 9) slik at bruker kan oppgi en bokstav i konsollen,
hvorpå programmet skriver ut 3 bokstaver, dvs bokstaven selv og de to
nabobokstavene. Eksempelvis hvis bokstaven d oppgis i konsollen, skal
bokstavene c d e skrives til skjerm.
Merk: dersom du oppgir bokstaven a eller å vil koden kunne oppføre seg
«unormalt», da man nå befinner seg i endepunktene av alfabetet (dvs listen) og
man mangler en nabobokstav. Du vil senere lære om konsepter som if/else til å
håndtere slike tilfeller.

@author: trudy
"""
import string as st

alfabet = list(st.ascii_lowercase)

print(alfabet)

alfabet.extend(['æ', 'ø', 'å'])

print(alfabet)

valg = input("Velg en bokstav i alfabetet: ")

bokstav = alfabet.index(valg)
print(alfabet[bokstav-1], alfabet[bokstav], alfabet[bokstav+1])

