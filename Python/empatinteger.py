def CekInteger (X) :
    if X > 0 :
        print("POSITIF")
    elif X == 0 :
        print("NOL")
    else :
        print("NEGATIF")

def Max(A, B, C, D) :
    N = [A, B, C, D]
    max = N[0]
    for i in range (1, 4) :
        if max < N[i] :
            max = N[i]
        else :
            max = max
    return max
def Min(A, B, C, D) :
    N = [A, B, C, D]
    min = N[0]
    for i in range (1, 4) :
        if min > N[i] :
            min = N[i]
        else :
            min = min
    return min
    
def IsAllPositif (A, B, C, D) :
    if A < 0 or B < 0 or C < 0 or D < 0 :
        return False
    else :
        return True
    
A = int(input())
B = int(input())
C = int(input())
D = int(input())
mo = 0
CekInteger(A)
CekInteger(B)
CekInteger(C)
CekInteger(D)

if IsAllPositif(A, B, C, D) == True :
    print(Max(A, B, C, D))
    print(Min(A, B, C, D))
    mo = (A + B + C + D - Max(A, B, C, D) - Min(A, B, C, D)) / 2
    print("%.2f" %mo)
