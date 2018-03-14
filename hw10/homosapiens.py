class Human:
	hand="Большой палец противопоставлен остальным."
	have_sense_of_humor = True #не все
	eyesight="Цветное объемное."
	finger=5
	intellect="Высокий, хорошо развитый(но это не точно)"

	def greeting(self):
		print("Привет!")
	def eat(self):
		print("Омномном")
	def sleep(self):
		print("Пора в объятия Морфея.")
	def fact(self):
		print("Человек - единственный представитель животного мира, способный рисовать прямые линии.")

person=Human()
person.greeting()
person.fact()
