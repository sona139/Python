from inspect import stack


n = int(input())
a = [int(input()) for _ in range(n)]

st = []
st.append(0)
res = 0
for i in range(n):
    while len(st)>1 and a[i] >= a[st[-1]] and a[st[i-2]] >= a[st[i-1]]:
        st.pop()
    res += i-st[-1]
    st.append(i)

print(res)