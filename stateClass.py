import random

# class state that is either rejected or accepted
# left and right 'nodes' are a and b

class State:

    state = 0
    label = False
    a = None
    b = None

    def __init__(self, state):
        self.state = state
        temp = random.randint(0,1)
        if temp == 0:
            self.label = False
        elif temp != 0:
            self.label = True
        self.a = self
        self.b = self

    #to print a state
    def printSt(self):
        if self.label:
            print("State: ", self.state, "\tLabel: Accepts\ta: State", self.a.state,"\tb: State", self.b.state)
        elif not self.label:
            print("State: ", self.state, "\tLabel: Rejects\ta: State", self.a.state,"\tb: State", self.b.state)


#takes an array of states and links them together through a and b
def connect(dfa):
    length = len(dfa)
    for i in range(length):
        temp = random.randint(0,length-1)
        dfa[i].a = dfa[temp]
        temp = random.randint(0,length-1)
        dfa[i].b = dfa[temp]

#prints all states
def printAll(dfa):
    for i in range(len(dfa)):
        dfa[i].printSt()

visited = []

#recursive function that calculates the depth and fills in the visited array.
def calcDepth(currentState, depth):
    l = 0
    r = 0
    if currentState in visited:
        return depth-1
    else:
        visited.append(currentState)
        l = calcDepth(currentState.a, depth+1)
        r = calcDepth(currentState.b, depth+1)
        if l < r :
            return r 
        else:
            return l

