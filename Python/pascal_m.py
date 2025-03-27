def segi3_psc(N, M):
    segi3 = [[M]]
    for i in range(1, N):
        prev_row = segi3[-1]
        new_row = [M]
        for j in range(1, i):
            new_row.append(prev_row[j-1] + prev_row[j])  
        new_row.append(M) 
        segi3.append(new_row)
    return segi3

def print_segi3(segi3):
    for row in segi3:
        print(*row)

N = int(input())
M = int(input())

generate = segi3_psc(N, M)
print_segi3(generate)