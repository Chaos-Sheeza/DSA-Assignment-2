from stateClass import *
import random

#size = random.randint(16,64)
size = 5
startState = random.randint(0, size-1)
dfa = []

#creating an array of states
for i in range(size):
    temp = State(i+1)
    dfa.append(temp)

#creating the dfa
connect(dfa)
#printing for debugging
printAll(dfa)
#print("Depth = ", calcDepth(dfa[startState]))
print("Depth = ", tocalc(dfa[startState]))
#remStates(dfa, startState, size)
dfa = vis
printAll(dfa)