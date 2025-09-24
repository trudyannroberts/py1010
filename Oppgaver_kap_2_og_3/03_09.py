# -*- coding: utf-8 -*-
"""
Følgende kode leser inn det engelske alfabetet, og lagrer dette i form av en liste
ved navn alfabet:
import string as st
# Leser inn alfabetet
alfabet = list(st.ascii_lowercase)
Utvid denne listen slik at bokstavene æ, ø, å legges til i listen alfabet

@author: trudy
"""
import string as st

alfabet = list(st.ascii_lowercase)

print(alfabet)

alfabet.extend(['æ', 'ø', 'å'])

print(alfabet)