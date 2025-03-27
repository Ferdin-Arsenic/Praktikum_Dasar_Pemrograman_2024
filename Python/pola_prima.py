def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def buat_prima(N):
    prima = []
    num = 2
    while len(prima) < N:
        if is_prime(num):
            prima.append(num)
        num += 1
    return prima

def buat_persegi(N, prima):
    persegi = [[''] * N for i in range(N)]
    diagonal_index = 0
    for i in range(N):
        for j in range(N):
            if i == j:
                persegi[i][j] = str(prima[diagonal_index])
            elif i > j:
                persegi[i][j] = str(prima[i - j])
            else:
                persegi[i][j] = str(prima[j - i])
    return persegi

def print_square(persegi):
    for row in persegi:
        print(" ".join(row))

N = int(input(""))

if N < 1:
    print("Tidak valid")
else:
    prima = buat_prima(N)
    persegi = buat_persegi(N, prima)
    print_square(persegi)