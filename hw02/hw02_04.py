#!/usr/local/bin/python
# coding: utf-8
import sys, os

def list_union(lista, listb):
	result = []
	result += lista
	for k in range(len(lista)):
		if(lista[k] in result):
			continue
		else:
			result.append(lista[k])
	k = 0
	for k in range(len(listb)):
		if(listb[k] in result):
			continue
		else:
			result.append(listb[k])
	result.sort()

	return result

print list_union([1, 2, 3], [1, 2, 4])
print list_union([-10, -5, 0, -1], [100, 9, 0, 9])
print list_union([0, 1, 2], [0, 1, 2])
