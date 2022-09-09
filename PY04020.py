class HD:
    def __init__(self, id, name, nums, price, ck):
        self.id = id
        self.name = name
        self.nums = nums
        self.price = price
        self.ck = ck
        self.total = self.nums*self.price-self.ck
        
    def __str__(self):
        return '{} {} {} {} {} {}'.format(self.id, self.name, self.nums, self.price, self.ck, self.total)

list = [HD(input(), input(), int(input()), int(input()), int(input())) for _ in range(int(input()))]
list.sort(key=lambda ele: -ele.total)
print(*list, sep='\n')