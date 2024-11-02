# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 16:31:09 2024

@author: Trudy Ann Roberts

Obligatorisk oppgave 1
"""
km = 10000  # [km per år]
elForsikring = 5000  # [elbilforsikring per år]
benForsikring = 7500  # [bensinbilforsikring per år]
forsAvgift = 8.38 * 365  # [trafikkforsikringsavgift per år]

# Beregning av årlig drivstoffkostnad for elbil
elDrivstoff = 0.2 * km * 2.00  # [kWh/km * km/år * kr/kWh]

# Beregning av årlig drivstoffkostnad for bensinbil
benDrivstoff = 1.0 * km  # [kr per år]

elBom = 0.1 * km  # [bomavgift for elbil]
benBom = 0.3 * km  # [bomavgift for bensinbil]

# Totale kostnader
elbilTotal = elForsikring + forsAvgift + elDrivstoff + elBom
bensinbilTotal = benForsikring + forsAvgift + benDrivstoff + benBom
differanse = bensinbilTotal - elbilTotal

print("Totalkostnader for elbil:", elbilTotal, "kr")
print("Totalkostnader for bensinbil:", bensinbilTotal, "kr")
print("Årlig kostnadsdifferanse:", differanse, "kr")