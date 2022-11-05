n = int(input())
str = [input() for _ in range(n)]
double_str = [i+i for i in str]

def solve(s):
    cnt = 0
    for i in double_str:
        index = i.index(s)
        if index == -1:
            return 9999999
        cnt += index
    return cnt

res = 9999999
for s in str:
    res = min(res, solve(s))
print(res if res < 999999 else -1)