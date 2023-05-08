# Un set no es una estructura ordenada
# Un set no admite repetidos

set1 = set()
set2 = {}

print(type(set2)) # type = dict
set2 = {"Álvaro", "Martín", 21}
print(type(set2)) # type = set

set2.add("España")
print(set2)

print("Martín" in set2) # ¿Existe 'Martín' en el set? true
print("Hola" in set2) # ¿Existe 'Hola' en el set? false

set2.remove("España") # Eliminar del set
print(set2)

set2.clear() # Vaciar todo el set
print(set2)

set1 = {"Álvaro", "Martín", 21}
set2 = {"Java", "Python", "JavaScript"}
set3 = set1.union(set2) # Unir sets
print(set3)
print(set3.union({"HTML, CSS"})) # También puedes unirlos sin el uso de una variable

print(set3.difference(set1)) # Muestra los datos que tiene una en diferencia con la otra