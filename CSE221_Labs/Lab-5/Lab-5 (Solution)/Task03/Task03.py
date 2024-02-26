f1 = open("input03.txt", "r")
f2 = open("output03.txt", "w")

n, m = [int(i) for i in f1.readline().strip().split()]
path = [[int(j) for j in i.strip().split()] for i in f1.readlines()]

ver = []
for i in range(1, n+1):
    ver.append(i)
            
adj = {}
for i in path:
    if(i[0] not in adj):
        adj[i[0]] = [i[1]]
    else:
        adj[i[0]] += [i[1]]
for i in ver:
    if(i not in adj):
        adj[i] = ""
        
stack = []
color = {}
def DFS_init(G):
    global color
    global ver
    for u in ver:
        color[u] = 0
    for u in G:
        if(color[u] == 0):
            DFS(G, u)
def DFS(G, s):
    color[s] = 1
    for v in G[s]:
        if(color[v] == 0):
            DFS(G, v)
            if(v not in stack):
                stack.append(v)
    color[s] = 2
    stack.append(s)
DFS_init(adj)

new_adj = {}
for i in path:
    if(i[1] not in new_adj):
        new_adj[i[1]] = [i[0]]
    else:
        new_adj[i[1]] += [i[0]]
for i in ver:
    if(i not in new_adj):
        new_adj[i] = ""
   
  
a = list()
color1 = {}
str1 = ""
def DFS_init1(G):
    global color1
    global ver
    for u in ver:
        color1[u] = 0
    while(len(stack) != 0):
        u = stack.pop()
        DFS1(G, u)   
def DFS1(G, s):
    global a
    global str1
    color1[s] = 1
    if(s not in a):
        a.append(s)
        str1 += str(s) + " "
    for v in G[s]:
        if(color1[v] == 0 and v not in a):
            a.append(v)
            str1 += str(v) + " "
            DFS1(G, v)
    str1 += "\n"
    color1[s] = 2
DFS_init1(new_adj)

str2 = sorted(str1.split("\n"))
for i in range(len(str2)):
    if(len(str2[i]) > 4):
        t = str2[i][0]
        t1 = str2[i][-1:0:-1]
        str2[i] = t+t1
str3 = ""
for i in str2:
    if(i != ""):
        str3 += i + "\n"

f2.write(str3)

f1.close()
f2.close()