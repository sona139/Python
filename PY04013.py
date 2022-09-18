from datetime import datetime

class Meteorology:
    def __init__(self, id, name, timeBegin:datetime, timeEnd:datetime, amount_of_rain):
        self.id = id
        self.name = name
        self.amount_of_rain = amount_of_rain
        self.hours = (timeEnd-timeBegin).total_seconds()/3600
    
    def set_average_rainfall(self):
        self.average_rainfall = self.amount_of_rain/self.hours
    
    def __str__(self):
        return self.id + ' ' + self.name + ' ' + '{:.2f}'.format(self.average_rainfall)
    
map_measuring = {}

stt = 1
for i in range(int(input())):
    name = input()
    newObj = Meteorology('T{0:0>2}'.format(stt), name, datetime.strptime(input(), '%H:%M'), datetime.strptime(input(), '%H:%M'), int(input()))
    if name in map_measuring:
        map_measuring[name].hours += newObj.hours
        map_measuring[name].amount_of_rain += newObj.amount_of_rain
    else:
        map_measuring[name] = newObj
        stt += 1

for i in map_measuring:
    map_measuring[i].set_average_rainfall()
    print(map_measuring[i])