f1 = open("input01_a.txt", "r")
f2 = open("output01_a.txt", "w")

n, m = [int(i) for i in f1.readline().strip().split()]
m1 = [[int(j) for j in i.strip().split()] for i in f1.readlines()]

l = []
for i in range(n+1):
    l1 = []
    for j in range(n+1):
        l1.append(0)
    l.append(l1)

for i in m1:
    l[i[0]][i[1]] = i[2]

for i in l:
    for j in i:
        f2.write(f"{j} ")
    f2.write(f"\n")

f1.close()
f2.close()