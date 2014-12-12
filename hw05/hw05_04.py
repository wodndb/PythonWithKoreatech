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
