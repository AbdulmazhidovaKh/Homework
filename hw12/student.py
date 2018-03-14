class Student:
	def __init__(self, name, surname, number_t, gpa, passes):
		self.name=name
		self.surname=surname
		self.number_t=number_t
		self.__gpa=gpa
		self.__passes=passes

	def sigh_up(self):
		print("Вы зaрегистрированы!")
	
	def sigh_in(self):
		print("Вы вошли в систему.")

	def get_passes(self):
		return "***"
	def set_passes(self, value):
		print("Error") 
	passes=property(get_passes, set_passes)

	def get_gpa(self):
		return "Конфиденциальная информация!" 
	def set_gpa(self, value):
		print("Error") 
	gpa=property(get_gpa, set_gpa)


class Math(Student):
	def __init__(self, name, surname, number_t, gpa, passes, course, group):
		super().__init__(name, surname, number_t, gpa, passes)
		self.course=course
		self.group=group

	def schedule(self):
		print("Расписание", self.group, "группы", self.course, " курса вы найдете по ссылке ниже.")


class Prog(Student):
	def __init__(self, name, surname, number_t, gpa, passes, course, group):
		super().__init__(name, surname, number_t, gpa, passes)
		self.course=course
		self.group=group

	def schedule(self):
		print("Расписание", self.group, "группы", self.course, " курса вы найдете по ссылке ниже.")


class Phys(Student):
	def __init__(self, name, surname, number_t, gpa, passes, course, group):
		super().__init__(name, surname, number_t, gpa, passes)
		self.course=course
		self.group=group

	def schedule(self):
		print("Расписание", self.group, "группы", self.course, "курса вы найдете по ссылке ниже.") 



