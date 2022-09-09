class Subject:
    def __init__(self, id, name, exam_forms):
        self.id = id
        self.name = name
        self.exam_forms = exam_forms
        
    def __str__(self):
        return '{} {} {}'.format(self.id, self.name, self.exam_forms)
    
subjects = [Subject(input(), input(), input()) for _ in range(int(input()))]
subjects.sort(key=lambda ele: ele.id)

print(*subjects, sep='\n')