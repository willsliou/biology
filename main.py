# Testing
from toolkit import *
import random


# Random DNA string
rand = ''.join([random.choice(Nucleotides)
                for i in range(20)])

print(validateSequence(rand))
