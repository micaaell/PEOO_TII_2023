casos=[ ]
for i in range(0,10):
    casos.append(0)

for i in range(0,10):
  x=int(input())
  if (x>0):
    casos[i] = x
  else:
    casos[i]=1
    casos==1

for i in range(0,10):
  print("X[%d] = %d" %(i, casos[i]))
