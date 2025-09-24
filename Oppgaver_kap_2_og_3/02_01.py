# -*- coding: utf-8 -*-
"""
Anta at du har et forbruksl ̊an (L) p ̊a kr 100 000 med rentesats (r) 23,4 % 
pr  ̊ar. Hvis du ikke betaler noe avdrag, hvor mye (kr) betaler 
du da i rente pr m ̊aned (R)? Finn svaret ved
 ̊a bruke Python som kalkulator, b ̊ade med beregning med bare tall og 
med beregning med bruk av variable (bokstavsymboler).
Created on Fri Oct 18 21:50:36 2024

@author: trudy
"""

L = 100000
r = 23.4
R = ((L*r)/100)/12
print("Rente pr mnd:", R)