# Un diccionario es una relacion clave-valor

dict1 = dict()
dict2 = {}

dict2 = {"Nombre":"Álvaro", "Apellido":"Martín", "Edad":21, 1:1.80}
dict1 = {"Nombre":"Álvaro", "Apellido":"Martín", "Edad":21, "Lenguajes": {"Java", "Python", "JavaScript"}}
print(dict2)
print(dict1)

print(dict2["Nombre"]) # Solo imprime el valor

dict2["Nombre"] = "Antonio"
print(dict2["Nombre"])

dict1["Alias"] = "AlvaroMago"
print(dict1)

del dict1["Alias"]
print(dict1)

print("Álvaro" in dict1) # false
print("Nombre" in dict1) # true (busca por clave no por valor)

print(dict1.items()) # Muestra las claves y valores unidos en formato lista
print(dict1.keys()) # Muestra las claves en formato lista
print(dict1.values()) # Muestra los valores en formato lista

dict3 = dict.fromkeys(("Nombre", "Edad")) # Esta función crea un diccionario vacio con las claves que tu le introduzcas
print(dict3)