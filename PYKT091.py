list = []
map = dict()

with open('VANBAN.in', mode='r', encoding='utf-8') as f:
    list = f.readlines()

res = []
    
for line in list:
    words = line.rstrip('\n').split()
    for word in words:
        if word == word[::-1]:
            if res == [] or len(word) == len(res[0]):
                if map.get(word) == None:
                    res.append(word)
                    map[word] = 1
                else:
                    map[word] += 1
            elif len(word) > len(res[0]):
                res = [word]
                map[word] = 1
                
for w in res:
    print(w, map[w])