#/usr/local/bin/python
# coding: utf-8

import sys, os
import math, cmath
from decimal import *

def frange(stmp, *arg):
	result = []
	if len(arg) > 3:
		print "The number of arguments in frange function must be same or smaller than 3"
		return -1

	elif len(arg) == 0:
		start = Decimal(0.0).quantize(Decimal(".000000000000001"), rounding = ROUND_DOWN)
		while start < stmp:
			result.append(float(start))
			start += Decimal(0.1).quantize(Decimal(".0000000000000001"), rounding = ROUND_DOWN)
		return result

	else:
		start = Decimal(stmp).quantize(Decimal(".000000000000001"), rounding = ROUND_DOWN)
		stop = Decimal(arg[0]).quantize(Decimal(".0000000000000001"), rounding = ROUND_DOWN)
		if len(arg) == 2:
			step = Decimal(arg[1]).quantize(Decimal(".000000000000001"), rounding = ROUND_DOWN)
		else:
			step = Decimal(0.1).quantize(Decimal(".0000000000000001"), rounding = ROUND_DOWN)

		while start < stop:
			result.append(float(start))
			start += step
		return result

print " # frange(0.5)"
print frange(0.5)
print
print " # frange(1.0, 2.0)"
print frange(1.0, 2.0)
print
print " # frange(2.2, 4.0, 0.5)"
print frange(2.2, 4.0, 0.5)
print
