a = int(input())
b = int(input())
c = int(input())
maks = 0
if a >= b and a >= c :
    maks = a
elif a <= b and b>= c:
    maks = b
else :
    maks = c
print(maks)
