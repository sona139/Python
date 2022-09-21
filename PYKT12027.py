n = int(input())
l = [int(i) for i in input().split()]
res = 0

def merge(l, mid, r, list):
	i, j, k = l, mid+1, l
	cnt = 0
	tmp = []
	while i <= mid and j <= r:
		if list[i] <= list[j]:
			tmp += [list[i]]
			i += 1
		else:
			tmp += [list[j]]
			cnt += (mid-i+1)
			j += 1
		k += 1
	while i <= mid:
		tmp += [list[i]]
		k += 1
		i += 1
	while j <= r:
		tmp += [list[j]]
		k += 1
		j += 1
	for i in range(l, r+1):
		list[i] = tmp[i-l]
	return cnt

def merge_sort(l, r, list):
    res = 0
    if r > l:
        mid = (l+r)//2
        res += merge_sort(l, mid, list) + merge_sort(mid+1, r, list)
        res += merge(l, mid, r, list)
    return res
print(merge_sort(0, n-1, l))