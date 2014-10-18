#!/usr/local/bin/python
# coding: utf-8

import sys, os
L1 = [1, 2, 3]
L2 = [4, 5, 6]
d = {'low':L1, 'high':L2}
e = d
f = d.copy()
print d
print e
print f
print
d['low'] = [10, 20, 30]
d['high'][1] = 500
print d
print e
print f
