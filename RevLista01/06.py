print("Digite três valores:")
n1=int(input())
n2=int(input())
n3=int(input())
soma=0
if n1<n2 and n1<n3 or (n1>n2 and n1>n3):
	soma+=n1
if n2<n1 and n2<n3 or (n2>n1 and n2>n3):
	soma+=n2
if n3<n1 and n3<n2 or (n3>n2 and n3>n1):
	soma+=n3
print(soma)
