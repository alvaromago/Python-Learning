cadenas = []

for i in range (10):
    cadenas.append(input("Introduce una cadena: ")) 

mayor = cadenas[1]

for i in range (10):
    if len(cadenas[i].replace(" ", "")) > len(mayor):
        mayor = cadenas[i]

print(f"La cadena más larga es: {mayor}")