class Rectangle:
    def __init__(self, length, width, color):
        self.__length = length
        self.__width = width
        self.__color = color
        
    def perimeter(self):
        return (self.__length+self.__width)*2
    
    def area(self):
        return self.__length*self.__width
    
    def color(self):
        return self.__color.title()

try:    
	if __name__ == '__main__':
		arr = input().split()
		r = Rectangle(int(arr[0]), int(arr[1]), int(arr[2]))

except:
    if int(arr[0]) <= 0 or int(arr[1]) <= 0:
        print('INVALID')
    else:
        r = Rectangle(int(arr[0]), int(arr[1]), arr[2])
        print('{} {} {}'.format(r.perimeter(), r.area(), r.color()))
