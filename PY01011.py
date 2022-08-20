CHICKEN = ['1', '3', '5', '7', '9']

def deff(s):
    for i in s:
        if i in CHICKEN:
            return ''
    return s + s[::-1] + ' '

for case in range(int(input())):
    num = int(input())
    i = 1
    while True:
        s = str(i)
        if int(s + s[::-1]) >= num:
            break
        i += 1
        print(deff(s), end='')
    print()