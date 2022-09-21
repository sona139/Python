s = input()
res = 1 if len(s) == 1 else 0
while(len(s) > 1):
    s = str(sum(ord(i)-ord('0') for i in s))
    res += 1
print(res)