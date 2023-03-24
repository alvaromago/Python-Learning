cad1 = input("Introduce una cadena: ")
cad2 = "" 

for i in range(len(cad1)):
    if i == 0 or cad1[i] != cad1[i-1]:   # Si la letra actual es diferente a la anterior, la agregamos a cad2
        cad2 += cad1[i]
    else:   # Si la letra actual es igual a la anterior, la reemplazamos por un *
        cad2 += "*"

print(f"La cadena resultante es: {cad2}")
