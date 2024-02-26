f1 = open("input03.txt", "r")
f2 = open("output03.txt", "w")

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

color = {}
l = []
def colorInitializing(G):
    global color
    for u in G.keys():
        color[u] = 0

def DFS(G, s):
    global color
    global l
    color[s] = 1
    for v in G[s]:
        if(color[v] == 0):
            if(s not in l):
                l.append(s)
            l.append(v)
            DFS(G, v)

colorInitializing(d)
DFS(d, "1") # here "1" is the starting city which is given.

l1 = [int(i) for i in l]
f2.write(str(l1).strip("[]").replace(", ", " "))
f1.close()
f2.close()