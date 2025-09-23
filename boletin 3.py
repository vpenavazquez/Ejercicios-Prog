#Codifica un programa que solicite un número por teclado e que saque un mensaxe que diga “É un número positivo”, sempre que cumpra esa condición.
from enum import IntFlag

numero = float(input("Introduce un número: "))
if numero > 0:
    print("É un número positivo")

#Escribe un programa no que se tecleen dous números. Se o primeiro é maior ou igual que o segundo,visualizaremos a resta. En calquera caso visualizaremos a suma.


num1 = float(input("Introduce o primeiro número: "))
num2 = float(input("Introduce o segundo número: "))

if num1 >= num2:
    print("A resta é:", num1 - num2)

print("A suma é:", num1 + num2)

#Codificar o programa que o teclear un número por teclado, mostre por consola o signo “ + “ se o número é positivo, o signo “ –“ se é negativo e “ 0 “ se é cero.

num = float(input("Introduzca un numero"))

if num < 0:
    print("-")
elif num > 0:
    print("+")
else:
    print("0")

#Coñecidos, o nome e o peso de dúas persoas, o programa escribirá por consola os datos da persoa que pesa máis e a diferenza de peso entre elas.

nome1 = input("Introduce un nombre")
peso1 = float(input("Introduce un peso"))

nome2 = input("Introduce un nombre")
peso2 = float(input("Introduce un peso"))

if peso1 > peso2:
    print(nome1, peso1, "la diferencia de peso es", peso1 - peso2)

elif peso1 < peso2:
    print(nome2, peso2, "la diferencia de peso es", peso2 - peso1)

#5- Dados 3 números que se supoñen distintos, indicar cal é o maior.

n1 = float(input("Introduce o primeiro número: "))
n2 = float(input("Introduce o segundo número: "))
n3 = float(input("Introduce o terceiro número: "))


if n1 > n2 and n1 > n3:
    print("O maior é:", n1)
elif n2 > n1 and n2 > n3:
    print("O maior é:", n2)
else:
    print("O maior é:", n3)