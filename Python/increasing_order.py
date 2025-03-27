def found (n, y) :
    countn = 0 
    for x in range (len(y)):
        if n == y[x] :
            countn += 1
    return countn
n = int(input())
a = list(map(int, input().strip().split()))
count = 0
urut = []
for i in range (n) :
    urut.append(a[i])
for i in range (n) :
    for j in range (i + 1, n) :
        if urut[i] > urut[j] :
            k = urut[i]
            urut[i] = urut[j] 
            urut[j] = k
        else :
            urut[i] = urut[i]
            urut[j] = urut[j]
while a != urut and count < n:
    k = a[len(a)-1]
    a.remove(a[len(a)-1])
    a.insert(0,k)
    count += 1
if a != urut:
    print("Tidak")
elif a == urut :
    print(count)

