def get_max(list, count):
    return max(list, key=lambda ele: count[ele])

def erase_mx(count, m, mx):
    return [count[i] if count[i] < count[mx] else 0 for i in range(0, m+1)]

n, m = [int(i) for i in input().split()]
list = [int(i) for i in input().split()]
count = [list.count(i) for i in range(m+1)]
count = erase_mx(count, m, get_max(list, count))
mx = get_max(list, count)	
print(mx if count[mx] else 'NONE')