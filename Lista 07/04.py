def aprovado(nota1,nota2):
	media=(nota1 + nota2) /2
	final = ' '
	if media>=60:
		final= 'Aprovado'
	else:
		final= 'Reprovado'
nota1=int(input("Digita a nota 1: "))
nota2=int(input("Digita a nota 2: "))
print(aprovado(nota1,nota2))
