#boletin 5, 1

for i in range(10, 21):
    print(i)

#boletin 5, 2

F = float(input("Dime una medida para pasarla a grados celsius"))

C = (F - 32) * 5/9

print(C)

#boletin 5, 3

F = float(input("Dime una medida para pasarla a grados celsius"))

for F in range(0, 121, 10):

    C = (F - 32) * 5 / 9

print(F, "ºF=", round(C, 2), "ºC")

#boletin 5, 4

try:
    inicio = int(input("Introduce el primer número: "))
    fin = int(input("Introduce el segundo número: "))
except ValueError:
    print("Por favor, introduce números enteros.")
    raise SystemExit

if inicio > fin:
    inicio, fin = fin, inicio

start = inicio if inicio % 2 == 0 else inicio + 1

for n in range(start, fin + 1, 2):
    print(n)

#boletin 5, 5

b = int(input("Dime un numero para escribir los primeros numeros triangulares"))

for m in range(1, b + 1):
    triangular = m * (m + 1) // 2
    print(m, "-", triangular)

#boletin 5, 6

m = int(input("¿Cuántos valores quieres ingresar? "))

for i in range(1, m + 1):
    num = int(input(f"Introduce el valor #{i}: "))


    factorial = 1
    for j in range(1, num + 1):
        factorial *= j

    print(f"{i} - {num}! = {factorial}")

#boletin 5, 7

for i in range(7):
    for j in range(i, 7):
        print(i, "-", j)




