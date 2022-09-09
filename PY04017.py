class DxD:
    def __init__(self, name, dv, time):
        self.id = ''
        for i in f'{dv} {name}'.split():
            self.id += i[0]
        self.name = name
        self.dv = dv
        self.speed = 120/(int(time[0])-6+(int(time[2:4])/60))
        
    def __str__(self):
        return self.id + ' ' + self.name + ' ' + self.dv + ' ' + str(round(self.speed)) + ' Km/h'

list = [DxD(input(), input(), input()) for _ in range(int(input()))]
list.sort(key=lambda ele: -ele.speed)
print(*list, sep='\n')