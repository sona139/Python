def deff(str):
    if len(str) < 3:
        return 'NO'
    i = 1
    while i < len(str) and str[i] > str[i-1]:
        i += 1
    while i < len(str) and str[i] < str[i-1]:
        i += 1
    return 'YES' if i == len(str) else 'NO'

for case in range(int(input())):
    print(deff(input()))