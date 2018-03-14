from os import rename, mkdir 
from shutil import rmtree
st=int(input("""Выберите действие: 
1-Открыть папку.
2-Создать папку.
3-Переименовать папку.
4-Удалить папку.
"""))
if st==1:
	q=input("Имя папки: ")
	open(q) #help me

elif st==2:
	name=input("Дайте имя папке: ")
	mkdir(name)

elif st==3:
	a=input("Старое имя папки: ")
	b=input("Новое имя папки: ")
	rename(a, b)

elif st==4:
	d=input("А именно? ")
	rmtree(d)