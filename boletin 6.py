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

#boletin 6, 8

prezos = [50, 75, 46, 22, 80, 65, 8]
print("O menor prezo é:", min(prezos))
print("O maior prezo é:", max(prezos))

