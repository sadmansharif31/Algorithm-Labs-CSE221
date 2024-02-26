f1 = open("input3.txt", "r")
f2 = open("output3.txt", "w")

n = int(f1.readline().strip())

si = [int(i) for i in f1.readline().strip().split()]
sm = [int(i) for i in f1.readline().strip().split()]

d = {}
for i in range(n):
    if(sm[i] not in d):
        d[sm[i]] = [si[i]]
    else:
        d[sm[i]] += [si[i]]

def selectionSort(a):    # sorting for students marks
    for i in range(len(a)):
        max_idx = i
        for j in range(i+1, len(a)):
            if(a[max_idx] < a[j]):
                max_idx = j
        a[max_idx], a[i] = a[i], a[max_idx]
selectionSort(sm)

def selectionSort2(a):      # sorting for student ID
    for i in range(len(a)):
        min_idx = i
        for j in range(i+1, len(a)):
            if(a[min_idx] > a[j]):
                min_idx = j
        a[min_idx], a[i] = a[i], a[min_idx]

for k,v in d.items():
    selectionSort2(v)

for i in sm:
    f2.write(f"ID: {d[i][0]} Mark: {i}\n")
    d[i] = d[i][1:]

f1.close()
f2.close()