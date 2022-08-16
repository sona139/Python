while True:
    n = int(input())
    if n == 0:
        break
    cnt = 1
    while n > 1:
        cnt += 1
        if n%2:
            n = n*3+1
        else:
            n = n/2
    print(cnt)