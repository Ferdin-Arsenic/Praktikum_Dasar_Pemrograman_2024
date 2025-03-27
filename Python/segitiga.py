# Ferdin Arsenarendra Purtadi / 19623090

#Program GambarSegitiga
#Input : N integer

def GambarSegitiga(N) :
    for i in range (1, N +1, 2) :
        if N == 1 : 
            print('*')
        else :
            print (' ' * (N - i) + '*' * (i))
            if i == N :
                for i in range (N - 2, 0, -2) :
                    print (' ' * (N - i) + '*' * (i))
def isValid(N) :
    if N > 0 and N % 2 != 0 :
        return True
    else :
        return False
N = int(input())
if isValid(N) == True :
    GambarSegitiga(N)
else :
    print("Masukan tidak valid")