import re

s = 'as 127 12e72 e.?h172b   .  ,ds asd,w 2e 17 21 2 8eh1yu2eh178'
print(s)
print(re.findall('\w+', s))