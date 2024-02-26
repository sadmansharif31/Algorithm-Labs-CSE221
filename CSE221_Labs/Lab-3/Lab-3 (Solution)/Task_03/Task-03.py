f1 = open("input-03.txt", "r")
f2 = open("output-03.txt", "w")

n = int(f1.readline().strip())
a = [int(i) for i in f1.readline().strip().split()]

def quickSort(a, p, r):
    if(p < r):
        q = partition(a, p, r)
        quickSort(a, p, q-1)
        quickSort(a, q+1, r)
    return a

def partition(a, p, r):
    piv = a[r]
    i = p-1
    for j in range(i+1, r):
        if(piv > a[j]):
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i+1], a[r] = a[r], a[i+1]
    return i+1

k = quickSort(a, 0, len(a)-1)
f2.write(str(k).strip("[]").replace(", ", " "))

f1.close()
f2.close()