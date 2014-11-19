#!/usr/local/bin/python
# coding: utf-8
import sys, os, urllib, string, pickle

urlList = {"http://www.koreatech.ac.kr", "http://cse.koreatech.ac.kr", "http://www.naver.com", "http://www.daum.net", "http://link.koreatech.ac.kr"}

def parsingUrl(url):
	s = urllib.urlopen(url).read()
	htmlFile = open(url[7:]+".html", "w")
	htmlFile.write(s)
	htmlFile.close()
	
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
	
	freqFile = open(url[7:]+".words.frequency", "w")
	pickle.dump(D, freqFile)

for urls in urlList:
	parsingUrl(urls)
