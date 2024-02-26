f1=open("input1_3.txt","r")
f2=open("output1_3.txt","w")

inp=f1.readline().strip().split()
N=int(inp[0])
tasks=[]
for i in range(N):
  inp=f1.readline().strip().split()
  S=int(inp[0])
  E=int(inp[1])
  tasks.append([S,E])

tasks.sort(key=lambda x:x[1])

schedule=[]
temp=tasks[0]
schedule.append(temp)
for i in range(1,len(tasks)):
  if temp[1]<=tasks[i][0]:
    schedule.append(tasks[i])
    temp=tasks[i]

task_count=len(schedule)

f2.write(str(task_count))
f2.write("\n")

for x in schedule:
  a=str(x[0])
  b=str(x[1])
  f2.write(f"{a} {b} \n")

f1.close()
f2.close()