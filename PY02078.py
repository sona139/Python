for __ in range(int(input())):
    n = int(input())
    a, b = [-1000], [1000]
    for i in range(n):
        enu = input().split()
        a += [float(enu[0])]
        b += [float(enu[1])]
    dp = [0]*(n+1)
    for i in range(1, n+1):
        index = 0
        for j in range(1, i):
            if a[j] < a[i] and b[j] > b[i] and dp[index] < dp[j]:
                index = j
        dp[i] = dp[index]+1
    print(max(dp))