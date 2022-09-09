s1 = set(input().lower().split())
s2 = set(input().lower().split())
print(*sorted(list(s1|s2)))
print(*sorted(list(s1&s2)))