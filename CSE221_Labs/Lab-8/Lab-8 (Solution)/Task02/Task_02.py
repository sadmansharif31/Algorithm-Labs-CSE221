f1 = open("input_02.txt", "r")
f2 = open("output_02.txt", "w")

n = int(f1.readline().strip())

a = [None]*(n+1)
def ways(k, a):
    if(k == 0 or k == 1):
        a[k] = 1
    if(a[k] == None):
        a[k] = ways(k-1, a) + ways(k-2, a)
    return a[k]
v = ways(n, a)
    
f2.write(f"{v}")
    
f1.close()
f2.close()