from stateClass import *
import random
from Tarjan import *

size = random.randint(16,64)
#size = 5
startState = random.randint(0, size-1)
dfa = []


#creating an array of states
for i in range(size):
    temp = State(i+1)
    dfa.append(temp)

#creating the dfa
connect(dfa)
#printing for debugging
#printAll(dfa)
#print("Depth = ", calcDepth(dfa[startState]))
print("Size of A = ", len(dfa))
temp = tocalc(dfa[startState])
print("Depth of A = ", temp)
#in the line below the start state is the first element in the dfa
dfa = vis
print("Size of A without unreachable states = ", len(dfa), "\n")
#remStates(dfa, startState, size)
#printAll(dfa)

#print(startState)
print(checkWords(genWords(), dfa))

t = Tarjan(dfa)
t.findSccs()

print("\nNumber of SCCs = ",t.sccCount)
s,l = t.sccSize()
print("Smallest SCC = ", s)
print("Largest SCC = ", l)