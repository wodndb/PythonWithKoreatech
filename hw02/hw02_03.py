#!/usr/local/bin/python
# coding: utf-8
import sys, os

num = int(raw_input('Please input integer number : '));
if((num >> 63) & 0x01 == 0x01):
	print num,'is negative number'
else:
	print num,'is positive number'

