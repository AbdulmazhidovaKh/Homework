def kv():
	x=input("Введите (через запятую): ")
	x=x.split(", ")
	i=0
	d=len(x)
	while i<=(d-1):
		x[i]=float(x[i])
		i+=1
	a=x[0]
	b=x[1]
	c=x[2]
	d=b**2-4*a*c
	x1=(-b+d**0.5)/2
	x2=(-b-d**0.5)/2
	if d==0:
		print("Единственный корень:", x2)
	elif d>0:
		print("Два корня:", x1,"и", x2)
	else:
		print("Нет корней")
kv()