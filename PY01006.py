for t in range(int(input())): 
	n = ' '.join(input()).split()
	count = n.count('4') + n.count('7')
	print("YES" if count == len(n) else "NO")