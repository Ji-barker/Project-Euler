

def palindrome_check(string):
    middle = int(len(string)/2+1)
    found = 0

    if middle != int:
        middle -= 0.5

    for i in range(int(middle)):
        if string[i] != string[len(string)-i-1]:
            found = 1
            break
        else:
            found = 0
    return found


found = 0
turn = 0
x = y = 999
temp = 0
while found != 1:
    answer = x * y

    while y >= 100:
        while x >= 100:
            answer = x * y
            if palindrome_check(str(answer)) == 0:
                if answer > temp:
                    temp = answer

                break
            x -= 1
        x = 999
        y -= 1
    break
print(temp)


"""
def palindrome_check(string):
    middle = int(len(string)/2+1)
    found = 0

    if middle != int:
        middle -= 0.5

    for i in range(int(middle)):
        if string[i] != string[len(string)-i-1]:
            found = 1
            break
        else:
            found = 0
    return found


def factor(num):
    for i in range(2, int(num/2)):
        if num%i == 0:
            print(i, int(num/i))

found = 1
x = y = 999
answer = x*y
while found != 0:
    if palindrome_check(str(answer)) == 0:
        factor(answer)
    else:
        answer -= 1

"""



