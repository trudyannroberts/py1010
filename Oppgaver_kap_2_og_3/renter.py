# -*- coding: utf-8 -*-
"""
Du f ̊ar renter p ̊a innskudd i bank. Opprett variabelen belop = 10 000, som representerer
innskuddet. Bankens rente er 1,85 %. Beløp etter ett  ̊ar er gitt ved formelen:
belop·(1 + 1,85/100) (3.5)
Lag et program som regner ut beløpet p ̊a konto etter 5  ̊ar. Skriv svaret til skjerm formatert
som et flyttall med 2 sifre etter desimalskilletegnet (punktum)
@author: trudy
"""

belop = 10000
rente = 1.85

belop = belop*(1 + rente/100)**5


print(f'Beløp etter fem år = {belop:.2f}')