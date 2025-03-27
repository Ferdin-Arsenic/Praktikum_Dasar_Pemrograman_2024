a = ord(str(input()))
b = ord(str(input()))
out = 0
if 65 <= a <= 90 and 65 <= b <= 90 :
    if abs(a - b) > 13 :
        out = 26 - abs(a-b)
    else :
        out = abs(a-b)
    print(out)
else :
    print("Tidak valid")