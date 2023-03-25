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