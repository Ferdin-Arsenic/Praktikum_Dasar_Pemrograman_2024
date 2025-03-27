ip = float(input())
pot = float(input())
k = 0
if ip >= 3.5 :
    k = 4
elif pot < 1 and ip < 3.5 :
    k = 1
elif 1 <= pot < 5 and ip < 3.5 :
    if ip >= 2 :
        k = 3
    else : 
        k = 2
else : 
    k = 0
print(k)