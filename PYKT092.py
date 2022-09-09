class Student:
    def __init__(self, id, name, score, ethnic, range):
        self.id = self.setId(id)
        self.name = self.setName(name)
        self.ethnic = ethnic
        self.range = range
        self.score = self.setScore(score)
        self.status = self.setStatus()
        
    def setId(self, id):
        return 'TS{0:0>2}'.format(id)
        
    def setName(self, name):
        name = name.lower().split()
        for i in range(len(name)):
            name[i] = name[i][0].upper() + name[i][1:]
        return ' '.join(name)
    
    def setScore(self, score):
        if self.ethnic != 'Kinh':
            score += 1.5
        if self.range == '1':
            score += 1.5
        elif self.range == '2':
            score += 1
        return float('{:.1f}'.format(score))
        
    def setStatus(self):
        return 'Do' if self.score >= 20.5 else 'Truot'
    	
    def __str__(self):
        return '{} {} {} {}'.format(self.id, self.name, self.score, self.status)

students = [Student(i+1, input(), float(input()), input(), input()) for i in range(int(input()))]
students.sort(key=lambda ele: (-ele.score, ele.id))
print(*students, sep='\n')