for case in range(int(input())):
    Str = input() + '/'
    cnt, character = 0, Str[0]
    res = ''
    for i in Str:
        if i == character:
            cnt += 1
        else:
            res += str(cnt) + character
            cnt = 1
            character = i
    print(res)
    