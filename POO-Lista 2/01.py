class Circulo:
	def __init__(self,r):
		self.__raio=0
		self.set__raio(r)
	def set__raio(self,r):
		if r >=0: 
			self.__raio= r
	def get__raio(self,r):
		return self.set__raio
	def calc_area(self):
		return 3.14*(self.__raio**2)
	def calc_circu(self):
		return 2*3.14*self.__raio


class UI:
	@staticmethod
	def main():
		r=float(input("Digite o valor do Raio:"))
		v=Circulo(r)
		print(f"Area: {v.calc_area()}")
		print(f"Circuferencia:{v.calc_circu()}")
		

UI.main()
