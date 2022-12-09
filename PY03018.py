for _ in range(int(input())):
    n, m = map(int, input().split())
    a = []
    for i in range(n):
        a.append([int(i) for i in input().split()])
    
    dp = [[0]*m for _ in range(n)]
    dp[0][0] = a[0][0]
    for i in range(1, n):
        dp[i][0] = dp[i-1][0] + a[i][0]
    for j in range(1, m):
        dp[0][j] = dp[0][j-1] + a[0][j]
        
    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = min(abs(dp[i-1][j]-a[i][j]), abs(dp[i-1][j-1]-a[i][j]), abs(dp[i][j-1]-a[i][j]))
    
    print(dp[n-1][m-1])