f1 = open("input04.txt", "r")
f2 = open("output04.txt", "w")

n, m = [int(i) for i in f1.readline().strip().split()]
path = [i.strip().split() for i in f1.readlines()]

adj = {}
for i in path:
    if(i[0] not in adj):
        adj[i[0]] = [i[1]]
    else:
        adj[i[0]] += [i[1]]

ver = []
for k, v in adj.items():
    if(k not in ver):
        ver.append(k)
    for i in v:
        if(i not in ver):
            ver.append(i)

g = {}
for i in ver:
    if(i in adj):
        g[i] = adj[i]
    else:
        g[i] = []

color = {}
def colorini(ver):
    global color
    for k in ver:
        color[k] = 0

var = "No"
def DFS(G, s):
    global color
    global var
    color[s] = 1
    if(G[s] != []):
        for v in G[s]:
            if(color[v] == 0):
                DFS(G, v)
            elif(color[v] == 1):
                var = "Yes"
                return
            color[v] = 2
        color[s] = 2

"""color 0 means not discovered, color 1 means discovered but not finished process, and 
color 2 means finished the process."""

colorini(ver)
DFS(g, "1")   # here "1" is the starting city.
f2.write(f"{var}")
f1.close()
f2.close()