f1 = open("input01_a.txt", "r")
f2 = open("output01_a.txt", "w")

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

stack = []
color = {}
def DFS_init(G, ver):
    global color
    global indeg
    for u in ver:
        if(u not in color):
            color[u] = 0
    for u in G:
        if(color[u] == 0 and indeg[u] == 0):
            DFS(G, u)
def DFS(G, s):
    global color
    global stack
    color[s] = 1
    for v in G[s]:
        if(color[v] == 0):
            DFS(G, v)
            if(v not in stack):
                stack.append(v)
            if(s not in stack):
                stack.append(s)
    color[s] = 2

DFS_init(adj, ver)

ans = stack[-1::-1]

if(len(stack) == len(ver)):
    f2.write(str(ans).strip("[]").replace(", ", " "))
else:
    f2.write(f"IMPOSSIBLE")

f1.close()
f2.close()