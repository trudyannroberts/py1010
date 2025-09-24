# -*- coding: utf-8 -*-
"""
Følgende graf består av 5 noder (de blå sirklene med tall), sammenbundet med
streker (Edges). Node 1 er sammenbundet med node 2 og 3. Videre er node 2
sammenbundet med node 1, 3, 4 og 5. Opprett en dictionary med nodenr som
«Keys» og de nodene den gitte noden er sammenbundet med som «Values». Be
bruker oppgi et nodenr i konsollen, hvorpå alle noder som er sammenbundet
med den gitte noden skrives til skjerm.

@author: trudy
"""
graf = { #lager et dictionary
      '1' : [2, 3], #tilegner key 1 verdiene 2 og 3
      '2' : [1, 3, 4, 5],
      '3' : [1, 2, 5],
      '4' : [2, 5],
      '5' : [2, 3, 4]
}

node = input("Skriv et nodenr mellom 1 - 5: ")

print("Node", node, "er sammenbundet med", graf[node]) #usk sqaure brackets for dictionary
