from re import S


for case in range(int(input())):
    num = input()
    i = 1
    while i <= 1000 and int(num)%7:
        num = str(int(num) + int(num[::-1]))
        i += 1
    print(-1 if int(num)%7 else num)