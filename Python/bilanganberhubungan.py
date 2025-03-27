n = int(input())
x = int(input())
a = list(map(int, input("").split()))
l = [0 for i in range (n)]
max = 0
ma = 0
for i in range (n) :
    min = l[0]
mi = 0
count = 0
for i in range (n) :
    if a[i] == x :
        count += 1
    else : 
        count += 0
if count == 0 :
    print("TIDAK ADA")
else : 
    print(x)
for i in range (n) :
    l[i] = abs(a[i] - x)

for i in range (n) :
    min = l[0]

for i in range (n) :
    if min > l[i] and l[i] != 0:
        min = l[i]
        mi = a[i]
    else :
        min = min
        mi = mi

for i in range (n) :
    if max < l[i] :
        max = l[i]
        ma = a[i]
    else :
        max = max
        ma = ma
print(mi)
print(ma)



