num = input()
k = int(input())
my_list = [num[i-1]+num[i] for i in range(1, len(num), 2)]
map = {i:my_list.count(i) for i in my_list}
res = sorted(list(set(filter(lambda x: map[x] >= k, my_list))))
if res == []:
    print('NOT FOUND')
else:
    for i in res:
        print(i, map[i])