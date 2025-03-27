def GambarBTercermin(N) :
    for i in range (1, N +1, 2) :
        if N == 1 : 
            print('*')
        else :
            print (' ' *(i-1) + '*' * (N - i + 1))
            if i == N :
                for i in range (N-2, 0, -2) :
                    print (' ' * (i-1) + '*' * (N-i + 1))
def isValid(N) :
    if N > 0 and N % 2 != 0 :
        return True
    else :
        return False
N = int(input())
if isValid(N) == True :
    GambarBTercermin(N)
else :
    print("Masukan tidak valid")