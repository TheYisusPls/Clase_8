planetas = {1: "Mercurio", 2: "Venus", 3: "Tierra", 4: "Marte", 5: "Júpiter", 6: "Saturno", 7: "Urano", 8: "Neptuno"}

i = int(input("Dime un numero del 1 al 8 y te dire que planeta es: "))
while i > 8:
    i = int(input("Te dije un numero del 1 al 8 estas tonto?, intenta otra vez: "))

print(planetas[i])















