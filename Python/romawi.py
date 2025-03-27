ro = input()
R = [chr for chr in ro]
sum = 0
for i in range (0, len(R)):
    if R[i] == "I" :
        sum += 1
        for j in range (i+1, len(R)):
            if R[j] == "V" :
                sum -= 2
            elif R[j] == "X" :
                sum -= 2
    elif R[i] == "V" :
        sum+= 5
    elif R[i] == "X" :
        sum += 10
        for j in range (i+1, len(R)):
            if R[j] == "L" :
                sum -= 20
            elif R[j] == "C" :
                sum -= 20
    elif R[i] == "L" :
        sum += 50
    elif R[i] == "C" :
        sum += 100
        for j in range (i+1, len(R)):
            if R[j] == "D" :
                sum -= 200
            elif R[j] == "M" :
                sum -= 200
    elif R[i] == "D":
        sum += 500
    elif R[i] == "M" : 
        sum += 1000
print(sum)