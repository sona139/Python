from datetime import datetime

class Car:
    def __init__(self, license_plate, type_car, number_of_chair, io, date):
        self.license_plate = license_plate
        self.type_car = type_car
        self.number_of_chair = number_of_chair
        self.io = io
        self.date = date
 
map = {}
fee = {'Xe_con 5':10000, 'Xe_con 7':15000, 'Xe_tai 2':20000, 'Xe_khach 29':50000, 'Xe_khach 45':70000}
       
for _ in range(int(input())):
    ip = input().split()
    car = Car(ip[0], ip[1], ip[2], ip[3], datetime.strptime(ip[4], '%d/%m/%Y'))
    if car.io == 'OUT': continue
    if car.date in map:
        map[car.date] += fee[car.type_car + ' ' + car.number_of_chair]
    else: map[car.date] = fee[car.type_car + ' 	' + car.number_of_chair]

for key in map:
    print('{}: {}'.format(datetime.strftime(key, '%d/%m/%Y'), map[key]))