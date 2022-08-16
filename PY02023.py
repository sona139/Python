for case in range(int(input())):
    n = int(input())
    print(*sorted([i for i in input().split()], key=lambda e: (sum(int(i) for i in e), int(e))))