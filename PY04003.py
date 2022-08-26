from math import gcd


class phan_so:
    def __init__(self, list):
        self.__x = int(list[0])
        self.__y = int(list[1])
        
    def rut_gon(self):
        g = gcd(self.__x, self.__y)
        self.__x //= g
        self.__y //= g
        
    def __str__(self):
        return f'{self.__x}/{self.__y}'
    
ps = phan_so(input().split())
ps.rut_gon()
print(ps)