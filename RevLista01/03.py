print("Digite quatro valores inteiros:")
n1=int(input())
n2=int(input())
n3=int(input())
n4=int(input())
par=0
impar=0
if n1%2==0:
	par=n1
else:
	impar=n1
if n2%2==0:
	par+=n2
else:
	impar+=n2
if n3%2==0:
	par+=n3
else:
	impar+=n3
if n4%2==0:
	par+=n4
else:
	impar+=n4
print(f"Soma dos pares = {par}")
print(f"Soma dos ímpares= {impar}")
