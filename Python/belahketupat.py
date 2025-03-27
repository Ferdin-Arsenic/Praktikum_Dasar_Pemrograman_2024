# Program BelahKetupat
# Input: N : integer
# Output: Jika N > 0 dan ganjil, gambar belah ketupat sesuai dengan N
#         Jika tidak, tampilkan pesan kesalahan: Masukan tidak valid
def GambarSegitiga(N) :
# I.S. N > 0 dan N ganjil
# F.S. Gambar belah ketupat dengan panjang diagonal mendatar sebesar N
    for i in range (1, N +1, 2) :
        if N == 1 : 
            print('*')
        else :
            print (' ' * ((N - i)//2) + '*' * (i))
            if i == N :
                for i in range (N - 2, 0, -2) :
                    print (' ' * ((N - i)//2) + '*' * (i))
def isValid(N) :
    # menghasilkan true jika N positif dan ganjil, false jika tidak
    if N > 0 and N % 2 != 0 :
        return True
    else :
        return False
#ALGORITMA PROGRAM UTAMA
N = int(input())
if isValid(N) == True :
    GambarSegitiga(N)
else :
    print("Masukan tidak valid")