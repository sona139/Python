for case in range(int(input())):
    n, m = input().split()
    str1, str2 = input(), input()
    num1 = int(str1.replace(n, m)) + int(str2.replace(n, m))
    num2 = int(str1.replace(m, n)) + int(str2.replace(m, n))
    print(min(num1, num2), max(num1, num2))