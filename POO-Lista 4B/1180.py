casos = int(input())
lista = input()

vet = lista.split(" ")

menor = int(vet[0])
posicao = 0

for i in range(0,casos):
  vet[i] = int(vet[i])
  if vet [i]< menor:
    menor = vet[i]
    posicao = i
print(f'Menor valor: {menor}')
print(f'Posicao: {posicao}')
