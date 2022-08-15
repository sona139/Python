str = input()
for i in range(len(str)-3, 0, -3):
    str = str[:i] + ',' + str[i:]
print(str)