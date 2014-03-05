def factorial(x):
    if x == 0 or x == 1:
        return 1
    else:
        return x * factorial(x - 1)

def digit_Sum(x):
    x_str = str(x)
    digit_sum = 0

    for i in x_str:
        digit_sum += int(i)

    return digit_sum

x = factorial(100)
print digit_Sum(x)