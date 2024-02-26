import math
import heapq

f1 = open("input03.txt", "r")
f2 = open("output03.txt", "w")

n, m = [int(i) for i in f1.readline().strip().split()]
path = [[int(j)  for j in i.strip().split()] for i in f1.readlines()]

adj = [[] for i in range(n+1)]
for i in path:
    adj[i[0]].append((i[1], i[2]))

def danger(G, s, n):   # using modified dijkstra algorithm
    distances = [math.inf]*(n+1)
    distances[s] = 0
    
    q = [(0, s)]
    while(len(q) != 0):
        danger1, u = heapq.heappop(q)
        
        if(u == n):
            return danger1
        
        for v, danger in G[u]:
            danger2 = max(danger1, danger)
            if(danger2 < distances[v]):
                distances[v] = danger2
                heapq.heappush(q, (danger2, v))
    return "Impossible"

l = danger(adj, 1, n)

f2.write(f"{l}")

f1.close()
f2.close()