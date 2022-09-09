from datetime import datetime

class Subject:
    def __init__(self, subject_id, subject_name):
        self.subject_id = subject_id
        self.subject_name = subject_name
        
class Exam:
    def __init__(self, exam_id, args):
        self.exam_id = exam_id
        self.subject = map_subject[args[0]]
        self.date = args[1]
        self.time = args[2]
        self.shift = args[3]
    
    def __str__(self):
        return '{} {} {} {} {} {}'.format(self.exam_id, self.subject.subject_id, self.subject.subject_name, self.date, self.time, self.shift)
    
n, m = [int(i) for i in input().split()]
subjects = [Subject(input(), input()) for _ in range(n)]
map_subject = {i.subject_id:i for i in subjects}

exams = [Exam('T{0:0>3}'.format(i+1), input().split()) for i in range(m)]
exams.sort(key=lambda ele: (ele.date.split('/')[::-1], ele.time, ele.subject.subject_id))

print(*exams, sep='\n')