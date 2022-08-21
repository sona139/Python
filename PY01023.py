from math import sqrt

def divisible(i):
    global num
    cnt = 0
    while num%i == 0:
        num /= i
        cnt += 1
    return cnt

def deff (i):
    global num, res
    if num%i:
        return
    res += [f'{int(i)}^{divisible(i)}']
    

for case in range(int(input())):
    num = int(input())
    res = ['1']
    deff(2)
    deff(3)
    i = 5
    while i <= sqrt(num):
        deff(i)
        deff(i+2)
        i += 6
    if num > 1:
        deff(num)
    print(' + '.join(res))