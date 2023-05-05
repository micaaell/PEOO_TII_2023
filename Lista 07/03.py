def iniciais(nome):
  palavras = nome.split()
  soma = ''
  for palavra in palavras:
    soma += palavra[0]
  return soma

nome = input('Escreva seu nome completo: ')
print(f'As iniciais do seu nome são: {iniciais(nome)}')
