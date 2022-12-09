if __name__ == '__main__':
    primes = [1]*10011
    primes[0] = primes[1] = 0
    for i in range(2, 105):
        if primes[i]:
            for j in range(i*i, 10011, i):
                primes[j] = 0
    res = [0]*10011
    res[0] = 2
    for i in range(1, 10011):
        if not primes[i]:
            res[i] = res[i-1]+1
    
    for i in range(10009, 1, -1):
        if not primes[i]:
            res[i] = min(res[i], res[i+1]+1)
    
    n = int(input())
    list = [res[int(i)] for i in input().split()]
    print(max(list))