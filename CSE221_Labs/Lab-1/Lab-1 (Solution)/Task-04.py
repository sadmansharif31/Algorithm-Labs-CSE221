f1 = open("input4.txt", "r")
f2 = open("output4.txt", 'w')

n = int(f1.readline().strip())

s = f1.readlines()

l = []
for i in s:
    l.append(i.strip().split())

def nameSort(a):     # selection sort have been used for name sorting
    for i in range(len(a)):
        min_idx = i
        for j in range(i+1, len(a)):
            if(a[min_idx][0] > a[j][0]):    # As the name of the train is at index 0 so I give the index 0
                min_idx = j
        a[min_idx], a[i] = a[i], a[min_idx]
nameSort(l)

for i in range(len(l)-1):
    if(l[i][0] == l[i+1][0]):    # As the name of the train is in the 0 index
        if(l[i][-1] < l[i+1][-1]): # As the departure time of the train is in the last index or in negative index -1.
            l[i], l[i+1] = l[i+1], l[i]

s = ""
for i in l:
    for j in range(len(i)):
        if(j != len(i)-1):
            s += i[j] + " "
        else:
            s += i[j] + "\n"
    f2.write(s)
    s = ""

f1.close()
f2.close()