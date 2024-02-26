f1 = open("input2.txt", "r")
f2 = open("output2.txt", "w")

n = int(f1.readline().strip())
arr = [int(i) for i in f1.readline().strip().split()]

def bubbleSort(a):
    for i in range(len(a)):
        swap = False
        for j in range(len(a)-1):
            if(a[j] > a[j+1]):
                a[j], a[j+1] = a[j+1], a[j]
                swap = True
            
        if(not swap):
            break
# Here I use swap variable where I assigned swap variable with False. So when the second loop run and the condition 
# is not be fullfiled then the swap has False and for this reason, the time complexity will become Big theta of (n). However,
# when the condition in the second loop fulfilled then the second loop run and in that case the time complexity will
# become big theta of (n^2).
bubbleSort(arr)

for i in range(len(arr)):
    f2.write(str(arr[i])+" ")

f1.close()
f2.close()