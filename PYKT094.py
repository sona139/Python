class Department:
    def __init__(self, args):
        self.department_id = args[0]
        self.department_name = ' '.join(args[1:])
        map_department[self.department_id] = self.department_name
        

class Employee:
    def __init__(self, employee_id, employee_name, daily_salary, number_of_workdays):
        self.employee_id = employee_id
        self.employee_name = employee_name
        self.daily_salary = int(daily_salary)
        self.number_of_workdays = int(number_of_workdays)
        self.salary = self.setSalary()*1000
        self.employee_department = map_department[employee_id[3:5]]
        
    def setSalary(self):
        years = int(self.employee_id[1:3])
        if years > 16: years = 16
        return self.daily_salary*self.number_of_workdays*bonus[ord(self.employee_id[0])-ord('A')][years]
    
    def __str__(self):
        return '{} {} {} {}'.format(self.employee_id, self.employee_name, self.employee_department, self.salary)
        
map_department = {}
bonus = [
	[1, 10, 10, 10, 12, 12, 12, 12, 12, 14, 14, 14, 14, 14, 14, 14, 20],
	[1, 10, 10, 10, 11, 11, 11, 11, 11, 13, 13, 13, 13, 13, 13, 13, 16],
	[1, 9, 9, 9, 10, 10, 10, 10, 10, 12, 12, 12, 12, 12, 12, 12, 14],
	[1, 8, 8, 8, 9, 9, 9, 9, 9, 11, 11, 11, 11, 11, 11, 11, 13]
]

departments = [Department(input().split()) for _ in range(int(input()))]
employees = [Employee(input(), input(), input(), input()) for _ in range(int(input()))]

print(*employees, sep='\n')