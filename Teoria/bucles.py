### WHILE, FOR & DO WHILE ###

condicion = 0

while condicion < 10:
    print(condicion)
    condicion += 2
else: # A un While se le puede meter un Else
    print("La condicion es mayor o igual a 10")

while condicion < 15:
    condicion += 2
    if condicion == 13:
        print("La condicion vale 13")
        break

list1 = [21, 30, 23, 24, 25, 24, 28] # Lista

for numero in list1:
    print(numero)

tuple1 = (21, 30, 24, 23, 24, 28) # Tupla

for numero in tuple1:
    print(numero)

set1 = {"Álvaro", "Martín", 21} # Set

for elemento in set1:
    print(elemento)

dict1 = {"Nombre":"Álvaro", "Apellido":"Martín", "Edad":21, 1:1.80} # Diccionario (imprime keys no values)

for elemento in dict1: # Devuelve keys
    print(elemento)

for elemento in dict1.values(): # Devuelve values
    print(elemento)