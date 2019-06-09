"""The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million."""

import time
start = time.time()

def main():
    count = 13
    answer = [0, 0]
    while count < 1000000:
        total = 0
        num1 = count
        while num1 != 1:
            if num1%2 == 0:
                num1 = num1/2
            else:
                num1 = 3*num1 + 1
            total += 1
        if total > answer[1]:
            answer[1] = total
            answer[0] = count
        count += 1
    print("number:",answer[0])
    print("chain length:", answer[1])



main()

elapsed = time.time() - start
print("Time: {:.5f} seconds".format(elapsed))
