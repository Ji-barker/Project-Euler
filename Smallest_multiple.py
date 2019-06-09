num = 11*13*17*19
count = 0
yeah = 0
while yeah == 0:
    for i in range(1,21):
        if num%i != 0:
            count += 1
            break
    if count == 0:
        print(num)
        yeah = 1
        break
    else:
        count = 0
        num += 11*13*17*19
