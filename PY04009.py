class complex_number:
    def __init__(self, real = None, imaginary = None):
        self.real = int(real)
        self.imaginary = int(imaginary)
        
    def __add__(self, other):
        return complex_number(self.real+other.real, self.imaginary+other.imaginary)
    
    def __mul__(self, other):
        return complex_number(self.real*other.real-self.imaginary*other.imaginary, self.real*other.imaginary+self.imaginary*other.real)
    
    def __str__(self):
        return f'{self.real} + {self.imaginary}i'
    
for case in range(int(input())):
    ip = input().split()
    a = complex_number(ip[0], ip[1])
    b = complex_number(ip[2], ip[3])
    sum = a+b
    c = sum*a
    d = sum*sum
    print(c, d, sep=', ')
    