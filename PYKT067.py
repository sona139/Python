from ctypes import sizeof
import itertools

for case in range(int(input())):
    n = int(input())
    sz = 0
    for i in itertools.permutations(range(n, 0, -1)):
        sz += 1
    print(sz)
    for i in itertools.permutations(range(n, 0, -1)):
        print(''.join([str(j) for j in i]), end=' ')
    print()