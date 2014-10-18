#!/usr/local/bin/python
# coding: utf-8
import sys, os, urllib, string

s = urllib.urlopen('http://cse.koreatech.ac.kr').read()


n = 0
pivot = 0
while(n < len(s)):
	if(s[n] == "<" and s[n + 1 : n + 7].lower() == "script"):
		pivot = n
		while(s[pivot] != "<" or s[pivot + 1] != "/" or s[pivot + 2 : pivot + 8].lower() != "script"):
			pivot += 1
		s = s[0:n] + ' ' + s[pivot+9:]

	elif(s[n] == "<" and s[n + 1 : n + 6].lower() == "style"):
		pivot = n
		while(s[pivot] != "<" or s[pivot + 1] != "/" or s[pivot + 2 : pivot + 7].lower() != "style"):
			pivot += 1
		s = s[0:n] + ' ' + s[pivot+8:]

	elif(s[n] == '<'):
		pivot = n
		while(s[pivot] != '>'):
			pivot += 1
		s = s[0:n] + ' ' + s[pivot+1:]
	elif(s[n] == '\n' or s[n] == '\t'):
		s = s[0:n] + ' ' + s[n+1:]
	elif(s[n] in string.punctuation):
		s = s[0:n] + s[n+1:]
	else:
		n += 1

s2 = s.split()
s3 = ' '.join(s2)
n = 0
D = {}
while(n < len(s2)):
	if(s2[n] in D.keys()):
		D[s2[n]] += 1
	else:
		D[s2[n]] = 1
	n += 1
	

print 'number of character :', len(s.split())
print '<characters in webpage>'
print s3

for key, value in D.items():
	print key, ":",  value 
