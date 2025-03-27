def found (n, y) :
    countn = 0 
    for x in range (len(y)):
        if n == y[x] :
            countn += 1
    return countn
    
n = int(input())
a = []
b = []
count = 1
while n != -9999 :
    a.append(n)
    n = int(input())
for i in range (len(a)) :
    for j in range (1,len(a)) :
        if j != i :
            out = a[i] + a[j]
        b.append(out)

for i in range (len(b)) :
    for j in range (i+1, len(b)) :
        if b[i] > b[j] :
            k = b[i]
            b[i] = b[j]
            b[j] = k
        else : 
            b[i] = b[i]
            b[j] = b[j]

i = 1
for i in range (1, 50000) :
    if found (i, a) == 0 and found (i, b) == 0 :
        print(i)
        break
    else :
        i += 1

