#!usr/local/bin/python
# coding: utf-8

def addallodd(L):
	"Return SUM of odd element in List that is parameter of this function by for~in literal"
	result = 0
	for k in range(len(L)):
		if(type(L[k]) == int and L[k] % 2 == 1):
			result += L[k]

	return result

print ">>> addallodd([1])"
print addallodd([1])
print
print ">>> addallodd([1, 2, 3, 4, 5, 6, 7, 8, 9])"
print addallodd([1, 2, 3, 4, 5, 6, 7, 8, 9])
print
