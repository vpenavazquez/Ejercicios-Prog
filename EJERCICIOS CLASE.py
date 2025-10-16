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

#ahorcado jojos

import random

palabras = ["jotaro kujo", "star platinum", "dio brando", "the world", "joseph joestar", "hermit purple", "josuke higashikata", "crazy diamond", "okuyasu nijimura", "the hand", "koichi hirose", "echoes", "rohan kishibe", "heaven’s door", "giorno giovanna", "gold experience", "bruno bucciarati", "sticky fingers", "narancia ghirga", "aerosmith", "guido mista", "sex pistols", "leone abbacchio", "moody blues", "trish una", "spice girl", "jolyne cujoh", "stone free", "enrico pucci", "made in heaven", "weather report", "foo fighters", "johnny joestar", "tusk", "gyro zeppeli", "yoshikage kira", "killer queen", "caesar zeppeli", "lisa lisa", "hol horse", "lucy steel", "hot pants", "diego brando", "scary monsters", "sandman", "in a silent way", "pocoloco", "hey ya!", "valentine", "dirty deeds done dirt cheap", "mountain tim", "oh! lonesome me", "josuke higashikata (jojolion)", "soft & wet", "yasuho hirose", "paisley park", "jobin higashikata", "speed king", "tooru", "wonder of u", "norisuke higashikata iv", "king nothing", "rai muromuzé", "born this way"]

palabra = random.choice(palabras)
letras_adivinadas = [letra if letra == " " else "_" for letra in palabra]
intentos = 10

print("Estas jugando al ahorcado de JoJo's")

while intentos > 0:
    print("Palabra:", " ".join(letras_adivinadas))

    if "".join(letras_adivinadas) == palabra:
        print("¡Buena! Adivinaste de una:", palabra)
        break

    intento = input("Adivina una letra: ").lower()

    if intento in palabra:
        print("¡Lesgoo, bien hecho!")
        for i in range(len(palabra)):
            if palabra[i] == intento:
                letras_adivinadas[i] = intento
    else:
        print("MAL.")
        intentos -= 1
        print("Te quedan", intentos, "intentos.")

if intentos == 0:
    print("CAGASTE, la palabra era:", palabra)