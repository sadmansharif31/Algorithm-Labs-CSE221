f1=open("input2_4.txt","r")
f2=open("output2_4.txt","w")

inp=f1.readline().strip().split()
N,M=int(inp[0]),int(inp[1])
tasks=[]
for i in range(N):
  inp=f1.readline().strip().split()
  S=int(inp[0])
  E=int(inp[1])
  tasks.append([S,E])

tasks.sort(key=lambda x:x[1])

st=tasks[0]
schedule=[[] for i in range(M)]
schedule[0].append(st)
end=[0 for i in range(M)]
end[0]=st[1]
for i in range(1,len(tasks)):
  difference=99999999999
  for j in range(M):
    interval=tasks[i][0]-end[j]
    if end[j]<=tasks[i][0] and interval<difference:
      person=j
      difference=interval
  if difference!=99999999999:
      schedule[person].append(tasks[i])
      end[person]=tasks[i][1]

task_count=0
for x in schedule:
  for y in x:
    task_count+=1
f2.write(str(task_count))

f1.close()
f2.close()