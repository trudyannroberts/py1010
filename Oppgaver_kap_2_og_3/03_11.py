# -*- coding: utf-8 -*-
"""
Gitt følgende problemstilling: du har en liste a = [1.3, 2, 2.5, 2.7, 3, 5.1, 4.3, 17],
og du vil finne ut om listen er perfekt sortert eller ikke. I realiteten kan liste a
bestå av tusenvis av elementer, men her ser vi på en forenklet versjon. Begge de
innebygde funksjonene sort() og sorted() kan brukes til å sortere lister, og er
dermed egnet til å løse problemstillingen over. Skriv to programmer, ett ved bruk
av sort() og et ved bruk av sorted() til å løse problemstillingen over. Programmene
skal skrive True til skjerm dersom liste a i utgangspunktet fremstod som sortert,
og False dersom a i utgangspunktet ikke fremstod som sortert.

@author: trudy
"""

#bruk av sort
a = [1.3, 2, 2.5, 2.7, 3, 5.1, 4.3, 17]
b = a.copy() #vi må lage en kopi av a, siden sort overskriver originalen
a.sort()
resultat = a == b
print("Der er", resultat, "at listen i utgangspunktet var sortert")

#bruk av sorted
a = [1.3, 2, 2.5, 2.7, 3, 5.1, 4.3, 17]
b = sorted(a) # b opprettes direkte som en egen liste
resultat = a == b
print("Der er", resultat, "at listen i utgangspunktet var sortert")