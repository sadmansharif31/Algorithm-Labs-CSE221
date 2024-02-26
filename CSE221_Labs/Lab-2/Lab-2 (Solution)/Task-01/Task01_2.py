f1 = open("input01.txt", "r")
f2 = open("output01.txt", "w")

m = f1.readline().strip()
l = f1.readline().strip()

n, s = [int(i) for i in m.split()]
a = [int(i) for i in l.split()]

def find(a, s, n):    # I use a function where I try to find the two numbers which summation is equal to s.
    d = {}            # By using this function we can get our desired result in time coplexity of O(N).
    for i in range(n):
        num = s - a[i]
        if(num in d):
            return d[num]+1, i+1
        d[a[i]] = i
    return "IMPOSSIBLE."

k = find(a, s, n)
if(k == "IMPOSSIBLE."):
    f2.write(k)
else:
    f2.write(f"{k[0]} {k[1]}")
    

f1.close()
f2.close()