#!/usr/local/bin/python
# coding: utf-8
import sys, os, urllib, string

s = urllib.urlopen('http://www.daum.net').read()


n = 0
pivot = 0
while(n < len(s)):
	if(s.startswith('<style', n)):
		pivot = n
		while(s.startswith('</style>', pivot) == False):
			pivot += 1
		s = s[0:n] + ' ' + s[pivot+8:]
	elif(s.startswith('<STYLE', n)):
		pivot = n
		while(s.startswith('</STYLE>', pivot) == False):
			pivot += 1
		s = s[0:n] + ' ' + s[pivot+8:]
	elif(s.startswith('<script', n)):
		pivot = n
		while(s.startswith('</script>', pivot) == False):
			pivot += 1
		s = s[0:n] + ' ' + s[pivot+9:]
	elif(s.startswith('<SCRIPT', n)):
		pivot = n
		while(s.startswith('</SCRIPT>', pivot) == False):
			pivot += 1
		s = s[0:n] + ' ' + s[pivot+9:]
	elif(s[n] == '<'):
		pivot = n
		while(s[pivot] != '>'):
			pivot += 1
		s = s[0:n] + ' ' + s[pivot+1:]
	elif(s[n] == '\n' or s[n] == '\t'):
		s = s[0:n] + ' ' + s[n+1:]
	else:
		n += 1

s2 = ' '.join(s.split())

print 'number of character :', len(s.split())
print '<characters in webpage>'
print s2

