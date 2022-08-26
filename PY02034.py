num = input()
nums = [num[i-1:i+1] for i in range(1, len(num), 2)]
mydict = dict()
for i in nums:
    mydict[i] = nums.count(i)
for i in nums:
    if mydict[i]:
        print(i, mydict[i])
        mydict[i] = 0