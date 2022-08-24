import re

num = []
for i in range(int(input())):
    num += [int(n) for n in re.findall(r'\d+', input())]
print(*sorted(num), sep='\n')