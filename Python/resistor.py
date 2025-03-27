a = float(input())
b = float(input())
c = float(input())
r = str(input())
RT = 0
if r == 's' or r == 'S' :
    RT = a + b + c
elif r == 'p' or 'P' :
    RT = (a*b*c) / (b*c + a*c + a*b)
print(RT)