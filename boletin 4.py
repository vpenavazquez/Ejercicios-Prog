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



