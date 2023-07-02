class Cliente:
	def __init__(self,nome,cpf,limite):
		self.__nome=nome
		self.__cpf=cpf
		self.__limite=limite
		self.__socio=None
		
	def setsocio(self,socio):
		if socio%2==0:
			socio=self.__socio
		else: raise ValueError()
	def getlimite(self):
		return self.__limite
	def __str__(self):
		return f"Nome: {self.__nome} CPF: {self.__cpf} Limite: {self.__limite} Socio: {self.__socio}"

class Empresa:
	def __init__(self):
		self.__clientes=[]
	def inserir(self,c):
		if c in self.__clientes:
			raise ValueError()
		else: self.__clientes.append(c)
	def listar(self):
		return self.__clientes
class UI:
	def main():
		e=Empresa()
		print("1 - Inserir cliente, 2 - Listar, 0 - Fim")
		op = int(input("Escolha: "))
		while op !=0:
			if op==1:
				nome=str(input())
				cpf=str(input())
				limite=float(input())
				c=Cliente(nome,cpf,limite)
				e.inserir(c)
			if op==2:
				for k in e.listar():
					print(k)
			if op==3:
				print("1 - Inserir Cliente, 2 - Listar, 0 - Fim")
			op = int(input("Escolha: "))
				
		



UI.main()
	
