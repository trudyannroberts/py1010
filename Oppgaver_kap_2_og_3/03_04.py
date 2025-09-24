# -*- coding: utf-8 -*-
"""
På en standard terning vil alltid tallene (dvs antall øyne) være ordnet parvis på en
slik måte at tallene 1 og 6 står på motsatte sider av terningen, 2 og 5 er på
motsatte sider og 3 og 4 er på motsatte sider. Lag et program hvor brukeren
skriver inn antall øyne som vises på oppsiden av terningen etter et terningkast
(du behøver ikke foreta et reelt terningkast ). Programmet skal så skrive ut «Du
slo en toer» dersom det var tallet 2 du oppgav i konsollen. Videre skal koden også
skrive ut «Siden som ligger ned er en femmer».
Hint: opprett en dictionary til å holde orden på mappingen 1 -> «ener», 2-> «toer»
og så videre

@author: trudy
"""

terning = {
"1": "ener",
"2": "toer",
"3": "treer",
"4": "firer",
"5": "femmer",
"6": "sekser"}

kast = input("Hva viser oppsiden av terningen? ")
tekst_oppside = terning[kast]
print("Du slo en", tekst_oppside)

nedside = 7-int(kast)
tekst_nedside = terning[str(nedside)]
print("Siden som ligger ned er en", tekst_nedside)