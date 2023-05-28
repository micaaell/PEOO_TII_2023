class Triangulo:
	def __init__(self, b, h):
		self.__b = b
		self.__h = h
	def set_base(self,b):
		if self.__b>=0:
			self.__b=b
	def set_altura(self,h):
		if self.__h>=0:
			self.__h=h
	def get_base(self,b):
		return self.__b
	def get_altura(self,h):
		return self.__h

	def calc_area(self):
		return self.__b * self.__h /2
	def calc_diagonal(self):
		return ((self.__b* self.__b)+(self.__h * self.__h))**(1/2)
	def __str__(self):
		return f"Base ={self.__b} - Altura ={self.__h}"
class UI:
	def main():
		b=int(input())
		h=int(input())
		x = Triangulo(b,h)
		print(x.calc_area())
		print(x.calc_diagonal())
		print(x)
UI.main()
