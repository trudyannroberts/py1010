# -*- coding: utf-8 -*-
"""
Denne oppgaven er litt krevende. Gjenta oppgave 5), men nå skal programmet
skrive ut en «to-stegs vei» fra noden man oppgir i konsollen. Eksempel: oppgir
brukeren node 2 vil en mulig «to-stegs vei» være 2 -> 4 -> 5.
Merk1: det finnes fler «to-stegs veier» fra node 2, men det er tilstrekkelig at
programmet skriver ut en slik «to-stegs vei».
Merk2: dersom koden din eksempelvis skulle skrive ut veien 2 -> 1 -> 2, så anses
dette som en gyldig vei.

@author: trudy
"""

graf ={
"1": [2, 3],
"2": [1, 3, 4, 5],
"3": [1, 2, 5],
"4": [2, 5],
"5": [2, 3, 4]
}
node_start = input("Oppgi en node: ")
naboer = graf[node_start] #finner naboer
node_neste = naboer[0] #velger neste node til å være den som ligger på index 0)
naboer = graf[str(node_neste)] #Finner de nye naboene

node_slutt = naboer[0] #velger neste node til å være den som ligger på index 0)
print("En mulig rute er",node_start,"->", node_neste, "->", node_slutt)