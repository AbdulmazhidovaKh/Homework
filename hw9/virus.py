from os import listdir, chdir, rename
def vi(a):
	sp=listdir(a)
	d=len(sp)
	chdir(a)
	for i in range(0, d):
		rename(sp[i],"Угадай, что я такое "+ str(i+1))