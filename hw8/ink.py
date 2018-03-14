def i_d():
	x=int(input("Введите число: "))
	st=int(input("""Выберите действие: 
1-Инкремент.
2-Декремент.
"""))
	if st==1:
		x+=1
		print(x)
	elif st==2:
		x-=1
		print(x)
	
i_d()