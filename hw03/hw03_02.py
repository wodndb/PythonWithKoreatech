#!/usr/local/bin/ipython
# coding: utf-8

S = 'Hello World and Python'
L = S.split()
print "원래 문자열 :", S
L.reverse()
RL = ' '.join(L)
print "거꾸로 출력 :", RL
RRL = ''.join(RL.split())
print '공백 제거 :', RRL
