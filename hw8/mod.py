def mod():
	x=int(input("Введите число: "))
	if x>=0:
		print('|', x, '|=', x)
	else:
		x=-x
		print('|', x, '|=', x)
mod()