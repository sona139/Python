l = [len(input().split()) for i in range(int(input()))]
res = []
i = 0
while i < len(l):
    if i < len(l) and l[i] == 7:
        res += [2]
        i += 4
    if i < len(l) and l[i] == 6:
        res += [1]	
        while i < len(l) and l[i] == 6:
            i += 2
print(len(res), *res, sep='\n')