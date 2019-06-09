"""A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc."""
#Time: 0.27834 seconds
import time
import math

start = time.time()
a = 1
b = 2
i = 1000
answer = "no"
for a in range(1,i):
    for b in range(2,i):
        if -(a + b - 1000) == math.sqrt(a**2+b**2):
            print(a,b,1000-a-b)
            answer = "yes"
            break

    if answer == "yes":
        break

elapsed = time.time() - start
print("Time: {:.5f} seconds".format(elapsed))


