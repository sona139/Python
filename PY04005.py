from math import sqrt


class Point:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
class Triangle:
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        
    def dis(self, p1, p2):
        return sqrt((p1.a-p2.a)**2+(p1.b-p2.b)**2)
    
    def cv(self):
        a = self.dis(self.p1, self.p2)
        b = self.dis(self.p1, self.p3)
        c = self.dis(self.p2, self.p3)
        if max(a, b, c)*2 >= a+b+c:
            return 'INVALID'
        return '{:.3f}'.format(a+b+c)

arg = []
t = int(input())
for _ in range(t):
    arg += [float(i) for i in input().split()]
i = 0
for index in range(t):
    print(Triangle(Point(arg[i], arg[i+1]), Point(arg[i+2], arg[i+3]), Point(arg[i+4], arg[i+5])).cv())
    i += 6