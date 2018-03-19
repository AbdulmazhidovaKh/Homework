class Vector:
	def sum(self, vect1, vect2):
		if len(vect1)==len(vect2):
			x1=vect1[0]+vect2[0]
			x2=vect1[1]+vect2[1]
			l=[x1, x2]

			print(l)

		else:
			print("Операция недоступна.")

	def mult(self, vect1, vect2):
		if len(vect1)==len(vect2):
			x1=vect1[0]*vect2[0]
			x2=vect1[1]*vect2[1]
			l=[x1, x2]

			print(l)

		else:
			print("Операция недоступна.")


