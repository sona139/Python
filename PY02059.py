from math import sqrt

def isPrime(n):
    if n < 2: return False
    for i in range(2, int(sqrt(n)+1)):
        if not n%i:
            return False
    return True

n, m = [int(i) for i in input().split()]
mt = []
for i in range(n):
    mt += [[int(i) for i in input().split()]]
num = 0
for i in mt:
    for j in i:
        if isPrime(j):
            num = max(num, j)
if num == 0: print('NOT FOUND')
else:
    print(num)
    for i in range(n):
        for j in range(m):
            if mt[i][j] == num:
                print('Vi tri [{}][{}]'.format(i, j))