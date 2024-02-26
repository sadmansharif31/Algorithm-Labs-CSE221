f1 = open("input1b.txt", "r")
f2 = open("output1b.txt", 'w')

T = int(f1.readline().strip())

for i in range(T):
    current = f1.readline().strip().split()
    if("." not in current[1] and "." not in current[3]):
        if(current[2] == "+"):
            f2.write(f"The result of {current[1]} + {current[3]} is {int(current[1]) + int(current[3])}\n")
        elif(current[2] == '-'):
            f2.write(f"The result of {current[1]} - {current[3]} is {int(current[1]) - int(current[3])}\n")
        elif(current[2] == "*"):
            f2.write(f"The result of {current[1]} * {current[3]} is {int(current[1]) * int(current[3])}\n")
        elif(current[2] == "/"):
            f2.write(f"The result of {current[1]} / {current[3]} is {int(current[1]) / int(current[3])}\n")
    elif("." in current[1] and "." not in current[3]):
        if(current[2] == "+"):
            f2.write(f"The result of {current[1]} + {current[3]} is {float(current[1]) + int(current[3])}\n")
        elif(current[2] == '-'):
            f2.write(f"The result of {current[1]} - {current[3]} is {float(current[1]) - int(current[3])}\n")
        elif(current[2] == "*"):
            f2.write(f"The result of {current[1]} * {current[3]} is {float(current[1]) * int(current[3])}\n")
        elif(current[2] == "/"):
            f2.write(f"The result of {current[1]} / {current[3]} is {float(current[1]) / int(current[3])}\n")
    elif("." in current[3] and "." not in current[1]):
        if(current[2] == "+"):
            f2.write(f"The result of {current[1]} + {current[3]} is {int(current[1]) + float(current[3])}\n")
        elif(current[2] == '-'):
            f2.write(f"The result of {current[1]} - {current[3]} is {int(current[1]) - float(current[3])}\n")
        elif(current[2] == "*"):
            f2.write(f"The result of {current[1]} * {current[3]} is {int(current[1]) * float(current[3])}\n")
        elif(current[2] == "/"):
            f2.write(f"The result of {current[1]} / {current[3]} is {int(current[1]) / float(current[3])}\n")
    elif("." in current[1] and "." in current[3]):
        if(current[2] == "+"):
            f2.write(f"The result of {current[1]} + {current[3]} is {float(current[1]) + float(current[3])}\n")
        elif(current[2] == '-'):
            f2.write(f"The result of {current[1]} - {current[3]} is {float(current[1]) - float(current[3])}\n")
        elif(current[2] == "*"):
            f2.write(f"The result of {current[1]} * {current[3]} is {float(current[1]) * float(current[3])}\n")
        elif(current[2] == "/"):
            f2.write(f"The result of {current[1]} / {current[3]} is {float(current[1]) / float(current[3])}\n")
        

f1.close()
f2.close()