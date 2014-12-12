#!/usr/local/bin/python
# coding: utf-8
import sys, os, urllib, string

def printDictForKorKey(d):
	if len(d) == 0:
		print {}
	else:
		print '{',
		for key, value in d.items():
			print '\'' + key + '\': ', value, ',',
		print '}'


# Url을 파싱하여 단어 및 단어 개수를 사전 형태로 반환하는 함수다.
def parsingUrl(url):
	s = urllib.urlopen(url).read()
	
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
	
	return D
	

# 웹사이트 상의 단어 빈도에 대한 정보를 다루는 클래스다.
class WebWordsFrequency:

	# 생성자
	def __init__(self, *urls):
		self.urlList = list(urls)

	# Url 추가
	def addUrl(self, strUrl):
		self.urlList.append(strUrl)

	# Url 삭제
	def removeUrl(self, strUrl):
		self.urlList.remove(strUrl)

	# Url 목록 출력
	def listUrls(self):
		for e in self.urlList:
			print e

	# 저장된 웹사이트 url에 기반한 단어 빈도 사전 출력
	def getWordsFrequency(self):
		totalDict = {}
	
		for urls in self.urlList:
			D = parsingUrl(urls)
			keys = totalDict.keys()
			for key, value in D.items():
				if(key in keys):
					totalDict[key] += value
				else:
					totalDict[key] = value
		return totalDict

	# 최다 빈도 출현 단어 출력
	def getMaxFrequencyWords(self):
		if len(self.urlList) == 0:
			return None
		else:
			maxValues = 0
			maxKeys = []
			maxUrls = ' '
			
			totalDict = {}
	
			for urls in self.urlList:
				D = parsingUrl(urls)
				keys = totalDict.keys()
				for key, value in D.items():
					if(key in keys):
						totalDict[key] += value
					else:
						totalDict[key] = value
		
			for key, value in totalDict.items():
				if(maxValues < value):
					maxValues = value
					maxKeys = [key]
				elif(maxValues == value):
					maxKeys.append(key)
			
			print "<Maximum Frequency Word List>"
			print " - Frequency : ", maxValues
			for k in maxKeys:
				print k
			print

if __name__ == "__main__":
	# Requirement 1
	w1 = WebWordsFrequency('http://www.daum.net', 'http://www.naver.com', 'http://www.google.co.kr')
	w2 = WebWordsFrequency('http://www.daum.net', 'http://www.naver.com')
	w3 = WebWordsFrequency()

	# Requirement 2
	w1.addUrl('http://cse.koreatech.ac.kr')
	w3.addUrl('http://www.koreatech.ac.kr')

	# Requirement 3
	w1.removeUrl('http://www.daum.net')
	w2.removeUrl('http://www.naver.com')

	# Requirement 4
	w1.listUrls()

	# Requirement 5
	printDictForKorKey(w1.getWordsFrequency())

	# Requirement 6
	w1.getMaxFrequencyWords()
	w2.getMaxFrequencyWords()

