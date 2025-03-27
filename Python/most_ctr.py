n = int(input())
a = list(map(int, input().strip().split()))
b = []
c = []
numb = 0
list = ""
count = 0
max = 0
for i in range (n) :
    for j in range (i + 1, n) :
        if a[i] > a[j] :
            k = a[i]
            a[i] = a[j]
            a[j] = k
        else :
            a[i] = a[i]
            a[j] = a[j]
numb = a[0]
for i in range (n) :
    if numb == a[i] :
        count += 1
        if i == n-1 :
            i += 0
        else : 
            i += 1
    else : 
        b.append(count)
        c.append(numb)
        count = 1
        numb = a[i]
b.append(count)
c.append(numb)
max = b[0]
for i in range (len(b)) :
    if max < b[i] :
        max = b[i]
    else :
        max = max
for i in range (len(b)) :
    if max == b[i] :
        break
print(c[i])
    


