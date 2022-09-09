def Try(s, a, b, c, d, n):
    if len(s) == n and s[len(s)-1] != '2' and a > 0 and b > 0 and c > 0 and d > 0: print(s)
    elif len(s) < n:
        Try(s + '2', a+1, b, c, d, n)
        Try(s + '3', a, b+1, c, d, n)
        Try(s + '5', a, b, c+1, d, n)
        Try(s + '7', a, b, c, d+1, n)

for i in range(4, int(input())+1):
    Try('', 0, 0, 0, 0, i)