class Student:
    def __init__(self, name, birth, scores):
        self.__name = name
        self.__birth = birth
        self.scores = sum(scores)
        
    def __str__(self):
        return f'{self.__name} {self.__birth} {self.scores}'
    
if __name__ == '__main__':
    print(Student(input(), input(), [float(input()), float(input()), float(input())]))