def deff(str):
    for i in range(1, len(str)):
        if str[i] < str[i-1]:
            return 'NO'
    return 'YES'

for case in range(int(input())):
    print(deff(input()))