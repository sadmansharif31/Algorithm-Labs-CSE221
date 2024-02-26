f1 = open("input1a.txt", "r")
f2 = open("output1a.txt", "w")

T = int(f1.readline().strip())

for i in range(T):
    current_num = int(f1.readline().strip())
    if(current_num % 2 == 0):
        f2.write(f"{current_num} is an Even number.\n")
    else:
        f2.write(f"{current_num} is an Odd number.\n")

f1.close()
f2.close()