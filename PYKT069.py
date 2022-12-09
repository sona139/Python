from datetime import datetime


class CaThi:
    def __init__(self, id, date, hour, room):
        self.id = id
        self.date = datetime.strptime(date, '%d/%m/%Y')
        self.hour = datetime.strptime(hour, '%H:%M')
        self.room = room
        
    def __str__(self):
        return '{} {} {} {}'.format(self.id, datetime.strftime(self.date, '%d/%m/%Y'), datetime.strftime(self.hour, '%H:%M'), self.room)
    
with open('CATHI.in', 'r') as f:
    list = []
    for i in range(int(f.readline())):
        list.append(CaThi('C{0:0>3}'.format(i+1), f.readline()[:-1], f.readline()[:-1], f.readline()))
        
    list.sort(key=lambda ele: (ele.date, ele.hour, ele.id))
    print(*list, sep='\n')