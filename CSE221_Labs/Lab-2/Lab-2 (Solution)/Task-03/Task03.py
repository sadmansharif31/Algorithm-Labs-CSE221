f1 = open("input03.txt", "r")
f2 = open('output03.txt', "w")

n = int(f1.readline().strip())
a = [int(i) for i in f1.readline().strip().split()]

def merge(a, b):
    merged = []
    i = 0
    j = 0
    while(i < len(a) and j < len(b)):
        if(a[i] < b[j]):
            merged.append(a[i])
            i += 1
        else:
            merged.append(b[j])
            j += 1
    merged += a[i:]
    merged += b[j:]
    return merged

def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
        a1 = mergeSort(left)
        a2 = mergeSort(right)
        return merge(a1, a2)
    
k = mergeSort(a)

f2.write(str(k).strip("[]").replace(", ", " "))

f1.close()
f2.close()