import math
f1 = open("input-02.txt", "r")
f2 = open("output-02.txt", "w")

n = int(f1.readline().strip())
a = [int(i) for i in f1.readline().strip().split()]

def maxPossible(a):         # following the Sir process
    if(len(a)==1):
        return -math.inf
    if(len(a)==2):
        return a[0]+a[1]**2
    
    left = maxPossible(a[:len(a)//2])
    right = maxPossible(a[len(a)//2:])
    mid = max(a[:len(a)//2]) + max([abs(i) for i in a[len(a)//2:]])**2

    return max(left, right, mid)

k = maxPossible(a)

f2.write(f"{k}")

f1.close()
f2.close()