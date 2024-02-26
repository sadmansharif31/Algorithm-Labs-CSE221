import math

f1 = open("input05.txt", "r")
f2 = open("output05.txt", "w")

n, m, d1 = [i for i in f1.readline().strip().split()]
path = [i.strip().split() for i in f1.readlines()]

d = {}  # adjacency list
for i in path:
    if(i[0] not in d):
        d[i[0]] = [i[1]]
    else:
        d[i[0]] += [i[1]]
    if(i[1] not in d):
        d[i[1]] = [i[0]]
    else:
        d[i[1]] += [i[0]]

class Queue:
    def __init__(self):
        self.arr = [None]*20
        self.front = 0
        self.back = 0
        self.size = 0
    def enqueue(self, e):
        if(self.size == len(self.arr)):
            return "Overflow"
        else:
            self.arr[self.back] = e
            self.back = (self.back+1)%len(self.arr)
            self.size += 1
    def dequeue(self):
        t = ""
        if(self.size == 0):
            return "Underflow"
        else:
            t = self.arr[self.front]
            self.arr[self.front] = None
            self.front = (self.front+1)%len(self.arr)
            self.size -= 1
        return t

q = Queue()

t = {}
pred = {}
def BFS(G, s):
    q.enqueue(s)
    global t
    global pred
    for k,v in G.items():
        if(s == k):
            t[k] = 0
        else:
            t[k] = math.inf
    pred[s] = "0"
    while(q.size != 0):
        u = q.dequeue()
        for v in G[u]:
            if(t[v] == math.inf):
                t[v] = t[u]+1
                pred[v] = u
                q.enqueue(v)
BFS(d, "1")   # here "1" is the starting city which is given.

l = [d1]
n = d1
while(n != "0"):
    n = pred[n]
    l.append(n)
l1 = [int(i) for i in l][-2::-1]

s = ""
for i in l1:
    s += f"{i} "

f2.write(f"Time: {t[d1]}\n")
f2.write(f"Shortest Path: {s}")

f1.close()
f2.close()