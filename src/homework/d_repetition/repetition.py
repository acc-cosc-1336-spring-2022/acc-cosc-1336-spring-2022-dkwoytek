

def get_factorial(num):
    factorial = 1
    for index in range(1, num):
        factorial = factorial * (index + 1)
    return factorial

def sum_odd_numbers(num2):
    sum = 0
    index = 0
    while index <= num2:
        if index % 2 != 0:
            sum = sum + index
        index = index + 1
    return sum
