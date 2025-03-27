def count_operations(num):
    operations = 0
    while num >= 10:
        sum_of_digits = sum(int(digit) for digit in str(num))
        num = sum_of_digits
        operations += 1
    return operations

N = int(input())
a = list(map(int, input("").split()))

total_operations = 0
for num in a:
    total_operations += count_operations(num)

print(total_operations)