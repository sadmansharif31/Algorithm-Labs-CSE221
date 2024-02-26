f1=open("input3_2.txt","r")
f2=open("output3_2.txt","w")

inp=f1.readline().strip().split()
N,K=int(inp[0]),int(inp[1])
Q=[]
for i in range(K):
  inp=f1.readline().strip().split()
  A=int(inp[0])
  B=int(inp[1])
  Q.append([A,B])

X=[[i] for i in range(1,N+1)]

def find(arr,ls):
  for i in arr:
    if ls in i:
      return i

for i in Q:
    a=find(X,i[0])
    b=find(X,i[1])
    if a!=b:
        new=a+b
        X.remove(a)
        X.remove(b)
        X.append(new)
        count=len(new)
        f2.write(str(count))
        f2.write("\n")
    else:
       count=len(a)
       f2.write(str(count))
       f2.write("\n")


f1.close()
f2.close()