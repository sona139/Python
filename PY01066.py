def deff(str1, str2):
    for i in range(1, len(str1)):
        num1 = ord(str1[i]) - ord(str1[i-1])
        num2 = ord(str2[i]) - ord(str2[i-1])
        if num1 != num2 and num1 != -num2:
            return 'NO'
    return 'YES'

for case in range(int(input())):
    str = input()
    print(deff(str, str[::-1]))