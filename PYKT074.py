for _ in range(int(input())):
    s = input()
    i = min(100, len(s))
    if len(s) > 100:
        if s[100] != ' ':
            while i >= 1 and s[i-1] != ' ':
                i -= 1
    print(s[:i])