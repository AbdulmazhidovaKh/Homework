class Mat:
	def sum(self, mat1, mat2):
		a=mat1[0]
		a1=mat1[0]

		b=mat2[0]
		b1=mat2[1]

		x=a[0]+b[0]
		x1=a[1]+b[1]
		l1=[x, x1]

		z=a1[0]+b1[0]
		z1=a1[1]+b1[1]
		l2=[z, z1]

		l3=[l1, l2]

		print(l3)

	def mult(self, mat1, mat2):
		a1=mat1[0][0]
		a2=mat1[0][1]
		b1=mat1[1][0]
		b2=mat1[1][1]
			
		c1=mat2[0][0]
		c2=mat2[0][1]
		d1=mat2[1][0]
		d2=mat2[1][1]

		x1=a1*c1+b1*c2
		x2=a2*c1+b2*c2
		l1=[x1, x2]

		z1=a1*d1+b1*d2
		z2=a2*d1+b2*d2
		l2=[z1, z2]

		l3=[l1, l2]

		print(l3)


q=Mat()
q.mult([[2,4], [-3,-6]], [[9,6], [-6,-4]])

