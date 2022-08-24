import re

for case in range(int(input())):
    s = input()
    print(''.join(sorted(re.findall(r'\D', s))) + str(sum(int(i) for i in re.findall(r'\d', s))))