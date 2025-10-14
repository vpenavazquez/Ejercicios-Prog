#boletin 4, 1

producto = input("dime el nombre del producto")
ventas = int(input("dime las ventas del producto"))

if ventas <= 100:
    tipo = "baixo"

elif ventas <= 500:
    tipo = "medio"

elif ventas <= 1000:
    tipo = "alto"

else:
    tipo = "primera necesidade"

print("el producto " + producto + "es de tipo" + tipo)

#boletin 4, 2

print("Selecciona unha opción para calcular a superficie:")
print("1... Cadrado")
print("2... Triángulo")
print("3... Círculo")


opcion = input("Escribe o número da opción: ")

if opcion == "1":
    lado = float(input("Introduce o lado do cadrado: "))
    superficie = lado * lado
    print("A superficie do cadrado é:", superficie)

elif opcion == "2":
    base = float(input("Introduce a base do triángulo: "))
    altura = float(input("Introduce a altura do triángulo: "))
    superficie = (base * altura) / 2
    print("A superficie do triángulo é:", superficie)

elif opcion == "3":
    radio = float(input("Introduce o radio do círculo: "))
    pi = 3.1416
    superficie = pi * radio * radio
    print("A superficie do círculo é:", superficie)

#boletin 4, 3

numero = float(input("Introduce un número: "))

absoluto = numero if numero >= 0 else -numero

print("O valor absoluto é:", absoluto)

#boletin 4, 4

numero = int(input("pon un numero entre el 0 y el 99"))

if numero >=100:
    print("opcion incorrecta")

else:
    unidades = ["", "un", "dous", "tres", "catro", "cinco", "seis", "sete", "oito", "nove"]
    especiais = ["dez", "once", "doce", "trece", "catorce", "quince", "dezaseis", "dezasete", "dezaoito", "dezanove"]
    decenas = ["", "dez", "vinte", "trinta", "corenta", "cincuenta", "sesenta", "setenta", "oitenta", "noventa"]

if numero < 10:
        texto = unidades[numero]

elif numero < 20:
        texto = especiais[numero - 10]

elif numero % 10 == 0:
        texto = decenas[numero // 10]

else:
        texto = decenas[numero // 10] + " e " + unidades[numero % 10]


print("O número", numero, "é:", texto.capitalize())

#boletin 4, 5

numero = input("Dime os 8 díxitos do teu número de DNI: ")

if len(numero) == 8 and numero.isdigit():

    letras_dni = ['T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F', 'P', 'D', 'X', 'B',
                  'N', 'J', 'Z', 'S', 'Q', 'V', 'H', 'L', 'C', 'K', 'E']

    indice = int(numero) % 23
    letra = letras_dni[indice]

    print("Número válido:", numero + letra)
else:
    print("Número inválido. Debe ter 8 díxitos numéricos.")