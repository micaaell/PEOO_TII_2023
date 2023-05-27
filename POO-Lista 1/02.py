class Notas:
	def __init__(self):
		self.disciplina= " "
		self.nota1=0
		self.nota2=0
		self.nota3=0
		self.nota4=0
		self.provafinal=0
	def media_parcial(self):
		return (self.nota1*2+self.nota2*2+self.nota3*3+self.nota4*3)/10
	def media_final(self):
		return (self.media_parcial() + self.provafinal)/2
			

v=Notas()
v.disciplina=str(input("Nome da Disciplina:"))
v.nota1=int(input("Digite a nota do 1 bimestre:"))
v.nota2=int(input("Digite a nota do 2 bimestre:"))
v.nota3=int(input("Digite a nota do 3 bimestre:"))
v.nota4=int(input("Digite a nota do 4 bimestre:"))
v.provafinal=int(input("Digite a nota da prova final:"))
print(f"Media parcial dos 4 bimestres: {v.media_parcial()}")
if v.media_parcial()<60:
	print(f"Media final com prova: {v.media_final()}")
