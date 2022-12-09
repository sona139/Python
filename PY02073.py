for _ in range(int(input())):
    n = int(input())
    x, y, z = [int(i) for i in input().split()]
    dp = [0]*(n+1)
    dp[1] = x
    for i in range(2, n+1):
        dp[i] = min(dp[i-1]+x, dp[i//2]+z if i%2 == 0 else dp[(i+1)//2]+z+y)
    print(dp[n])