def chicken(list):
    if len(list) != 4: return 'NO'
    for i in list:
        if i > 255:
            return 'NO'
    return 'YES'

for __ in range(int(input())):
    print(chicken([int(i) for i in input().split()]))