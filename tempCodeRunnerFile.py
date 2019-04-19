from stateClass import *
import random

size = random.randint(16,64)
dfa = []

for i in range(size):
    temp = State(i+1)
    dfa.append(temp)

connect(dfa)
printAll(dfa)