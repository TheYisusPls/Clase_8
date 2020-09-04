lista = []
condicion = ()
fin = "fin"
while condicion != fin:

    condicion = input("Dime numeros al azar: ")
    if condicion == fin:
        break
    lista.append(int(condicion))

print(lista)

suma = 0

for numero in lista:
    suma = suma + numero
print(suma)
