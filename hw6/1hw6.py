a=(input("Введите что-нибудь: "))
b=(input("И еще что-нибудь: "))
a=a.split(" ")
b=b.split(" ")
print(set(a)&set(b))