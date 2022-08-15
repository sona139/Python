for case in range(int(input())):
    str = input()
    if len(str) <= 1:
        print('NO')
        continue
    str = str[-2:len(str)]
    if str == '86':
        print('YES')
    else:
        print('NO')