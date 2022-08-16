for case in range(int(input())):
    num = ' '.join(input()).split()
    print('YES' if num.count('0')+num.count('1')+num.count('2') == len(num) else 'NO')