class ElectricityBill:
    def __init__(self, id, name, args):
        self.id = id
        self.setName(name)
        self.type = args[0]
        self.numberOfElectric = int(args[2])-int(args[1])
    
    def setName(self, name):
        name = name.lower().split()
        for i in range(len(name)):
            name[i] = name[i][0].upper() + name[i][1:]
        self.name = ' '.join(name)
        
    def getMoneyInNorm(self):
        if self.numberOfElectric <= norm[self.type]:
            return self.numberOfElectric*450
        return norm[self.type]*450
    
    def getMoneyOutNorm(self):
        if self.numberOfElectric <= norm[self.type]:
            return 0
        return (self.numberOfElectric-norm[self.type])*1000
    
    def getVAT(self):
        return self.getMoneyOutNorm()//20
    
    def getPrice(self):
        return self.getMoneyInNorm()+self.getMoneyOutNorm()+self.getVAT()
    
    def __str__(self):
        return '{} {} {} {} {} {}'.format(self.id, self.name, self.getMoneyInNorm(), self.getMoneyOutNorm(), self.getVAT(), self.getPrice())
        
norm = {'A':100, 'B':500, 'C':200}

if __name__ == '__main__':
    bill = [ElectricityBill('KH{0:0>2}'.format(i+1), input(), input().split()) for i in range(int(input()))]
    bill.sort(key=lambda ele: -ele.getPrice())
    print(*bill, sep='\n')