from time import sleep #подключение функции "sleep" из модуля  "time" 

class Typical_dag_05: #описание класса
	favorite_phrase = 'Жи есть' #свойство класса
	red_moccasins = True #свойство класса
	iq = 80 #свойство класса
	respect_to_elders = None #свойство класса 

	def no_work(self): #метод класса
		while True: #цикл
			sleep(1) #остановочка на 1 сек

	def speak(self): #метод класса
		print(self.favorite_phrase) #

man = Typical_dag_05() #создание объекта класса 
print(man.iq) #вывод одного из свойств класса: "iq"
man.favorite_phrase = 'Mom, give me money, please.' #изменение свойства 

man.speak() #вызов метода класса
