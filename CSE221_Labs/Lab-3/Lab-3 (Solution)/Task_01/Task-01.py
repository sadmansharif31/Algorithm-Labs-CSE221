f1 = open("input-01.txt", "r")
f2 = open("output-01.txt", "w")

n = int(f1.readline().strip())
h = [int(i) for i in f1.readline().strip().split()]

count = 0
def divide(a):
    if(len(a) <= 1):
        return a
    mid = len(a)//2
    left = a[:mid]
    right = a[mid:]
    a1 = divide(left)
    a2 = divide(right)
    return counting(a1, a2)

def counting(left, right):
    global count
    merged = []
    i = 0
    j = 0
    while(i < len(left) and j < len(right)):
        if(left[i] > right[j]):
            merged.append(right[j])
            count += len(left[i:])
            j += 1
        else:
            merged.append(left[i])
            i += 1
    merged += left[i:]
    merged += right[j:]
    return merged

divide(h)

f2.write(str(count))

f1.close()
f2.close()