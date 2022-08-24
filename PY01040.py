def rot(str:str):
    sum = 0
    for i in str:
        sum += ord(i) - 65
    rotstr = ''
    for i in str:
        rotstr += chr((ord(i)-65+sum)%26 + 65)
    return rotstr

def merge(s1:str, s2:str):
    res = ''
    for i in range (len(s1)):
        res += chr((ord(s1[i])-65+ord(s2[i])-65)%26 + 65)
    return res
        
for case in range(int(input())):
    str = input()
    s1 = rot(str[:len(str)//2])
    s2 = rot(str[len(str)//2:])
    print(merge(s1, s2))