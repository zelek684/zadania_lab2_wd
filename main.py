# 1

sporty = ['golf' , 'boks' , 'siatkówka']
print(sporty)
sporty.reverse()
print(sporty)
sporty.append("karate")
sporty.append("Ju-jitsu")
print(sporty)


#2

skrot = {"zw.":"zaraz wracam" , "itd.":"i tak dalej"}
print(skrot)


#3

gry = {"FC":"Far Cry", "CS":"Counter Strike"}
print(gry)

#4

zdanie = str(input("Podaj zdanie: "))
print("ile znajduje sie liter a =",zdanie.count('a'))


#5

#6

a = int(input("Podaj a:"))
b = int(input("Podaj b:"))
c = int(input("Podaj c:"))
maks=a
if maks <b:
    maks=b
if maks <c:
    maks=c
print("maks",maks)


#7

lista = [0,1,2.5,3,6,7,3.14]
wyn=[]
for i in lista:
    wyn.append(i**2)
print(wyn)

#8

i=10
liczba =[]
while(i>0):
    temp = int(input("Podaj liczbe: "))
    if(temp%2==0):
        liczba.append(temp)
    i=i-1

print(liczba)


#9

for i in range(5):
    if(i%2==0):
        print("EEEEEE")
    else:
        print("E")

#10

import math
pierwiastek = int(input("Podaj liczba: "))
try:
    print(math.sqrt(pierwiastek))
except ValueError:
    print("Błąd")

