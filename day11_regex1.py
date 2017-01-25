import re

str1 = '14b, wellington accord, 4th floor'

print re.findall('\d', str1)
print re.findall('\d+', str1)
print re.findall('\d+\w+', str1)
