def calc():
	ex=list(input("Введите пример:"))
	ex[0]=float(ex[0])
	ex[2]=float(ex[2])

	if ex[1]=='+':
		print("Ответ:", ex[0]+ex[2])
	elif ex[1]=='-':
		print("Ответ:", ex[0]-ex[2])
	elif ex[1]== "/":
		print("Ответ:", ex[0]/ex[2])
	elif ex[1]=='*':
		print("Ответ:", ex[0]*ex[2])
	elif ex[1]=='^':
		print("Ответ:", ex[0]**ex[2])
	
calc()
