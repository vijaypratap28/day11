import re
str1 = 'ip address is 122.184.10.1'


match = re.findall(r'\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}',str1)
if match:
	print "it is an ip address"
else:
	print "it is not an ip address"
