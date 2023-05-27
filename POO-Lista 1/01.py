class Circulo:
	def __init__(self):
		self.raio=0
		
	def area(self):
		return 3.14*(self.raio**2)
	def circuferencia(self):
		return 2*(3.14*self.raio)
		
		
v=Circulo()
v.raio=float(input("Digite o valor do Raio:"))
print(v.area())
print(v.circuferencia())
