#!usr/local/bin/python
# coding: utf-8

def addall(L):
	"Return SUM of element in List that is parameter of this function by list comprehension"
	return sum([L[k] for k in range(len(L)) if type(L[k]) == int])

print ">>> addall([1])"
print addall([1])
print
print ">>> addall([1, 2, 3, 4, 5, 6, 7, 8, 9])"
print addall([1, 2, 3, 4, 5, 6, 7, 8, 9])
print
