CHICKEN = ['1', '3', '5', '7', '9']

def deff(s):
    for i in s:
        if i in CHICKEN:
            return ''
    return s + s[::-1] + ' '

for case in range(int(input())):
    num = input()
    num = int(num[:(len(num)+1)//2])
    i = 1
    while i < num:
        s = str(i)
        i += 1
        print(deff(s), end='')
    print()