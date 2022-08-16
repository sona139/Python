t = int(input())
a = list(map(int, input().split()))
def binSearch(a, l, r, t):
    if l <= r:
        mid = (l + r) // 2
        if a[mid] == t:
            print(t)
            return 1
        else:
            print(a[mid], end=' ')
        if a[mid] == t: return 1
        elif a[mid] > t: return binSearch(a, 0, mid - 1, t)
        else: return binSearch(a, mid + 1, r, t)
    else: return -1

binSearch(a, 0, len(a) - 1, t)
