def formatar_nome(nome):
	nome1=nome.split()
	listanome=[]
	for i in nome1:
		listanome.append(i.capitalize())
	final=str(listanome[0])
	for i in range(1,len(listanome)):
		final+=' '
		final+= listanome[i]
	return final
nome=input('Digite seu nome:')
print(f'Aqui está seu nome formatado: {formatar_nome(nome)}')
