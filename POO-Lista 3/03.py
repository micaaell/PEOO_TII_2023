class Equacao:
	def __init__(self,a,b,c):
		self.__a=a
		self.__b=b
		self.__c=c
	def set_a(self,a):
		self.__a=a
	def set_b(self,b):
		self.__b=b
	def set_c(self,c):
		self.__c=c
	def get_a(self):
		return self.__a
	def get_b(self):
		return self.__b
	def get_c(self):
		return self.__c
	def raiz1(self):
		return (-self.__b+(self.__b**2)-(4*self.__a*self.__c))/(2*self.__a)
	def raiz2(self):
		return (-self.__b-(self.__b**2)-(4*self.__a*self.__c))/(2*self.__a)
	def __str__(self):
		return f"A= {self.__a} , B={self.__b} e C={self.__c}"

class UI:
	a=int(input("Digite o valor de A:"))
	b=int(input("Digite o valor de B:"))
	c=int(input("Digite o valor de C:"))
	v=Equacao(a,b,c)
	print(f"Raiz 1 = {v.raiz1()}")
	print(f"Raiz 2 = {v.raiz2()}")
	print(v)
