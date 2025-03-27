
count_parentheses = 0
count_square_brackets = 0
count_curly_brackets = 0
string = input()
tdkv = 0
A = [chr for chr in string ]
for i in range (0, len(A)) :
        if A[i] == '(':
            count_parentheses += 1
        elif A[i] == ')':
            count_parentheses -= 1
            if count_parentheses < 0:
                tdkv += 1
        elif A[i] == '[':
            count_square_brackets += 1
        elif A[i] == ']':
            count_square_brackets -= 1
            if count_square_brackets < 0:
                tdkv += 1
        elif A[i] == '{':
            count_curly_brackets += 1
        elif A[i] == '}':
            count_curly_brackets -= 1
            if count_curly_brackets < 0:
                tdkv += 1

if count_parentheses == 0 and count_square_brackets == 0 and count_curly_brackets == 0:
    print("valid")
elif count_parentheses > 0 or count_square_brackets > 0 or count_curly_brackets > 0:
    tdkv += 1
if tdkv > 0 :
    print("tidak valid")