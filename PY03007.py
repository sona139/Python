from sys import stdin, stdout

down = '.!?'
flat = ',:'

list = []

newlist = stdin.readlines()
for line in newlist:
    line.replace(' ', '\n')
    for word in line.lower().split():
        character = word[len(word)-1]
        if len(word) > 1 and (character in down or character in flat):
            list += [word[:len(word)-1]]
            list += [character]
        else:
            list += [word]
            
list[0] = list[0].title()
print(list[0], end = '')
for i in range(1, len(list)-1):
    if list[i] in down:
        print()
        list[i+1] = list[i+1].title()
    else:
        if list[i-1] not in down and list[i] not in flat:
            print(' ', end = '')
        print(list[i], end = '')