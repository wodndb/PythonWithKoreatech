#!/usr/local/bin/python
# coding: utf-8

import sys, os
d = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5}

L = d.items()
L_keys = d.keys()
L_values = d.values()


#1. Sorting tuples incresely to alphabet in keys
L_keys.sort()
for key in L_keys:
	print key, d[key]
print

#2. Sorting tuples decreasly to alphabet in keys
L_keys.sort(reverse = True)
for key in L_keys:
	print key, d[key]
print

#3. Sorting tuples increaely to number in values
L_values.sort()
for value in L_values:
	for key in L_keys:
		if(d[key] == value):
			print key, value
print

#4. Sorting tuples decreaely to number in values
L_values.sort(reverse = True)
for value in L_values:
	for key in L_keys:
		if(d[key] == value):
			print key, value
print
