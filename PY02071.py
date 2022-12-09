def Try(n:int, l:list, sum:int, s:int):
    if sum == n:
        global ress
        ress.append(tuple(l))
        return
    for i in range(s, 0, -1):
        Try(n, l+[i], sum+i, i)
        

for _ in range(int(input())):
    n = int(input())
    ress = []
    Try(n, [], 0, n)
    print(len(ress))
    for res in ress:
        print('(', end='')
        print(*res, end='')
        print(')', end=' ')
    print()