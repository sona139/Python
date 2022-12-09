if __name__ == '__main__':
    for _ in range(int(input())):
        n, m = [int(i) for i in input().split()]
        matrix = []
        for i in range(n):
            matrix.append([int(i) for i in input().split()])
        
        h = []
        for i in range(3):
            h.append([int(i) for i in input().split()])
        
        res = [[] for _ in range(n-2)]
        for i in range(n-2):
            for j in range(m-2):
                num = 0
                for k in range(3):
                    for l in range(3):
                        num += matrix[i+k][j+l]*h[k][l]
                res[i].append(num)
        print(sum([sum(line) for line in res]))