
class Tarjan:

    UNVISITED = -1
    n = 0
    g = []
    id = 0 #for each node
    sccCount = 0

    ids = [0]
    low = [0]
    onStack = [False]
    stack = []

    def __init__(self, dfa):
        size = len(dfa)
        self.n = size
        self.g = dfa
        self.id = 0 #for each node
        self.sccCount = 0

        self.ids = [0]*size
        self.low = [0]*size
        self.onStack = [False]*size
        self.stack = []

    def findSccs(self):
        for i in range(self.n): self.ids[i] = self.UNVISITED
        for i in range(self.n): 
            if(self.ids[i] == self.UNVISITED):
                self.dfs(i)
        return self.low

    def dfs(self, at):
        self.stack.append(at)
        self.onStack[at] = True
        self.id+=1
        self.ids[at] = self.low[at] = self.id

        to = self.g.index(self.g[at].a)
        if(self.ids[to] == self.UNVISITED): self.dfs(to)
        if(self.onStack[to]): self.low[at] = min(self.low[at],self.low[to])

        to = self.g.index(self.g[at].b)
        if(self.ids[to] == self.UNVISITED): self.dfs(to)
        if(self.onStack[to]): self.low[at] = min(self.low[at],self.low[to])
        
        if(self.ids[at] == self.low[at]):
            for i in range(len(self.stack)):
                node = self.stack.pop()
                self.onStack[node] = False
                self.low[node] = self.ids[at]
                if(node == at): break
            self.sccCount+=1

    def sccSize(self):
        small = self.n
        large = 1
        checked = []
        for x in self.low:
            if not x in checked:
                counter = 0
                checked.append(x)
                for y in self.low:
                    if x == y: counter+=1
                if counter<small: small=counter
                if counter>large: large=counter
        return small,large