import datetime
class Local:
	def __init__(self,id,endereco,nome):
		self.__id=id
		self.__endereco=endereco
		self.__nome=nome
		self.set_id(id)
		self.set_endereco(endereco)
		self.set_nome(nome)
	def set_id(self,id):
		if id>0:
			self.__id=id
		else:raise ValueError()
	def set_endereco(self,endereco):
		if endereco>0:
			self.__endereco=endereco
		else:raise ValueError()
	def set_nome(self,nome):
		if nome>0:
			self.__nome=nome
		else:raise ValueError()
	def get_id(self):
		return self.__id
	def get_endereco(self):
		return self.__endereco
	def get_nome(self):
		return self.__nome
	def __str__(self):
		return f"id={self.__id},endereco={self.__endereco},nome={self.__nome}"
		
class Evento:
	def __init__(self,id,idLocal,valoringresso,data,nome):
		self.__id=id
		self.__idLocal=idLocal
		self.__valoringresso=valoringresso
		self.__data=data
		self.__nome=nome
	def set_id(self,id):
		if id==str():
			self.__id=id
		else:raise ValueError()
	def set_idLocal(self,idLocal):
		if idLocal==str():
			self.__idLocal=idLocal
		else:raise ValueError()
	def set_valoringresso(self,valoringresso):
		if valoringresso>0:
			self.__valoringresso=valoringresso
		else:raise ValueError()
	def set_data(self,data):
		if data>0:
			self.__data=data
		else: raise ValueError()
	def set_nome(self,nome):
		if nome==str():
			self.__nome=nome
		else:raise ValueError()
	def get_id(self):
		return self.__id
	def get_idLocal(self):
		return self.__idLocal
	def get_valoringresso(self):
		return self.__valoringresso
	def get_data(self):
		return self.__data
	def get_nome(self):
		return self.__nome
	def __str__(self):
		return f"id={self.__id},idLocal={self.__idLocal},Valor do Ingresso={self.__valoringresso},Data={self.__data} e Nome={self.__nome}"

class Nlocal:
	def __init__(self):
		self.locais=[]
	def inserir(self,i):
		self.locais.append(i)
	def listar(self):
		return self.locais
	def atualizar(self,i):
		for obj in self.locais:
			if obj.get_id()==i.get_id():
				obj.set_nome(i.get_nome())
				obj.set_endereco(i.get_endereco())
	def deletar(self,i):
		self.locais.remove(i)

class UI:
	def menu():
		print("0-fim,1-inserir,2-Listar,3-Atualizar,4-Remover")
		return int(input())
	def main():
		op = 1
		E=Evento("id",'idLocal','valoringresso','data','nome')
		Nl=Nlocal()
		while op!=0:
			op = UI.menu()
			if op==1:
				id=int(input("Digite o id:"))
				endereco=int(input("Digite o endereco:"))
				nome=int(input("Digite o Nome:"))
				i=Local(id,endereco,nome)
				Nl.inserir(i)
			if op==2:
				for i in Nl.listar():
					print(i)
			if op==3:
				print(Nl.atualizar(i))
			if op==4:
				print(Nl.deletar(i))
			
				
UI.main()
