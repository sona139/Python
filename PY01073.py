import itertools

str = input()
for i in itertools.permutations(str):
    print(''.join(i))