### Strings ###

string1 = "Mi String"
print(len(string1))

# Introduciendo \n en un String hacemos un salto de línea
string_linea = "Este es un String\ncon salto de línea"
print(string_linea)

# Introduciendo \t en un String lo indentamos
string_tab = "\tEste es un String tabulado"
print(string_tab)

# Formateo
name, surname, age = "Fernando", "Alonso", 14

## Para formatear Strings utiliza %s
## Para formatear Integers utiliza %d
## Para formatea Floats utiliza %f
print("Mi nombre es %s %s y tengo %d años" %(name, surname, age))

## Si utilizas .format entonces utiliza {}
print("Mi nombre es {} {} y tengo {} años".format(name, surname, age))
