map = {}
n, k = [int(i) for i in input().split()]
for _ in range(int(n)):
    s = input().lower()
    for i in range(len(s)):
        if not s[i].isalnum():
            s = s.replace(s[i], ' ')
    for i in s.split():
        if i in map:
            map[i] += 1
        else:
            map[i] = 1;
map = sorted(map.items(), key=lambda ele: (-ele[1], ele[0]))
for i in map:
    if i[1] >= k:
        print(*i)
    else: break