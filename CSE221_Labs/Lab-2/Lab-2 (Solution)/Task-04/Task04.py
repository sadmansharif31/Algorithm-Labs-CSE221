import math

f1 = open("input04.txt", "r")
f2 = open("output04.txt", "w")

n = int(f1.readline().strip())
a = [int(i) for i in f1.readline().strip().split()]

def findMax(l):
    if(len(l) <= 1):
        return l
    else:
        m = len(l)//2
        left = l[:m]
        right = l[m:]
        left = findMax(left)
        right = findMax(right)
        return maxValue(left, right)
    
def maxValue(g, h):
    max1 = [-math.inf]
    for i in range(len(g)):
        if(g[i] > max1[0]):
            max1[0] = g[i]
    for j in range(len(h)):
        if(h[j] > max1[0]):
            max1[0] = h[j]
    return max1

k = findMax(a)

f2.write(f"{k[0]}")

f1.close()
f2.close()