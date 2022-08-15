def deff(num):
    sum = int(num[0])
    for i in range(1, len(num)):
        if num[i] == num[i-1]:
            return 'NO'
        sum += int(num[i])
    if sum%10:
        return 'NO'
    return 'YES'

for case in range(int(input())):
    num = input()
    print(deff(num))