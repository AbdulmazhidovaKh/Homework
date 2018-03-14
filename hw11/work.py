class User:
	def __init__(self, name, surname, password, ph, mail):
		self.name=name
		self.surname=surname
		self.password=password
		self.ph=ph
		self.mail=mail
	
	def sigh_up(self):
		print("Вы зaрегистрированы!")
	
	def sigh_in(self):
		print("Вы вошли в систему.")

class Aspirant(User):
	def __init__(self, name, surname, password, ph, mail, prof, seniority, education):
		super().__init__(name, surname, password, ph, mail)
		self.prof=prof
		self.seniority=seniority
		self.education=education

	def post_r(self):
		print("Ваше резюме размещено на сайте, ожидайте ответа.")

	def  interview(self, vac):
		print("Откликнуться на вакансию" + vac)

class Boss(User):
	def __init__(self, name, surname, password, ph, mail, company, type_c, vacancy):
		super().__init__(name, surname, password, ph, mail)
		self.company=company
		self.type_c=type_c
		self.vacancy=vacancy

	def post_v(self):
		print("Вакансия размещена.")

	def interview(self, time, address):
		print("Собеседование назначено в " + time + " по адресу: " + address + ".")


		