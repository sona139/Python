Fib = [1]*93
for i in range(3, 93):
    Fib[i] = Fib[i-1] + Fib[i-2]

for case in range(int(input())):
    a, b = [int(i) for i in input().split()]
    for i in range(a, b+1):
        print(Fib[i], end = ' ')
    print()