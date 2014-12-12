#/usr/local/bin/python
# coding: utf-8

class MySet(list):
	def __init__(self, l):
		for e in l:
			self.append(e)
		MySet.eliminate_duplicate(self)

	def __str__(self):
		result = "MySet: {"
		for e in self:
			result = result + str(e) + ", "
		result = result[0:len(result) - 2] + "}"
		return result
	
	def __or__(self, otherList):
		for e in otherList:
			self.append(e)
			MySet.eliminate_duplicate(self)
		return self

	def __and__(self, otherList):
		s = []
		for e in otherList:
			if e in self:
				s.append(e)
		return MySet(s)
	
	def __sub__(self, otherList):
		s = []
		for e in self:
			if e not in otherList:
				s.append(e)
		return MySet(s)	

	@staticmethod
	def eliminate_duplicate(l):
		s = []
		for e in l:
			if e not in s:
				s.append(e)
		l[:] = []
		for e in s:
			l.append(e)

if __name__ == "__main__":
	s = MySet([1, 2, 2, 3])
	print s
	t = MySet([2, 3, 4, 5, 6, 7, 8, 8, 8, 8, 8, 9])
	print t
	
	# Requirement 1
	s = s | t
	print s
	
	# Requirement 2
	s = MySet([1, 2, 3])
	t = MySet([3, 4, 5])
	s = s & t
	print s
	
	# RequireMent 3
	s = MySet([1, 2, 3])
	t = MySet([3, 4, 5])
	s = s - t
	print s
