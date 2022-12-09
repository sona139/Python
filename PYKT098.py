res = []

for line in open('DATA.in', mode='r', encoding='utf-8'):
    for i in line.split():
        if not i.isdigit() or int(i) > 2147483647 or int(i) < -2147483648:
            res.append(i)
            
print(*sorted(res))