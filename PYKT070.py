from datetime import datetime

class Subject:
    def __init__(self, id_subject, name_subject, exam_form):
        self.id_subject = id_subject
        self.name_subject = name_subject
        self.exam_form = exam_form
        
class Exam:
    def __init__(self, id_exam, date, time, id_room):
        self.id_exam = id_exam
        self.date = datetime.strptime(date, '%d/%m/%Y')
        self.time = datetime.strptime(time, '%H:%M')
        self.id_room = id_room
        
class Schedule:
    def __init__(self, args):
        self.exam = map_exam[args[0]]
        self.subject = map_subject[args[1]]
        self.id_group = args[2]
        self.number_students = args[3]
        
    def __str__(self):
        return '{} {} {} {} {} {}'.format(datetime.strftime(self.exam.date, '%d/%m/%Y'), datetime.strftime(self.exam.time, '%H:%M'), self.exam.id_room, self.subject.name_subject, self.id_group, self.number_students)
        
map_exam, map_subject = {}, {}

with open('MONTHI.in', mode = 'r', encoding='utf-8') as f:
    n = int(f.readline().rstrip('\n'))
    for i in range(n):
        subject_id = f.readline().rstrip('\n')
        subject_name = f.readline().rstrip('\n')
        exam_form = f.readline().rstrip('\n')
        map_subject[subject_id] = Subject(subject_id, subject_name, exam_form)
    
with open('CATHI.in', mode = 'r', encoding = 'utf-8') as f:
    n = int(f.readline().rstrip('\n'))
    for i in range(n):
        date = f.readline().rstrip('\n')
        time = f.readline().rstrip('\n')
        id_room = f.readline().rstrip('\n')
        id_exam = 'C{0:0>3}'.format(i+1)
        map_exam[id_exam] = Exam(id_exam, date, time, id_room) 
        
with open('LICHTHI.in', mode = 'r', encoding = 'utf-8') as f:
    list = [Schedule(f.readline().rstrip('\n').split(' ')) for _ in range(int(f.readline().rstrip('\n')))]

list.sort(key=lambda ele: (ele.exam.date, ele.exam.time, ele.exam.id_exam))
print(*list, sep = '\n')