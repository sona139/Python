mh = {'A': 'TOAN', 'B':'LY', 'C':'HOA'}
ut = {'1':2.0, '2':1.5, '3':1.0, '4':0.0}

class TT:
    def __init__(self, id, name, ma, d1, d2):
        self.id = id
        self.name = name
        self.ma = ma
        self.d1 = d1
        self.d2 = d2
        self.score = d1*2+d2 + ut[ma[1]]
        self.mh = mh[ma[0]]
        if self.score >= 18: self.note = 'TRUNG TUYEN'
        else: self.note = 'LOAI'
        
    def __str__(self):
        return self.id + ' ' + self.name + ' ' + self.mh + ' ' + str(self.score) + ' ' + self.note
        
list = [TT('GV{0:0>2}'.format(i+1), input(), input(), float(input()), float(input())) for i in range(int(input()))]
list.sort(key=lambda ele: -ele.score)
print(*list, sep='\n')