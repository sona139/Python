n = int(input())
list = [float(i) for i in input().split()]
MIN, MAX = min(list), max(list)
newlist = []
for i in list:
    if i != MIN and i != MAX:
        newlist += [i]
print('{:.2f}'.format(sum(newlist)/len(newlist)))