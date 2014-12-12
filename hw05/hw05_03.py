class Counter:
	def __init__(self, count, step = 1):
		self.count = count
		self.step = step
	def __str__(self):
		return '[Count (step: ' + str(self.step) + ')] ' + str(self.count)
	def __call__(self):
		self.count = self.count + self.step
	def __add__(self, other):
		self.count = self.count + other
		return self
	def __sub__(self, other):
		self.count = self.count - other
		return self
	def __cmp__(self, other):
		return self.count - other
	def incr(self):
		self.count = self.count + self.step

# Requirement 1
c = Counter(10)
d = Counter(10, 2)

# Requirement 2
print c
print d

# Requirement 3
c.incr()
d.incr()
print c
print d

# Requirement 4
c()
d()
print c
print d

# Requirement 5
c = c + 5
d = d - 5
print c
print d

# Requirement 6
print c > 10
print d > 10
print c < 10
print d < 10
print c == 17
print d != 9
