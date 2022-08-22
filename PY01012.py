s1, s2 = input(), input()
index = int(input())
print(s1[:index-1] + s2 + s1[index-1:])