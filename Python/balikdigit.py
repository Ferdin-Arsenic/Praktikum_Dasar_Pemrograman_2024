angka = str(input())
D = [chr for chr in angka]
A = ["*" for i in range (len (D))]
a = ""
if int(angka) < 0 :
    for i in range (0, len(D)) :
        if i == 0 :
            A[0] = D[0]
        else :
            A[i] = D[(len(D) - i)]
        a += str(A[i])
elif int(angka) >= 0 :
    for i in range (0, len(D)) :
        A[i] = D[(len(D) - 1) - i]
        a += str(A[i])
print(int(a))
        