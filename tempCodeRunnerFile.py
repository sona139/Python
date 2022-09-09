
n = int(input())
students = [Student(i+1, input(), input(), input(), input()) for i in range(n)]
students.sort(key=lambda ele: (-float(ele.score), ele.id))