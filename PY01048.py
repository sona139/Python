from math import sqrt

for _ in range(int(input())):
    n = int(input())*2
    res = sum([i if n%i == 0 and (n//i-i)&1 else 0 for i in range(2, int(sqrt(n))+1)])
    print(res)
