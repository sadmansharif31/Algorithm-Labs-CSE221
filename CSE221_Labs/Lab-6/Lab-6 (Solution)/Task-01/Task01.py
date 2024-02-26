import math
import heapq
f1 = open("input01.txt", "r")
f2 = open("output01.txt", "w")

n, m = [int(i) for i in f1.readline().strip().split()]
path = []
for i in range(m):
    v = [int(i) for i in f1.readline().strip().split()]
    path.append(v)
s = int(f1.readline().strip())

adj = [[] for i in range(n+1)]
for i in path:
    adj[i[0]].append((i[1], i[2]))
    
def dijkstra(G, s):
    distances = [math.inf] * (n+1)
    distances[s] = 0
    
    pq = [(0, s)]
    while(len(pq) != 0):
        dist, node = heapq.heappop(pq)
        for neighbor, weight in G[node]:
            if(distances[neighbor] > dist + weight):
                distances[neighbor] = dist + weight 
                heapq.heappush(pq, (dist+weight, neighbor))
    return distances
    
distance = dijkstra(adj, s)

str1 = ""
for i in range(1, len(distance)):
    if(distance[i] == math.inf):
        str1 += "-1 "
    else:
        str1 += f"{distance[i]} "
f2.write(f"{str1}")

f1.close()
f2.close()