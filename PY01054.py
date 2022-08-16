from audioop import mul


for case in range(int(input())):
    sb = 1
    for i in input():
        if i != '0':
            sb *= int(i)
    print(sb)