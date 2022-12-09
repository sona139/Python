class Phone:
    def __init__(self, date, name, phone):
        self.date = date[5:]
        self.name = name
        self.phone = phone
        tmp = name.split()
        self.last_name = tmp[-1]
        
    def __str__(self):
        return '{}: {} {}'.format(self.name, self.phone, self.date)
        

list = []
with open('SOTAY.txt', mode='r', encoding='utf-8') as f:
    list = f.readlines()
    for i in range(len(list)):
        list[i] = list[i][:-1]

phones = []
date = ''
i = 0        
while i < len(list)-1:
    if list[i][:5] == 'Ngay ':
        date = list[i]
        i += 1
        continue
    phones.append(Phone(date, list[i], list[i+1]))
    i += 2

phones.sort(key=lambda ele: (ele.last_name, ele.name))
    
with open('DIENTHOAI.txt', mode='w', encoding='utf-8') as f:
    for phone in phones:
        f.write(str(phone) + '\n')