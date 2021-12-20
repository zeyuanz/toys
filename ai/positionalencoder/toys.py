import numpy as np
import math


# create constant 'pe' matrix with values dependant on
# pos and i
max_seq_len = 80
d_model = 200

pe = np.zeros((max_seq_len, d_model))
for pos in range(max_seq_len):
    for i in range(0, d_model, 2):
        pe[pos, i] =  math.sin(pos / (10000 ** ((2 * i)/d_model)))
        pe[pos, i + 1] =  math.cos(pos / (10000 ** ((2 * (i + 1))/d_model)))

print(pe)
