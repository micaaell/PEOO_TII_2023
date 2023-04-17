valor=0
posicao=0
for i in range(100):
    numero=int(input())
    if(numero>valor):
        valor=numero
        posicao=i
print(valor)
print(posicao+1)
