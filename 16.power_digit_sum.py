import time
import math

start = time.time()


#print((2**1000*(2**1000+1))//2)
def main():
    num = str(2**1000)
    total = 0
    for i in range(len(num)):
        total += int(num[i])
    print(total)


main()

elapsed = time.time() - start
print("Time: {:.5f} seconds".format(elapsed))
