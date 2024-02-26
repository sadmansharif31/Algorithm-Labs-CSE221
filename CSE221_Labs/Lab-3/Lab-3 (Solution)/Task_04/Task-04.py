f1 = open("input-04.txt", "r")
f2 = open("output-04.txt", "w")

n = int(f1.readline().strip())
a = [int(i) for i in f1.readline().strip().split()]
q = int(f1.readline().strip())
k = f1.readlines()

def partition(a, p, r):
    piv = a[r]
    i = p-1
    for j in range(i+1, r):
        if(a[j] < piv):
            i += 1
            a[i], a[j] = a[j], a[i]
    a[r], a[i+1] = a[i+1], a[r]
    return i+1

def findK(a, p, r, k):
    g = partition(a, p, r)
    if(g == k):
        return a[k]
    if(k>g):
        return findK(a, g+1, r, k)
    else:
        return findK(a, p, g-1, k)
    
for i in range(q):
    f2.write(f"{findK(a, 0, len(a)-1, int(k[i].strip())-1)}\n")

f1.close()
f2.close()