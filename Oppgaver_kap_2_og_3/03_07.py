# -*- coding: utf-8 -*-
"""
Denne oppgaven er litt krevende. Gjenta oppgave 6), men koden skal oppdateres
slik at man unngår veivalg av typen 2 -> 1 -> 2 eller 5 -> 4 -> 5. Dette betyr at
startnoden ikke må forekomme som sluttnode.

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
#Fjerner node_start fra mulige kandidater blandt disse naboene
naboer.remove(int(node_start))
node_slutt = naboer[0] #velger neste node til å være den som ligger på index 0)
print("En mulig rute er",node_start,"->", node_neste, "->", node_slutt)