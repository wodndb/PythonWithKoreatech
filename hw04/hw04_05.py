#/usr/local/bin/python
# coding: utf-8

import sys, os

def myinitial(string):
	return ''.join(map(lambda x: x.capitalize()[0], string.split()))

print " # myinitial(\"as soon as possible\")"
print myinitial("as soon as possible")
