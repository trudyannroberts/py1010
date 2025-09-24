# -*- coding: utf-8 -*-
"""
Omkretsen på en friidrettsbane er 400 meter. Gitt at man har løpt 5 km. Lag et
program som skriver ut antall hele runder man da har løpt, og hvor mange meter
man kom inn i den siste runden.
Hint: les om funksjonen divmod()
Test koden din for løpeturer av ulik lengde, og verifiser at svarene er fornuftige.
@author: trudy
"""

# Constants
track_length = 400  # length of one lap in meters
distance_run = 5000  # total distance run in meters (5 km)

# Calculate number of full laps and remaining distance
laps, remaining_distance = divmod(distance_run, track_length)

# Print the results
print(f"Antall hele runder: {laps}")
print(f"Meters inn i siste runde: {remaining_distance}")