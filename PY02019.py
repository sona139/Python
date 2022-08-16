from math import gcd


n = int(input())
list = [int(i) for i in input().split()]
list.sort()
for i in range(0, len(list)):
    for j in range(i+1, len(list)):
        if gcd(list[i], list[j]) == 1:
            print(list[i], list[j])