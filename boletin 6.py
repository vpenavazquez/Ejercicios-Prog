#boletin 6, 1
asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lingua"]

notas = {}

for asignatura in asignaturas:
    nota = input(f"Que nota sacaches en {asignatura}? ")
    notas[asignatura] = nota

for asignatura in asignaturas:
    print(f"En {asignatura} sacaches {notas[asignatura]}")

#boletin 6, 3

numeros = list(range(1, 11))

print(numeros[::-1])

#BOLETIN 6, 4

asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lingua"]

suspensas = []

for asignatura in asignaturas:
    nota = float(input(f"Que nota sacaches en {asignatura}? "))
    if nota < 5:
        suspensas.append(asignatura)
if suspensas:
    print("Tes que repetir as seguintes asignaturas:")
    for asignatura in suspensas:
        print(f"- {asignatura}")
else:
    print("Parabéns! Aprobaches todas as asignaturas.")


#boletin 6, 5

abecedario = list("abcdefghijklmnopqrstuvwxyz")
resultado = []

for i in range(len(abecedario)):
    if (i + 1) % 3 != 0:
        resultado.append(abecedario[i])

print(resultado)

#boletin 6, 6

palabra = input("Introduce unha palabra: ")
if palabra == palabra[::-1]:
    print("É un palíndromo.")
else:
    print("Non é un palíndromo.")

#boletin 6, 7

palabra = input("Escribe unha palabra para contar as vogais")

vogais = ['a', 'e', 'i', 'o', 'u']

for vogal in vogais:
    contador = palabra.count(vogal)
    print(f"A vogal '{vogal}' aparece {contador} veces.")

#boletin 6, 8

prezos = [50, 75, 46, 22, 80, 65, 8]
print("O menor prezo é:", min(prezos))
print("O maior prezo é:", max(prezos))






