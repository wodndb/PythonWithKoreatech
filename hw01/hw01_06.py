#!/usr/local/bin/python
# coding: utf-8
import sys, os

i = 0		# while문의 조건 변수 겸 100까지 증가하는 짝수
result = 0	# 짝수들의 총합을 저장할 변수

while i < 100:		# i가 100에 도달할 때까지
	i += 2		# i에 2를 더하고
	result += i	# 증가된 짝수 i를 result에 저장한다.

print "1부터 100 사이의 짝수들의 합 :", result
