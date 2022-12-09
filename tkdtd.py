for _ in range(int(input())):
    n = int(input())
    l = [int(i) for i in input().split()]
    h = [int(i) for i in input().split()]
    m = [0]*n
    s = [0]*n
    m[0] = 0
    for i in range(1, n):
        m[i] = max(h[i-1], m[i-1])
        s[i] = s[i-1]+h[i-1]
    area = [0]*n
    for i in range(n):
        if h[i] < m[i]:
            area[i] = area[i-1]+(l[i]-l[i-1]-1)*h[i]
        else:
            area[i] = l[i]*h[i] - s[i]
    for q in range(int(input())):
        k = int(input())
        if k < area[0]:
            print(0)
            continue
        for i in range(n-1, -1, -1):
            if k > area[i]:
                print(i+1)
                break