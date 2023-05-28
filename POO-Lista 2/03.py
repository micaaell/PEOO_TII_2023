class Viagem:
	def __init__(self,d,t):
		self.__distancia=0
		self.__tempo=0
		self.set_distancia(d)
		self.set_tempo(t)
	def set_distancia(self,d):
		if d>=0: self.__distancia = d
	def set_tempo(self,t):
		if t>0: self.__tempo= t
	def get_distancia(self):
		return self.__distancia
	def get_tempo(self):
		return self.__tempo
	def __str__(self):
		return f"Viagem - distância = {self.__distancia} - tempo = {self.__tempo}"
	def velocidade_media(self):
		if self.__tempo == 0: return 0
		return self.__distancia / self.__tempo
			

class UI:
	@staticmethod
	def main():
		print("Informe a distancia percorrida em km")
		d = float(input())
		print("Informe o tempo gasto em hh:mm")
		h,m=map(int, input().split(':'))
		t = h+m/60
		v = Viagem(d,t)
		print(f"{v.get_distancia()} Km")
		print(f"{v.get_tempo()} h")
		print(f"{v.velocidade_media()}km/h")
		print(v)

UI.main() 
