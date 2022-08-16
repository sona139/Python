def deff(str):
    for i in range(2, len(str)):
        if str[i] != str[i-2]:
            return 'NO'
    return 'YES'

for case in range(int(input())):
    print(deff(input()))