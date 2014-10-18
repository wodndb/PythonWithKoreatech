#!usr/local/bin/python
# coding: utf-8

def addallodd(L):
	"Return SUM of odd element in List that is parameter of this function by list comprehension"
	return sum([L[k] for k in range(len(L)) if type(L[k]) == int and L[k] % 2 == 1])

print ">>> addallodd([1])"
print addallodd([1])
print
print ">>> addallodd([1, 2, 3, 4, 5, 6, 7, 8, 9])"
print addallodd([1, 2, 3, 4, 5, 6, 7, 8, 9])
print
