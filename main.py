# Testing
from toolkit import *
import random

# Random DNA string
size = 100
rand = ''.join([random.choice(Nucleotides)
                for i in range(size)])

print(validateSequence(rand))
