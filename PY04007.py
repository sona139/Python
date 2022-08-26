import numpy

class Matrix:
    def __init__(self, n, m, mt):
        self.n = n
        self.m = m
        self.mt = mt
        
    def __mul__(self, other):
        return Matrix(self.n, self.n, self.mt.dot(other.mt))
    
    def transpose(self):
        return Matrix(self.m, self.n, self.mt.transpose())
    
    def __str__(self):
        res = ''
        for i in range(self.n):
            for j in range(self.m):
                res += str(self.mt[i][j]) + ' '
            res += '\n'
        return res

if __name__ == '__main__':    
	for case in range(int(input())):
		n, m = [int(i) for i in input().split()]
		ip = []
		for i in range(n):
			ip += [[int(j) for j in input().split()]]
		mt = numpy.zeros((n, m), dtype=int)
		for i in range(n):
			for j in range(m):
				mt[i][j] = int(ip[i][j])
		mt = Matrix(n, m, mt)
		print(mt*mt.transpose())