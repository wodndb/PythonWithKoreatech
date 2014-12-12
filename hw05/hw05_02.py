#/usr/local/bin/python
# coding: utf-8

class Poketmon:			#Parent Class
	def cry(self):
		print 'this is Poketmon class'

class Pikachu(Poketmon):	#Child Class 1
	def cry(self):
		print 'Pit-Ka-Chu!!!!'

class Pairi(Poketmon):		#Child Class 2
	def cry(self):
		print 'Pa----e---ri!'

class Butterfree(Poketmon):	#Child Class 3
	def cry(self):
		print 'Bba-Tta!'

for each in (Pikachu(), Pairi(), Butterfree()):
	each.cry()
