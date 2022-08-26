import itertools

n, k = [int(i) for i in input().split()]
l = sorted(list(set(input().split())))
for i in itertools.combinations(l ,k):
    print(' '.join(i))