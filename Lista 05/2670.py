pessoa1=int(input())
pessoa2=int(input())
pessoa3=int(input())
minutos1=pessoa1*0 + pessoa2*2+ pessoa3*4
minutos2=pessoa1*2 + pessoa2*0 + pessoa3*2
minutos3= pessoa1*4 + pessoa2*2 + pessoa3*0

if minutos1<=minutos2:
  menor=minutos1
else:
  menor=minutos2
if menor>=minutos3:
  menor=minutos3
print(menor)
