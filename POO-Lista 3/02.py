class Frete:
	def __init__(self,distancia,peso):
		self.__distancia=distancia
		self.__peso=peso
	def set_distancia(self,distancia):
		if distancia>=0:
			self.__distancia=distancia
	def set_peso(self,peso):
		if peso>=0:
			self.__peso=peso
	def get_distancia(self):
		return self.__distancia
	def get_peso(self):
		return self.__peso
	def calc_frete(self):
		return (self.__peso * self.__distancia)*0.1
	def __str__(self):
		return f"Distancia= {self.__distancia}km e Peso= {self.__peso}kg"

class UI:
	distancia=int(input("Digite a distancia em km:"))
	peso=int(input("Digite o peso em kg:"))
	v=Frete(distancia,peso)
	print(f"Valor do frete: R$ {v.calc_frete()}")
	print(v)
