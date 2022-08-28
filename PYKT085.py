n = int(input())
list = [''] + [input().replace('\\n', '\n') for i in range(n)]
md = dict()
for i, s in enumerate(list):
    if s.strip() == '':
        str = list[i+1]
        md[str] = -1
    else: md[str] += 1

set = md.keys()
for i in set:
    print(f'{i}: {md[i]}')