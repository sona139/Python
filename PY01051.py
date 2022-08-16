for case in range(int(input())):
    s = str(sum(map(int, ' '.join(input()).split())))
    print('YES' if len(s) > 1 and s == s[::-1] else 'NO')