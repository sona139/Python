
pow = {0:1, 1:2, 2:4, 3:8, 4:16}
log = {16:4, 8:3, 4:2, 2:1, 1:0}
r = '0123456789ABCDEF'

ip = []

with open('DATA.in', mode='r', encoding='utf-8') as f:
    ip = f.readlines()
    for i in range(len(ip)):
        ip[i] = ip[i][:-1]
        
index = 1
for _ in range(int(ip[0])):
    base, n = int(ip[index]), ip[index+1]
    base = log[base]
    n = '0'*((base-len(n)%(base))%base) + n
    for i in range(0, len(n), base):
        res = 0
        for j in range(base):
            res += int(n[i+j])*pow[base-j-1]
        print(r[res], end='')
    print()
    index += 2