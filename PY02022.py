from math import sqrt


def isprime(n):
    if n == 2 or n == 3:
        return True
    if n < 5 or n%2 == 0 or n%3 == 0:
        return False
    for i in range(5, int(sqrt(n)+1), 6):
        if n%i == 0 or n%(i+2) == 0:
            return False
    return True

n = int(input())
list = [int(i) for i in input().split()]
used = []
for i in list:
   if i not in used and isprime(i):
       print(i, list.count(i))
       used += [i] 