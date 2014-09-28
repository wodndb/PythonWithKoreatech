#!/usr/local/bin/python
# coding: utf-8
import sys, os

def div_path(s):
	result = s.rsplit('/', 1);
	return result


print div_path('usr/local/bin/python')
print div_path('home/chulsoo/test.txt')
