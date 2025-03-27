x = int(input())
y = int(input())
count = 0
if x > y :
    count = 0
else : 
    for i in range (x, y+1) : 
        if i % 3 == 0 or i % 4 == 0 :
            count += 1
        else :
            count += 0

if count > 0 :
    print(count)
else :
    print("Tidak Ada")