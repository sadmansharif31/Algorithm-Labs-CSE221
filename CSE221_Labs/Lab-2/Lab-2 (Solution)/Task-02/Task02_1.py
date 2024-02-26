f1 = open("input02.txt", "r")
f2 = open("output02.txt", "w")

n = f1.readline().strip()
a = [int(i) for i in f1.readline().strip().split()]

m = f1.readline().strip()
b = [int(i) for i in f1.readline().strip().split()]

l = a+b
def mergeSort(a):
    if(len(a) <= 1):
        return a
    m = len(a)//2
    left = a[:m]
    right = a[m:]
    left = mergeSort(left)
    right = mergeSort(right)
    return merge(left, right)

def merge(l, r):
    merged = []
    i = 0
    j = 0
    while(i < len(l) and j < len(r)):
        if(l[i] < r[j]):
            merged.append(l[i])
            i += 1
        else:
            merged.append(r[j])
            j += 1
    merged += l[i:]
    merged += r[j:]
    return merged

k = mergeSort(l)

f2.write(str(k).strip("[]").replace(", ", " "))

f1.close()
f2.close()