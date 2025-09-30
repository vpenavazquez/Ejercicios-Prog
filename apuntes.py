nteiros
Coma flotante
complexos

Cadeas de caracteres

Booleanos

Hexadecimal
Octal
Binario

Operadores * / %
Operadores binarios - & / ^
Operadores lóxios "and or not"
Operadores relacionais == != < > <= >=


print("4==6 " + str  )
print(4!=6)
print(4<6)
print(4>6)
print(4>=6)
print(4<=6)


boTempo = True
temp = 24
porcNubes= 30
precipitacion= 2

if temp >16 and porcNubes < 40 and precipitacion == 0:
    print("Collo Toalla")
    print("Poño Bañador")
    print("vou a praia")
else:
    print("Collo chuvasqueiro")
    print("Vou a casa dun amigo/a")

print("Volto a casa")
print("Duchome")
print("Ceo")
print("Cama")

if precipitacion > 0:
    print("Collo paraugas")

if temp < 0:
    print("Vai un frio do carallo")
else:
    if temp > 0 and temp < 10:
        print("Vai moito frio")
    else:
        if temp>10 and temp<20:
            print("esta fresco")
        else:
            if temp>20 and temp<30:
                print("Isto templase)
            else:
                if temp>30 and temp<40:
                    print("Charca")



if temp >15 :
    valoracionAtmosferica= "Calor"
else:
    valoracionAtmosferica= "Frio"

valoracionAtmosferica = "calor" if temp>15 else "Frio"