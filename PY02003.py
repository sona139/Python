list = []
MAX = 10**18

i = 1
while i <= MAX:
    j = 1
    while j <= MAX:
        z = 1
        while z <= MAX:
            list += [i*j*z]
            z *= 5
        j *= 3
    i *= 2

list.sort()

def bin(l, r, x):
    mid = (l+r)//2
    if list[mid] == x:
        return mid+1
    if l >= r:
        return 'Not in sequence'
    if list[mid] < x:
        return bin(mid+1, r, x)
    return bin(l, mid-1, x)

for case in range(int(input())):
    print(bin(0, len(list), int(input())))