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
def connect(arr):
    length = len(arr)
    for i in range(length):
        temp = random.randint(0,length-1)
        arr[i].a = arr[temp]
        temp = random.randint(0,length-1)
        arr[i].b = arr[temp]

#prints all states
def printAll(arr):
    for i in range(len(arr)):
        arr[i].printSt()
