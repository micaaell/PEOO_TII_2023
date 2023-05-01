first_hour = input()
second_hour = input()
uno = first_hour.split(":")
a = int(uno[0])
b = int(uno[1])
dios = second_hour.split(":")
c = int(dios[0])
d = int(dios[1])
hour = a + c
minutes = b + d 
if minutes < 60:
  print(f'Total de horas = {hour}:{minutes}')
elif minutes == 60:
  hour += 1
  minutes = minutes % 60
  print(f'Total de horas = {hour}:{minutes}0')
elif minutes > 60:
  hour += 1
  minutes -= 60
  print(f'Total de horas = {hour}:{minutes}')
