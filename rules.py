import Generator
import numpy as np
import time

'''seed'''
seed = str(time.time())
# seed = "aboab"

'''Image'''
'''
boundary:
    Правило, указывающее на способ обработки границы:
        fill - дополняет входные массивы значением заполнения. (по умолчанию)
        wrap - круговые граничные условия.
        symm - симметричные граничные условия.
'''
height = 200
width = 200
boundary = "wrap"
# boundary = "fill"
# boundary = "symm"
