def s(num):
    return sum(int(num[i]) for i in range(1, len(num), 2))

def m(num):
    list = [int(num[i]) for i in range(0, len(num), 2)]
    if list.count(0) == len(list):
        return 0
    res = 1
    for i in list:
        if i != 0:
            res *= i
    return res
    

for case in range(int(input())):
    num = input()
    print(m(num), s(num))