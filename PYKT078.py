for __ in range(int(input())):
    n, m = [int(i) for i in input().split()]
    l = [int(i) for i in input().split()]
    index = l.index(max(l))
    l = l[:index] + [m] + l[index:]
    for i in l:
        if i < 0:
            print(i, end=' ')
    for i in l:
        if i >= 0:
            print(i, end=' ')
    print()