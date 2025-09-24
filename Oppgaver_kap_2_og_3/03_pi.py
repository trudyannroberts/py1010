# -*- coding: utf-8 -*-
"""
Lag et program som tar r (radius) for ei kule som input fra kommandolinjen og regner ut
overflaten og volumet til kula. Svaret skrives til skjerm. (Vi antar at du finner fram til
formelen for overflate og volum til ei kule

@author: trudy
"""
import numpy as np
r = int(input("Gi radius for ei kule: "))

overflate = (4*r*math.pi
volum = (r/3)*math.pi

print("Overflate er", overflate)
print("Volum er", volum)

#dette er feil