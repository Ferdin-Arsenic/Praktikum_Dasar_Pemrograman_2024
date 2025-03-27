def valid(n) :
    if 0 < n <= 100 :
        return True
    else :
        return False 
n = int(input())
min = 0
count = 0
valid(n)
if valid(n) == True :
    a = list(map(int, input("").split()))
    x = int(input())
    b = [0]
    for i in range(n):
        for j in range(i+1, n):
            if a[i] > a[j] :
                k = a[i]
                a[i] = a[j]
                a[j] = k
            else : 
                a[i] = a[i]
                a[j] = a[j]
    for i in range (n) :
        if b[0] == 0 :
            if a[i] > x :
                b[0] = a[i]
        else :
            if a[i] > x :
                b.append(a[i])
    if len(b) >= 2 :
        print(b[1])
    else :
        print("-1")
else :
    print("Tidak valid")

