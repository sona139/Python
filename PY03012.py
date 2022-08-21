class student:
    def __init__(self, name, *congacon):
        self.__name = name
        self.__total = int(congacon[0])
        self.__submit = int(congacon[1])
    
    def set_name(self, name):
        self.__name = name
    
    def get_name(self):
        return self.__name
    
    def set_total(self, total):
        self.__name = total
    
    def get_total(self):
        return self.__total
    
    def set_submit(self, submit):
        self.__name = submit
    
    def get_submit(self):
        return self.__submit
    
    def __str__(self):
        return f'{self.__name} {self.__total} {self.__submit}\n'    

students = []    
for i in range(int(input())):
    students += [student(input(), *input().split())]
    
students.sort(key=lambda ele: (-ele.get_total(), ele.get_submit(), ele.get_name()))

print(*students)