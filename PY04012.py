class Student:
    def __init__(self, code, name, group):
        self.code = code
        self.name = name
        self.group = group
        self.note = ''
    
    def set_cc(self, cc):
        self.score = max(0, 10-cc.count('m')-cc.count('v')*2)
        if self.score == 0: self.note = 'KDDK'
        
    def __str__(self):
        return self.code + ' ' + self.name + ' ' + self.group + ' ' + str(self.score) + ' ' + self.note
n = int(input())    
list = [Student(input(), input(), input()) for _ in range(n)]
for _ in range(n):
    id, cc = input().split()
    for i in range(len(list)):
        if list[i].code == id:
            list[i].set_cc(cc)
            break
print(*list, sep='\n')