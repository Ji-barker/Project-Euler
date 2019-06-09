import time
import math
start = time.time()
#time: 1.92652 seconds

def prime_array():
    #array of prime numbers
    array = [2,3]
    step = 0
    i = 5
    comp = 0
    count = 1
    count2 = 2
    while len(array) < 10001:
        # this loop get the next 6n+/-1 number and checks whether it be divided by each prime number in the array, if not it is added to the array
        while step < int(math.sqrt(array[len(array)-1])):
            if i%array[step] == 0 and i != array[step]:
                comp += 1
                step = array[len(array)-1]
            else:
                step += 1
        if comp == 0:
            array.append(i)
        comp = 0

        step = 0
        #prime number can be either 6n +/- 1. Eg 6*1-1=5, 6*1+1=7, 6*2-1=11
        if count2 % 2 != 0:
            i = 6 * count - 1
        else:
            i = 6 * count + 1
            count += 1
        count2 += 1

    print("Answer to the question:", array[len(array)-1])


prime_array()

elapsed = time.time() - start
print("Time: {:.5f} seconds".format(elapsed))


