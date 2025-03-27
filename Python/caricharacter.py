n = int(input())
A = []
B = []
count = 0
while n <= 0 or n> 100 :
    print("Masukan salah. Ulangi!")
    n = int(input())
for i in range (n) :
    A.append(str(input()))
    B.append(ord(A[i]))
cc = str(input())
if cc == 'S' or cc == 's' :
    for i in range (n) :
        if 97 <= B[i] <= 127 :
            break
        count += 1
    if count == len(A) :
        print("Tidak ada huruf kecil")
elif cc == 'L' or cc == 'l' :
    for i in range (n) :
        if 65 <= B[i] <= 90 :
            break
        else :
            count += 1
    if count == len(A) :
        print("Tidak ada huruf besar")
elif cc == 'X' or cc == 'x' :
    for i in range (n) :
        if 90 < B[i] < 97 or B[i] < 65 or B[i]>127 :
            break
        else : 
            count += 1
    if count == len(A) :
        print("Semua huruf")
else :
    print("Tidak diproses")
if i != n-1 :
    print(i+1, A[i])