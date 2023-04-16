n1=int(input())
n2=int(input())
n3=int(input())
n4=int(input())
media=(n1+n2+n3+n4)/4
print(media)
print("Números menores que a média")
if n1<media:
  print(n1)
if n2<media:
  print(n2)
if n3<media:
  print(n3)
if n4<media:
  print(n4)
print("Números maiores ou iguais à média")
if n1>=media:
  print(n1)
if n2>=media:
  print(n2)
if n3>=media:
  print(n3)
if n4>=media:
  print(n4)
