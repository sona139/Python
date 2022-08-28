num = input()
while len(num) > 1:
    num = str(int(num[:len(num)//2]) + int(num[len(num)//2:]))
    print(num)