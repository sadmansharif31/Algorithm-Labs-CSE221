import math
f1 = open("input_03.txt", "r")
f2 = open("output_03.txt", "w")

n, x = [int(i) for i in f1.readline().strip().split()]
c = [int(i) for i in f1.readline().strip().split()]

def minimum_coin(n, c):
    m = [None]*(n+1)
    m[0] = 0
    for i in range(1, n+1):
        min1 = math.inf
        for j in range(len(c)):
            if(c[j] <= i and 1+m[i-c[j]] < min1):
                min1 = 1+m[i-c[j]]
        m[i] = min1
    return m

v = minimum_coin(x, c)
if(v[x] != math.inf):
    f2.write(f"{v[x]}")
elif(v[x] == math.inf):
    f2.write(f"{-1}")

f1.close()
f2.close()