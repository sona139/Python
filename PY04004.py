from math import gcd

class phan_so:
    def __init__(self, x=None, y=None):
        self.__x = x
        self.__y = y
        
    def rut_gon(self):
        g = gcd(self.__x, self.__y)
        self.__x //= g
        self.__y //= g
    
    def __add__(self, other):
        res = phan_so()
        res.__y = self.__y*other.__y
        res.__x = self.__x*other.__y + self.__y*other.__x
        res.rut_gon()
        return res
    
    def __str__(self):
        return f'{self.__x}/{self.__y}'
    
ip = [int(i) for i in input().split()]
ps1 = phan_so(ip[0], ip[1])
ps2 = phan_so(ip[2], ip[3])
res = ps1 + ps2
print(res)