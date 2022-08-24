n, m = [int(i) for i in input().split()]
a = sorted(list({int(i) for i in input().split()}))
b = sorted(list({int(i) for i in input().split()}))
congacon, congabo, congame = [], [], []
for i in a:
    if i in b: congacon += [i]
    else: congabo += [i]
for i in b:
    if i not in a: congame += [i]
print(*congacon)
print(*congabo)
print(*congame)
