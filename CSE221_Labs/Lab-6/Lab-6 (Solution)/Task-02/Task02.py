import math
import heapq

f1 = open("input02.txt", "r")
f2 = open("output02.txt", "w")

n, m = [int(i) for i in f1.readline().strip().split()]
path = [[int(i) for i in f1.readline().strip().split()] for i in range(m)]
s, t = [int(i) for i in f1.readline().strip().split()]

adj = [[] for i in range(n+1)]
for i in path:
    adj[i[0]].append((i[1], i[2]))
    
def dijkstra(G, s):
    distances = [math.inf]*(n+1)
    distances[s] = 0
    
    q = [(0, s)]
    while(len(q) != 0):
        dist, u = heapq.heappop(q)
        for v, w in G[u]:
            if(distances[v] > dist+w):
                distances[v] = dist+w
                heapq.heappush(q, (dist+w, v))
    return distances

a = dijkstra(adj, s)
b = dijkstra(adj, t)

l = []
for i in range(n+1):
    if(a[i] > b[i]):
        l.append(a[i])
    elif(b[i] > a[i]):
        l.append(b[i])

min_l = [math.inf, 0]
for i in range(len(l)):
    if(l[i] < min_l[0]):
        min_l[0], min_l[1] = l[i], i+1
    
if(min_l[0] == math.inf):
    f2.write("Impossible")
else:
    f2.write(f"Time {min_l[0]}\nNode {min_l[1]}")

f1.close()
f2.close()