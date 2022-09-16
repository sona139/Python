s1, s2 = set(), set()
with open(r'DATA1.in', encoding='utf-8') as f:
    s1 = set(' '.join(f.readlines()).replace('\n', ' ').split())
with open(r'DATA1.in', encoding='utf-8') as f:
    s2 = set(' '.join(f.readlines()).replace('\n', ' ').split())
print(*sorted(list(s1-s2)))
print(*sorted(list(s2-s1)))