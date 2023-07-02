import datetime
class Musica:
	def __init__(self,titulo,artista,album,duracao):
		self.__titulo=titulo
		self.__artista=artista
		self.__album=album
		self.__datadeinclucao=datetime.datetime.today()
		self.__duracao=duracao
	def getduracao(self):
		return self.__duracao
	
	def __str__(self):
		data =self.__datadeinclucao.strftime("%d/%m/%Y")
		return f"Titulo: {self.__titulo} Artista: {self.__artista} Album: {self.__album} Data:{data} Duração: {self.__duracao}"

class Playlist:
	def __init__(self,nome,descricao):
		self.__nome=nome
		self.__descricao=descricao
		self.__musicas=[]
	def inserir(self,m):
		if m in self.__musicas:
			raise ValueError("música já inserida na playlist")
		else: self.__musicas.append(m)
	def listar(self):
		return self.__musicas
	def tempototal(self):
		total=datetime.timedelta()
		for k in self.__musicas:
			total+=k.getduracao()
		return total
	def __str__(self):
		return f"Nome:{self.__nome} Descrição: {self.__descricao}"

class UI:
	def main():
		p=Playlist("Os crias","Musicas de metro")
		print("1 - Inserir música, 2 - Listar, 3 - Tempo total, 0 - Fim")
		op = int(input())
		while op != 0:
			if op == 1:
				titulo = input("Título da música: ")
				artista = input("Banda: ")
				album = input("Álbum: ")
				duracao = input("Duração (mm:ss): ")
				min, sec = map(int, duracao.split(":"))
				duracao = datetime.timedelta(minutes=min, seconds=sec)
				m = Musica(titulo, artista, album, duracao)
				p.inserir(m)
			if op == 2:
				for k in p.listar(): 
					print(k)
			if op == 3:  
				print(p.tempo_total)
			print("1 - Inserir música, 2 - Listar, 3 - Tempo total, 0 - Fim")
			op = int(input())

UI.main()
		
		
