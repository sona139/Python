from bisect import bisect_left
from sys import stdin

input = []
for line in stdin:
    for num in line.split():
        input.append(int(num))
        
it = iter(input)
for _ in range(next(it)):
    n = next(it)
    l = [next(it) for i in range(n)]
    h = [next(it) for i in range(n)]
    
    dcm = [-1]*n
    st = []
    for i in range(n):
        while st and h[i] >= h[st[-1]]:
            st.pop()
        if len(st): dcm[i] = st[-1]
        st.append(i)
        
    sum = [0]*n
    for i in range(1, n):
        sum[i] = sum[i-1]+h[i-1]
    
    area = [0]*n
    for i in range(n):
        if dcm[i] == -1:
            area[i] = l[i]*h[i]-sum[i]
        else:
            area[i] = area[dcm[i]]+(l[i]-l[dcm[i]]-1)*h[i] - (sum[i]-sum[dcm[i]+1])
    
    # print(area)
    # print(input[index])
    
    for __ in range(next(it)):
        k = next(it)
        print(bisect_left(area, k, 0, n))