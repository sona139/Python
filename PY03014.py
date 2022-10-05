for _ in range(int(input())):
    s = input()
    index = 1
    st, res = [], []
    for i in s:
        if i == '(':
            res += [index]
            st += [index]
            index += 1
        elif i == ')':
            res += [st.pop()]
    print(*res)
            