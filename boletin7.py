#boletin 7, 1

texto = " Isto é Python!"
lonxitude = len(texto)
print(lonxitude)

#boletin 7, 2

texto = "Python"

for caracter in texto:
    print(caracter)

#boletin 7, 3

texto = "Python para todos"
texto_invertido = texto[::-1]
print(texto_invertido)

#boletin 7, 4

texto = "Guido Van Rossum creou Python"
sen_espazos = texto.replace(" ", "")
print(sen_espazos)

#boletin 7, 5

texto = "Python Python Python".replace(" ", "")
vocais = "aeiouAEIOU"
num_vocais = 0
num_consoantes = 0

for letra in texto:
    if letra.isalpha():
        if letra in vocais:
            num_vocais += 1
        else:
            num_consoantes += 1

print("Número de vocais:", num_vocais)
print("Número de consoantes:", num_consoantes)

#boletin7, 6

texto = " www.phytonparatodos.com "

parte1 = texto[:12]

parte2 = texto[12:]

resultado = parte1 + parte2

print(parte1)
print(parte2)
print(resultado)

#boletin7, 7

texto = " Phytoneros"

maiusculas = texto.upper()
print(maiusculas)

minusculas = maiusculas.lower()
print(minusculas)

