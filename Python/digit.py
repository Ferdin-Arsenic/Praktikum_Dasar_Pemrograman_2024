b_digit = [0]
b_bilangan = 0

while b_bilangan < 100:
    bilangan = int(input())
    if bilangan < 0:
        break
    if bilangan == 0 :
        b_digit[0] += 1
    while bilangan > 0:
        digit = bilangan % 10
        if digit > (len(b_digit) - 1) :
            b_digit.extend([0]*(digit))
            b_digit[digit] += 1
            bilangan //= 10
        elif digit == (len(b_digit) - 1) :
            b_digit.extend([0]*1)
            b_digit[digit] += 1
            bilangan //= 10
        else :
            b_digit[digit] += 1
            bilangan //= 10
    b_bilangan += 1
print(b_bilangan)
if b_bilangan > 0 :
    for digit in range(0,len(b_digit)):
        if b_digit[digit] > 0 :
            print(digit ,":" ,b_digit[digit])