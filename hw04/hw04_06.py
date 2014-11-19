#/usr/local/bin/python
# coding: utf-8

def myfact(num):
	if(num == 1):
		return 1;
	else:
		return num * myfact(num - 1)

print "myfact(5)"
print myfact(5)
