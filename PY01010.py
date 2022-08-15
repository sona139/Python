for case in range(int(input())):
    str = input()
    if str[:2] == str[-2:len(str):]:
        print('YES')
    else:
        print('NO')