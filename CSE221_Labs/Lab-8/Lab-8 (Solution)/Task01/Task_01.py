f1 = open("input_01.txt", "r")
f2 = open("output_01.txt", "w")

n, m = [int(i) for i in f1.readline().strip().split()]
path = [[int(j) for j in i.strip().split()] for i in f1.readlines()]
path.sort(key = lambda x:x[2])

ver = []
for i in range(1, n+1):
    ver.append(i)
      
# Using Kruskal Algorithm concept as sir said.  
set1 = []
for i in ver:
    set1.append([i])

def find(a, e):
    for i in a:
        for j in i:
            if(j == e):
                return i
        
result = []    
for i in path:
    a = find(set1, i[0])
    b = find(set1, i[1])
    if(a != b):
        new = a + b
        set1.remove(a)
        set1.remove(b)
        set1.append(new)
        result.append(i)

sum1 = 0
for i in result:
    sum1 += i[2]

f2.write(str(sum1))

f1.close()
f2.close()