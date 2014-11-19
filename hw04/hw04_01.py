#/ust/local/bin/python
# coding: utf-8
import sys, os, math

def cmp_1(a1, a2):
	return cmp(a1[1], a2[1])

# Sorting 1 #

f0 = file("s.txt")
l1 = f0.readline()
tempList = []

while l1:
	tempList.append(l1.split())
	l1 = f0.readline()

tempList.sort()

f1 = open("s1.txt", "w+")
f1.write("\n".join([' '.join(x) for x in tempList]))
f1.seek(0)

print "[01]"
print f1.read()
print

# Sorting 2 #

f0 = file("s.txt")
l2 = f0.readline()
tempList = []

while l2:
	tempList.append(l2.split())
	l2 = f0.readline()

tempList.sort(cmp_1)

f2 = open("s2.txt", "w+")
f2.write("\n".join([' '.join(x) for x in tempList]))
f2.seek(0)

print "[02]"
print f2.read()
print

# Sorting 3 #

f0 = file("s.txt")
l3 = f0.readline()
tempList = []

i = 0

while l3:
	tempList = tempList + l3.split()
	l3 = f0.readline()

tempList2 = []

for x in range(int(math.ceil(len(tempList) / 3.0))):
	tempList2.append(tempList[3*x:3*(x+1)])

f3 = open("s3.txt", "w+")
f3.write("\n".join([' '.join(x) for x in tempList2]))
f3.seek(0)

print "[03]"
print f3.read()
print
