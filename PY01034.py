for _ in range(int(input())):
    num = list(input())
    i = len(num)-2
    while i >= 0 and num[i] <= num[i+1]:
        i -= 1
    if i == -1:
        print(-1)
        continue
    j = len(num)-1
    while num[j] >= num[i] or num[j] == num[j-1]:
        j -= 1
    num[i], num[j] = num[j], num[i]
    if num[0] == '0':
        print(-1)
        continue
    print(''.join(num))