n = int(input())
mt = []
for i in range(n):
    mt += [[int(j) for j in input().split()]]
if n == 2:
    print(mt[0][1]//2, mt[0][1]//2)
    exit(0)
a = [0]*n
# a[0] + a[1] = b[0][1]
# a[1] + a[2] = b[1][2]
# a[0] - a[2] = b[0][1] - b[1][2]
# a[0] + a[2] = b[0][2]
# a[0] = (b[0][1]-b[1][2]+b[0][2])/2
a[0] = (mt[0][1]-mt[1][2]+mt[0][2])//2
for i in range(1, n):
    a[i] = mt[i][0] - a[0]
print(*a)