import re

while True:
    try:
        line = re.findall('[^\d\s]+', input().strip().lower())
        for i in range(len(line)):
            if len(line[i]) > 1 and line[i][-1] in '.?!:,':
                line = line[:i+1] + [line[i][-1]] + line[i+1:]
                line[i] = line[i][:-1]
        line[0] = line[0].title()
        s = line[0]
        for i in range(1, len(line)):
            if line[i] in '.?!':
                s += line[i]
                if i != len(line)-1:
                    line[i+1].title()
            elif re.match('\w+', line[i]):
                s += ' ' + line[i]
            else: s += line[i]
        if s[-1] not in '.?!':
            s += '.'
        print(s) 
    except:
        break