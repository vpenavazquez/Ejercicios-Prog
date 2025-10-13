#GENERADOR DE CONTRASEÑAS

import random

def xeradorContrasinais(n):
    l = ['1234567890', 'abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', '!@#$%^&*()_+-=[]{};:,.<>/?']
    i=0
    contrasinal=''
    while i<n:
        tipo = random.randint(0,3)
        iSim = random.randint(0,len(l[tipo])-1)
        contrasinal = contrasinal + l[tipo][iSim]
        i+=1
    return contrasinal
while True:
    n = int(input("Introduce un numero para xerar a lonxitude do contrasinal"))
    if n >= 6 and n <=12:
        print(xeradorContrasinais(n))
    elif n ==0:
        break

    else:
        print("a lonxitude valida es entre 6 e 12")

#COMPROBACION FORMATO FECHA

fecha = input("Dime una fecha formato (dd/mm/aaaa): ")
formato_valido = ( len(fecha) == 10 and
                   fecha[2] == "/" and
                   fecha[5] == "/" and " " not in fecha and
                   fecha.replace("/", "").isdigit() )

if formato_valido:
    print("Formato correcto")
else:
    print("Formato incorrecto")

#eliminacion de espacios al principio y fin

frase = " unha cadea calquera "

inicio = 0
while inicio < len(frase) and frase[inicio] == " ":
    inicio += 1

fin = len(frase) - 1
while fin >= 0 and frase[fin] == " ":
    fin -= 1

espacios= frase[inicio:fin+1]
print(espacios)
