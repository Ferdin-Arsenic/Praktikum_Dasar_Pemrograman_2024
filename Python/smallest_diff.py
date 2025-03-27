n = int(input())
a = list(map(int, input().strip().split()))
b = []
for i in range (n) :
    for j in  range (i + 1, n) :
        out = abs(a[i] - a[j])
        b.append(out)
min = b[0]
for i in range (len (b)) :
    if min > b[i] :
        min = b[i]
    else :
        min = min
print(min)