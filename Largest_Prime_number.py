
def closest_prime(x):
    y = x
    count = int(x/2)
    comp = 0
    for a in range(2, count):
        if y % a == 0 and y != a and y >= 0:
            comp += 1
        if comp >= 2:
            print("comp", y)
            break
    if comp < 2:
        print("prime", y)
        return y


def factor_num(num):
    stop = int(num/2)
    for i in range(2, stop):
        if num%i == 0:
            if closest_prime(num/i) is not None:
                print(closest_prime(num/i))
                break


factor_num(600851475143)
