class Timer:
    def __init__(self, id, name, time_begin, tiem_end):
        self.id = id
        self.name = name
        self.time_begin = time_begin
        self.time_end = tiem_end
        self.cal()
        
    def cal(self):
        begin = self.time_begin.split(':')
        end = self.time_end.split(':')
        self.hours = int(end[0]) - int(begin[0])
        self.minutes = int(end[1]) - int(begin[1])
        if self.minutes < 0:
            self.hours -= 1
            self.minutes += 60
        self.total_time = f'{self.hours} gio {self.minutes} phut'
        
    def __str__(self):
        return f'{self.id} {self.name} {self.total_time}'
    
print(*sorted([Timer(input(), input(), input(), input()) for i in range(int(input()))], key=lambda ele: (-ele.hours, -ele.minutes)), sep='\n')