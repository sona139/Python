num = input()
my_list = [num[i-1] + num[i] for i in range(1, len(num), 2)]
res = list(set(my_list))
print(*sorted(res, key=lambda ele: my_list.index(ele)))