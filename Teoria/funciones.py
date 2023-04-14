# Palabra reservada para definir una función 'def'

def funcion():
    print("Esto es una función")

funcion()

def suma(num1, num2):
    print(num1 + num2)

suma(5,5)

def suma_con_return(num1, num2):
    return num1 + num2

resultado = suma_con_return(3,6)
print(resultado)

def print_nombre(nombre, apellido):
    print(f"{nombre} {apellido}")

print_nombre(apellido = "Martin", nombre = "Alvaro") # Puedes reordenar el orden de los valores

def print_nombre_con_default(nombre, apellido, alias = "Sin alias"): # Puedes definir valores por defecto para un parámetro
    print(f"{nombre} {apellido}, {alias}")

print_nombre_con_default("Alvaro", "Martin")

def print_textos_mayusculas(*textos): # Con el asterisco defines que pueden pasarle de 1 a infintos valores a esa función
    print(type(textos)) # Type = tuple
    for texto in textos:
        print(texto.upper())

print_textos_mayusculas("Hola", "Prueba de Python", "Parámetros infinitos")