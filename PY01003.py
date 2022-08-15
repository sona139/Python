for case in range(int(input())):
    num = ' '.join(input()).split()
    for i in range(len(num)-1, 0, -1):
        if num[i] >= '5':
            num[i-1] = chr(ord(num[i-1])+1)
        num[i] = '0'
    if num[0] > '9':
        num[0] = '10'
    print(''.join(num))