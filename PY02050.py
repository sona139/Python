for _ in range(int(input())):
    n = int(input())
    list = [int(i) for i in input().split()]
    res = [1]*n
    st = [-1]
    for i in range(0, n):
        while len(st) > 1 and list[st[len(st)-1]] <= list[i]:
            st.pop()
        res[i] = i - st[len(st)-1]
        st += [i]
    print(*res)