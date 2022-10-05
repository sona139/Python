n = int(input())
list = []
while True:
    try:
        list += [int(i) for i in input().split()]
    except:
        break
index = 1
while list:
    if index == list[0]:
        list.pop(0)
    else:
        print(index)
    index += 1
if index == n+1:
    print('Excellent!')