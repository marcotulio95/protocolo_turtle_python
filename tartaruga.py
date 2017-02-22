from turtle import *

class Tartaruga(object):
	
	def __init__(self, shape, speed):
		self.shape = shape
		self.speed = speed
		
	def hello(self):
		print ("hello world !")
	
	def TartarugaForward(self, valor):
		forward(valor)
		
	def TartarugaBackward(self, valor):
		backward(valor)
		
	def TartarugaLeft(self, valor):
		left(valor)
		
	def TartarugaRith(self, valor):
		right(valor)


t1 = Tartaruga("turtle", speed)
t1.TartarugaForward(100)
t1.TartarugaLeft(90)
t1.TartarugaForward(100)
done()

