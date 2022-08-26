n = int(input())
while n != 0:
    list = [int(input()) for i in range(n)]
    print('BANG NHAU' if list.count(list[0]) == n else f'{min(list)} {max(list)}')
    n = int(input())