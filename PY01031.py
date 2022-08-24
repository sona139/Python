BASE = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for case in range(int(input())):
    num, base = [int(i) for i in input().split()]
    res = ''
    while num > 1:
        res += BASE[int(num%base)]
        num /= base
    print(res[::-1])