f1 = open("input02.txt", "r")
f2 = open("output02.txt", "w")

n = int(f1.readline().strip())
a = [int(i) for i in f1.readline().strip().split()]

m = int(f1.readline().strip())
b = [int(i) for i in f1.readline().strip().split()]

list1 = []
i = 0
j = 0
while(i < len(a) and j < len(b)):
    if(a[i] < b[j]):
        list1.append(a[i])
        i += 1
    else:
        list1.append(b[j])
        j += 1
list1 += a[i:]
list1 += b[j:]

f2.write(str(list1).strip("[]").replace(", ", " "))

f1.close()
f2.close()