num = input()
a = [key for key in {num[i-1:i+1] for i in range(1, len(num), 2)}]
print(*sorted(a))