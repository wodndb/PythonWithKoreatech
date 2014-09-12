#!/usr/local/bin/python
# coding: utf-8
import sys, os

#이 코드는 리북스 우분투 14.04 LTS 환경의 vim에디터로 작업한 것으로, 한글 인코딩 문제를 해결하기 위해 위의 세 줄의 코드가 우선적으로 삽입되어야 합니다.

a = "Hello Python"
print "변경 전 : " + a
a = a[6::] + ' ' + a[0:5]	#Slicing 및 연결 연산자 사용
print "변경 후 : " + a
