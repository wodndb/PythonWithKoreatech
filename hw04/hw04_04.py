#/usr/local/bin/python
# coding: utf-8
import sys, os

def sum(*arg):
	result = 0;
	for num in arg:
		result += num

	return result

print " # sum() "
print sum()
print

print " # sum(1, 2) "
print sum(1, 2)
print

print " # sum(1, 2, 3, 4, 5) "
print sum(1, 2, 3, 4, 5)
print

print " # sum(1, 5, 7, 2, -10) "
print sum(1, 5, 7, 2, -10)
