#/usr/local/bin/python
# coding: utf-8
import sys, os, pickle

urlList = {"http://cse.koreatech.ac.kr", "http://www.koreatech.ac.kr", "http://www.naver.com", "http://www.daum.net", "http://link.koreatech.ac.kr"}

maxValues = 0
maxKeys = ' '
maxUrls = ' '

totalDict = {}

for urls in urlList:
	freqFile = open(urls[7:] + ".words.frequency")
	D = pickle.load(freqFile)
	keys = totalDict.keys()
	for key, value in D.items():
		if(key in keys):
			totalDict[key] += value
		else:
			totalDict[key] = value

for key, value in totalDict.items():
	if(maxValues < value):
		maxValues = value
		maxKeys = key
	elif(maxValues == value):
		maxKeys.append(key)

print "The max of frequency key is", maxKeys, ':', maxValues
print "in", urlList
