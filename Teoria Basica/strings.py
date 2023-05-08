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
print(f"Mi nombre es {name} {surname} y tengo {age} años")
# Desempaquetado de caracteres
language = "Python"
a, b, c, d, e, f = language
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

# División
language_slice = language[1:4]
print(language_slice)
language_slice = language[2:]
print(language_slice)
language_slice = language[:3]
print(language_slice)
language_slice = language[-3]
print(language_slice)
reverse_language = language[::-1] # Reverse
print(reverse_language)

# Funciones
print(language.upper())
print(language.lower())
print(language.count("t"))
print(language.isnumeric())
print(language.upper().isupper())
print(language.startswith("Py"))