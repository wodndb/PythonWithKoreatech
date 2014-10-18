#!/usr/local/bin/python
#coding:utf-8

s = '  first star   :   second star   :   third star  '
L = s.split(':')

print "< 1. for ~ in 리터럴을 사용한 문제 해결>" 

for k in range(len(L)):
	L[k] = L[k].strip()

print L

print
print "< 2. 리스트 내포를 사용한 문제 해결>"

s = '  first star   :   second star   :   third star  '
L = s.split(':')

L = [L[k].strip() for k in range(len(L))]

print L
