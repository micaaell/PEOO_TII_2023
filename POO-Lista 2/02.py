class Diciplina:
	def __init__(self,materia,n1,n2,n3,n4,provafinal):
		self.__meteria=" "
		self.__n1=0
		self.__n2=0
		self.__n3=0
		self.__n4=0
		self.__provafinal=0
		self.set_materia(materia)
		self.set_n1(n1)
		self.set_n2(n2)
		self.set_n3(n3)
		self.set_n4(n4)
		self.set_provafinal(provafinal)
	def set_materia(self,materia):
		if materia==str():
			self.__meteria=materia
	def set_n1(self,n1):
		if n1>=0:
			self.__n1=n1
	def set_n2(self,n2):
		if n2>=0:
			self.__n2=n2
	def set_n3(self,n3):
		if n3>=0:
			self.__n3=n3
	def set_n4(self,n4):
		if n4>=0:
			self.__n4=n4
	def set_provafinal(self,provafinal):
		if provafinal>=0:
			self.__provafinal=provafinal
	def get_materia(self,materia):
		return self.__materia
	def get_n1(self,n1):
		return self.__n1
	def get_n2(self,n2):
		return self.__n2
	def get_n3(self,n3):
		return self.__n3
	def get_n4(self,n4):
		return self.__n4
	def get_provafinal(self,provafinal):
		return self.__provafinal
	def calcu_media_parcial(self):
		return (self.__n1*2+self.__n2*2+self.__n3*3+self.__n4*3)/10
	def calcu_media_final(self):
		return (self.calcu_media_parcial() + self.__provafinal)/2

class UI:
	@staticmethod
	def main():
		materia=str(input("Nome da Disciplina:"))
		n1=int(input("Nota 1:"))
		n2=int(input("Nota 2:"))
		n3=int(input("Nota 3:"))
		n4=int(input("Nota 4:"))
		provafinal=float(input("Nota da prova final:"))
		v=Diciplina(materia,n1,n2,n3,n4,provafinal)
		print(f"Nota dos bimestres:{v.calcu_media_parcial()}")
		if v.calcu_media_parcial()<60:
			print(f"Nota com a prova final: {v.calcu_media_final()}")
		
UI.main()		
