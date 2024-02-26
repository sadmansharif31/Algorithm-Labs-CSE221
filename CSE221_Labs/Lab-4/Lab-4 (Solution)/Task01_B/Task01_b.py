f1 = open("input01_b.txt", "r")
f2 = open("output01_b.txt", "w")

n, m = [int(i) for i in f1.readline().strip().split()]
m1 = [[int(j) for j in i.strip().split()]for i in f1.readlines()]

d = {}
for i in range(n+1):
    d[i] = []

for i in m1:
    d[i[0]] += [[i[1], i[2]]]

for k, v in d.items():
    if(v==[]):
        f2.write(f"{k} : \n")
    else:
        s1 = str(k) + " : "
        for i in v:
            list1 = str(i).strip("[]")
            s1 += "(" + list1 + ")" + " "
        s1 += "\n"
        f2.write(s1)

f1.close()
f2.close()