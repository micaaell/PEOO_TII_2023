class Entrada:
	def __init__(self,dia,horario):
		self.dia=0
		self.horario=0
		self.set_dia(dia)
		self.set_horario(horario)
	def set_dia(self,dia):
		if dia==str():
			self.dia=dia
	def set_horario(self,horario):
		if horario>=0:
			self.horario=horario
	def entrada(self):
		if self.dia=="quarta":
			return 8
		if self.dia=="segunda" or "terca" or "quinta":
			if self.horario>=17:
				return 24
			else:
				return 16
		if self.dia=="sexta" or "sabado" or "domingo":
			if self.horario>=17:
				return 20
			else:
				return 30
	def meiaentrada(self):
		if self.dia=="quarta":
			return 8
		if self.dia=="segunda" or "terca" or "quinta":
			if self.horario>=17:
				return 12
			else:
				return 8
		if self.dia=="sexta" or "sabado" or "domingo":
			if self.horario>=17:
				return 15
			else:
				return 20
class UI:
	def main():
		dia=str(input())
		horario,min=map(int,input().split(":"))
		v=Entrada(dia,horario)
		print(v.entrada())
		print(v.meiaentrada())
UI.main()
		
