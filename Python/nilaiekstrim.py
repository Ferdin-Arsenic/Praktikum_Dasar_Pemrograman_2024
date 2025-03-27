n = int(input())
A = []
count = 0
for i in range (n) :
    A.append(int(input()))
min = A[0]
max = A[0]
x = int(input())
for i in range (n) :
    if max < A[i] :
        max = A[i]
    else :
        max = max
    if min > A[i] :
        min = A[i]
    else : 
        min = min
    if x == A[i] :
        count += 1
    else :
        count += 0
if count == 0 :
    print(x, "tidak ada")
else :
    if x == max :
        print("maksimum")
    if x == min :
        print("minimum")
    if x != max and x != min :
        print("N#A")
