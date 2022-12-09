from math import sqrt


def isPrime(n):
    if n == 2 or n == 3:
        return True
    if n < 5 or n%2 == 0 or n%3 == 0:
        return False
    for i in range(5, int(sqrt(n))+1, 6):
        if n%i == 0 or n%(i+2) == 0:
            return False
    return True

n = int(input())
ar = [int(i) for i in input().split()]
list = []
for i in ar:
    if i not in list:
        list.append(i)
sum_left, sum_right = 0, sum(list)

res = -1
for i in range(len(list)):
    sum_left += list[i]
    sum_right -= list[i]
    if isPrime(sum_left) and isPrime(sum_right):
        res = i
        break
print(res if res != -1 else 'NOT FOUND')