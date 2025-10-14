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

