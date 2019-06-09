"""The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million"""
#Time: 121.43211 seconds
import time
import math
start = time.time()


def prime_array():
    array = [2,3]
    step = 0
    comp = 0
    count2 = 2
    total = 5
    while True:
        if count2 % 2 == 0:
            i = 6 * int(count2/2) - 1
        else:
            i = 6 * int(count2/2) + 1
        count2 += 1
        while step < array[len(array)-1]:
            if i%array[step] == 0 and i != array[step]:
                comp += 1
                break
            else:
                step += 1
        if comp == 0 and i < 2000000:
            array.append(i)
            total += i
        elif i > 2000000:
            return total
        comp = 0
        step = 0





        #6n +/- 1 = a prime number

#int(math.sqrt(array[len(array)-1]))


print(prime_array())
elapsed = time.time() - start
print("Time: {:.5f} seconds".format(elapsed))
#142913828922