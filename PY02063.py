n = int(input())
list = [int(i) for i in input().split()]
list.sort()
print(max(list[0]*list[1]*list[-1], list[0]*list[1], list[-1]*list[-2], list[-1]*list[-2]*list[-3]))