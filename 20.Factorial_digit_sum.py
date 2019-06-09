import time
start = time.time()

def main():
    total = 1
    for i in range(1,100):
        total *= i
    print(total)
    sumtotal = 0
    total = str(total)
    for i in range(len(str(total))):
        sumtotal += int(total[i])
    print(sumtotal)
    
    
main()    

elapsed = time.time() - start
print("Time: {:.5f} seconds".format(elapsed))