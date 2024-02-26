f1 = open("input01_b.txt", "r")
f2 = open("output01_b.txt", "w")

n, m = [int(i) for i in f1.readline().strip().split()]
prereq = [[int(j) for j in i.strip().split()] for i in f1.readlines()]

ver = []
for i in range(1, n+1):
    ver.append(i)

adj = {}
for i in prereq:
    if(i[0] not in adj):
        adj[i[0]] = [i[1]]
    else:
        adj[i[0]] += [i[1]]
for i in ver:
    if(i not in adj):
        adj[i] = ""

indeg = [0]*(len(ver)+1)
for k,v in adj.items():
    for i in v:
        indeg[i] += 1

class Queue:
    def __init__(self):
        self.arr = [None]*20
        self.size = 0
        self.front = 0
        self.back = 0
    def enqueue(self, a):
        if(self.size == len(self.arr)):
            return "Overflow"
        self.arr[self.back] = a
        self.back = (self.back+1)%len(self.arr)
        self.size += 1
    def dequeue(self):
        if(self.size == 0):
            return "Underflow"
        t = self.arr[self.front]
        self.arr[self.front] = None
        self.front = (self.front+1)%len(self.arr)
        self.size -= 1
        return t

q = Queue()
visited = {}
for u in ver:
    if(u not in visited):
        visited[u] = 0

list1 = []
def BFS(G, s):
    visited[s] = 1
    q.enqueue(s)
    while(q.size != 0):
        u = q.dequeue()
        for v in G[u]:
            if(visited[v] == 0):
                visited[v] = 1
                if(u not in list1):
                    list1.append(u)
                if(v not in list1):
                    list1.append(v)
                q.enqueue(v)
        visited[u] = 2

for i in ver:
    if(indeg[i] == 0):
        BFS(adj, i)

if(len(list1) == len(ver)):
    f2.write(str(list1).strip("[]").replace(", ", " "))
else:
    f2.write(f"IMPOSSIBLE")
    
f1.close()
f2.close()