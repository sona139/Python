n = int(input())
str = [input() for _ in range(n)]
double_str = [i+i for i in str]

def solve(s):
    cnt = 0
    for i in double_str:
        try:
            cnt += i.index(s)
        except ValueError:
            return 9999999
    return cnt

res = 9999999
for s in str:
    res = min(res, solve(s))
print(res if res < 999999 else -1)