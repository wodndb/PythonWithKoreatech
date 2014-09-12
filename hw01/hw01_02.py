#!/usr/local/bin/python
# coding: utf-8
import sys, os

b = "Hello Python World"
print "변경 전 : " + b
b = b[13::] + ' '+ b[6:12] + ' ' + b[:5]
print "변경 후 : " + b
