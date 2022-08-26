num = input()
c688 = num.count('688')
c68 = num.count('68')-c688
c6 = num.count('6')-c68-c688
print('YES' if c6 + c68*2 + c688*3 == len(num) else 'NO')