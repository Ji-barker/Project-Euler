
def sum_squares(num):
    total = 0
    for i in range(1, num+1):
        total += i**2
    return total


def square_sum(num):
    total = 0
    for i in range(1, num+1):
        total += i
    total = total**2
    return total


num = 100
print(sum_squares(num))
print(square_sum(num))
print(square_sum(num)-sum_squares(num))
