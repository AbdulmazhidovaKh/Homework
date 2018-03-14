def kv():
  x=input("Введите уравнение: ")
  x=x.split("x")
  x[1]=x[1][2:]
  i=0
  d=len(x)
  while i<=(d-1) :
  	x[i]=float(x[i])
  	i+=1
  d=x[1]**2-4*x[0]*x[2]
  x1=(-x[1]+d**0.5)/2
  x2=(-x[1]-d**0.5)/2
  if d==0:
  	print("Единственный корень:", x2)
  elif d>0:
  	print("Два корня:", x1,"и", x2)
  else:
  	print("Нет корней")

kv()
