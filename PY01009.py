str = input()
up, lw = 0, 0
for i in str:
    if i.isupper():
        up += 1
    else:
        lw += 1
if lw >= up:
    str = str.lower()
else:
    str = str.upper()
print(str)