class Team:
    def __init__(self, team_id, team_name, school):
        self.team_id = team_id
        self.team_name = team_name
        self.school = school

class Student:
    def __init__(self, student_id, student_name, team):
        self.student_id = student_id
        self.student_name = student_name
        self.team = team
        
    def __str__(self):
        return '{} {} {} {}'.format(self.student_id, self.student_name, self.team.team_name, self.team.school)

map_team = dict()
list_team = []
for i in range(int(input())):
    list_team += [Team('Team{0:0>2}'.format(i+1), input(), input())]
    map_team[list_team[i].team_id] = list_team[i]

m = int(input())
list_student = []
for i in range(m):
    student_id = 'C{0:0>3}'.format(i+1)
    student_name = input()
    student_team = map_team[input()]
    list_student += [Student(student_id, student_name, student_team)]

list_student.sort(key=lambda ele: ele.student_name)

print(*list_student, sep='\n')
    