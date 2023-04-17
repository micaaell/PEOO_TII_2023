n = int(input())
for i in range(n):
  n1,n2=input().split(" ")
  n1=int(n1)
  n2=int(n2)
  if (n2==0):
    print("divisao impossivel")
  print(f"{(n1/n2):0.1f}")
