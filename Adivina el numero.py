import random

intentos = 0
minNumber = 0
maxNumber = 10

username = input("Hola!, Cual es tu nombre?: ")

numero = random.randint(minNumber, maxNumber)
print("Bueno!, {}".format(username), "estoy pensando en numero entre el " + str(minNumber) + " y " + str(maxNumber) + ", puedes adivinar cual es?")

while intentos <6:
    print("adivina: ")
    intento = int(input())
    intentos += 1

    if intento < numero:
        print("Tu numero es demasiado bajo.")
    if intento > numero:
        print("Tu numero es muy alto.")
    if intento == numero:
        break

if intento == numero:
    print("Buen trabajo {}!, ".format(username) + "adivinaste el numero despues de {} ".format(str(intentos)) + "intentos")