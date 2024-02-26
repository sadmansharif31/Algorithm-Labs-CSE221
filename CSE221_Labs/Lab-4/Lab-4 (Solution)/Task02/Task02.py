f1 = open("input02.txt", "r")
f2 = open("output02.txt", "w")

n, m = [int(i) for i in f1.readline().strip().split()]
road = [i.strip().split() for i in f1.readlines()]

d = {}  # adjacency list
for i in road:
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

l = []
color = {}
def BFS(G, s):
    global l
    global color
    for u in G.keys():
        color[u] = 0
    color[s] = 1
    q.enqueue(s)
    l.append(s)
    while(q.size != 0):
        u = q.dequeue()
        for v in G[u]:
            if(color[v] == 0):
                color[v] = 1
                q.enqueue(v)
                l.append(v)
BFS(d, "1")  # here "1" is the starting city which is given.

l1 = [int(i) for i in l]
f2.write(str(l1).strip("[]").replace(", ", " "))

f1.close()
f2.close()