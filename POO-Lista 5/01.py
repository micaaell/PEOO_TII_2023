import datetime

class Paciente:
	def __init__(self,nome,cpf,telefone,nascimento):
		self.__nome=nome
		self.__cpf=cpf
		self.__telefone=telefone
		self.__nascimento=nascimento
		self.setnome(nome)
		self.setcpf(cpf)
		self.settelefone(telefone)
		self.setnascimento(nascimento)
	def setnome(self,nome):
		if nome!=' ':
			nome=self.__nome
		else: raise ValueError()
	def setcpf(self,cpf):
		if cpf!=0:
			cpf=self.__cpf
		else: raise ValueError()
	def settelefone(self,telefone):
		if telefone!=0:
			telefone=self.__telefone
		else: raise ValueError()
	def setnascimento(self,nascimento):
		if nascimento!=00:
			self.__nascimento=datetime.datetime(nascimento[2], nascimento[1], nascimento[0])
		else: raise ValueError()
	def getnome(self):
		return self.__nome
	def getcpf(self):
		return self.__cpf
	def gettelefone(self):
		return self.__telefone
	def getnascimento(self):
		return self.__nascimento
	def idade(self):
		delta= datetime.datetime.today()-self.__nascimento
		dias = delta.days
		anos = dias // 365
		meses = dias % 365 //30
		return f'Idade do paciente: {anos} ano(s) e {meses} mes(es)'
	def __str__(self):
		nasci_texto = self.__nascimento.strftime('%d/%m/%y')
		return f'Nome: {self.__nome}\nCPF: {self.__cpf}\nTelefone: {self.__telefone}\nData de nascimento: {nasci_texto}'
class UI:
	@staticmethod
	def main():
		nome = input('Informe seu nome:\n')
		cpf = input('Informe seu CPF:\n')
		telefone = input('Informe seu telefone:\n')
		nascimento = list(map(int, input('Informe sua data de nascimento (DD/MM/AAAA):\n').split('/')))
		x = Paciente(nome, cpf, telefone, nascimento)
		print(x.idade())
		print(x)

UI.main()
