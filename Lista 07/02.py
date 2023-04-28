def maior(x, y,z):
	if x>y and x>z:
		return x
		if y>x and y>z:
			return y
	else:
		return z

x=int(input())
y=int(input())
z=int(input())
print(maior(x,y,z))
