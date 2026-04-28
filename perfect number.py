num = 28
sum_div = 0

for i in range(1, num):
    if num % i == 0:
        sum_div += i

print(sum_div == num)  # True