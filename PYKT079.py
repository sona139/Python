for case in range(int(input())):
    n = int(input())
    l = list({int(i) for i in input().split()})
    print(max(l)-min(l)+1-len(l))