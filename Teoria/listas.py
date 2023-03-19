list1 = list()
list2 = []

list1 = [21, 30, 23, 24, 25, 24, 28]
print(list1)
print(len(list1))

list2 = [21, 1.80, "Álvaro", "Martín"] # type = list
print(list2[0])
print(list2[-2]) # Empezando por atrás

age, height, name, surname = list2
print(surname)
print(list1 + list2) # Se pueden concatenar listas

list2.append("España") # Añadir elemento al final de la lista (.append)
print(list2)

list2.insert(4, "Rojo") # Añadir elemento en índice específico (.insert)
print(list2)

list2[4] = "Naranja" # Cambiar contenido de índice específico
print(list2)

del list1[1] # Eliminar índice sin guardar su contenido (del)
print(list1)

print(list1.pop(4)) # Eliminar índice de la lista, último por defecto, guardando el contenido que tenía (.pop)
print(list1)

list2.remove("España") # Eliminar contenido específico de la lista (.remove)
print(list2)

list1.clear() # Borra lista (.clear)
print(list1)