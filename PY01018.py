P = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_.'

while True:
    str = input()
    if str.strip() == '0':
        break
    k, str = str.split()
    k = int(k)
    res = ''
    for i in str:
        res += P[(P.index(i)+k)%28]
    print(res[::-1])