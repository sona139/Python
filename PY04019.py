class Staff:
    def __init__(self, id, name, score1, score2):
        self.id = id
        self.name = name
        while score1 > 10:
            score1 /= 10
        while score2 > 10:
            score2 /= 10
        self.score1 = score1
        self.score2 = score2
        self.score = (self.score1+self.score2)/2
        self.setStatus()
        
    def setStatus(self):
        if self.score < 5:
            self.status = 'TRUOT'
        elif self.score < 8:
            self.status = 'CAN NHAC'
        elif self.score <= 9.5:
            self.status = 'DAT'
        else: self.status = 'XUAT SAC'
        
    def __str__(self):
        return '{} {} {} {}'.format(self.id, self.name, '{:.2f}'.format(self.score+0.001), self.status)
    
staffs = [Staff('TS{0:0>2}'.format(i+1), input(), float(input()), float(input())) for i in range(int(input()))]
staffs.sort(key=lambda ele: -ele.score)
print(*staffs, sep='\n')