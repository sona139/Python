class Line:
    def __init__(self, args):
        self.x = int(args[0])
        self.y = int(args[1])
        
if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        list = []
        for i in range(n):
            list.append(Line(input().split()))
        list.sort(key=lambda ele: (ele.x, ele.y))
        res, start = 0, 0
        for line in list:
            if line.x >= start:
                res += 1
                start = line.y
            elif line.y < start:
                start = line.y
        print(res)