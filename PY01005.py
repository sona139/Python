n = ' '.join(input()).split()
count = n.count('4') + n.count('7')
print("YES" if count == 4 or count == 7 else "NO")