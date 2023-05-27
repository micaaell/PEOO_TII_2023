class Viagem:
	def __init__(self):
		self.distancia=0
		self.tempo=0
	def calculo(self):
		return self.distancia / self.tempo
v=Viagem()
v.distancia=int(input("Digite a distancia em km:"))
h,m=map(int, input("Digite o tempo em hh:mm:").split(':'))
t = h+m/60
v.tempo=t
print(f"Velocidade Media:{v.calculo()} km/h")
