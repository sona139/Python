myset = set()
while True:
	try:
		myset.update([int(i)%42 for i in input().split()])
	except EOFError:
		print(len(myset))
		break