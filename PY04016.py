from datetime import datetime

price = {'1': 25, '2': 34, '3':50, '4':80}

class HD:
    def __init__(self, id, name, room, day_in, day_out, any):
        self.code = 'KH{0:0>2}'.format(id)
        self.name = name
        self.room = room
        self.day_in = day_in
        self.day_out = day_out
        self.any = any
        self.day = str(datetime.strptime(day_out, '%d/%m/%Y')-datetime.strptime(day_in, '%d/%m/%Y')).split()[0]
        if self.day == '0:00:00': self.day = 1
        else: self.day = int(self.day) + 1
        self.total = price[self.room[0]]*self.day + self.any
    
    def __str__(self):
        return self.code + ' ' + self.name + ' ' + self.room + ' ' + str(self.day) + ' ' + str(self.total)
    
list = [HD(i+1, input().strip(), input().strip(), input().strip(), input().strip(), int(input().strip())) for i in range(int(input()))]
list.sort(key=lambda ele: -ele.total)
print(*list, sep='\n')