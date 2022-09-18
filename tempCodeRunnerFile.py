map = {}
for _ in range(int(input())):
    s = input().lower().strip()
    for i in range(len(s)):
        if s[i] >= '0' and s[i] <= '9' or s[i] >= 'a' and s[i] <= 'z': continue
        s[i] = ' '
    for i in s.split():
        if i in map:
            map[i] += 1
        else:
            map[i] = 1;
map = sorted(map.items(), key=lambda ele: (-ele[1], ele[0]))
for i in map:
    print(*i)