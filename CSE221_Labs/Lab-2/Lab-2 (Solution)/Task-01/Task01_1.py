f1 = open("input01.txt", "r")
f2 = open("output01.txt", "w")

m = f1.readline().strip()
l = f1.readline().strip()

n, s = [int(i) for i in m.split()]
a = [int(i) for i in l.split()]

f = False
for i in range(n):
    for j in range(i+1, n):
        if(a[i] + a[j] == s):
            f2.write(f"{i+1} {j+1}")
            f = True
    if(f):
        break
if(not f):
    f2.write("IMPOSSIBLE.")

f1.close()
f2.close()