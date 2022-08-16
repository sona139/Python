def reversible(str):
    if len(str)%2 or str != str[::-1]:
        return False
    for i in str:
        if int(i)%2:
            return False
    return True

for case in range(int(input())):
    num = int(input())
    for i in range(22, num, 2):
        if reversible(str(i)):
            print(i, end = ' ')
    print()