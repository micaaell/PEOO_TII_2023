class Cinema:
	def __init__(self):
		self.dia=" "
		self.horario=0
	def valor_entrada(self):
		if self.dia== "quarta":
			return 8
		if self.dia=="segunda" or "terca" or "quinta":
			if self.horario >=17:
				return 24
			else:
				return 16
		if self.dia == "sexta" or "sabado" or "domingo":
			if self.horario>=17:
				return 30
			else:
				return 20
	def valor_meia(self):
		if self.dia== "quarta":
			return 8
		if self.dia=="segunda" or "terca" or "quinta":
			if self.horario >=17:
				return 12
			else:
				return 8
		if self.dia == "sexta" or "sabado" or "domingo":
			if self.horario >=17:
				return 15
			else:
				return 10

v=Cinema()
v.dia=str(input("Digite o Dia:"))
v.horario,min=map(int, input("Digite o tempo em hh:mm:").split(':'))
print(f"Valor do ingresso em uma entrada: R$ {v.valor_entrada()},00")
print(f"Valor do ingresso em uma meia-entrada: R$ {v.valor_meia()},00")
