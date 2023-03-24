cadena = input("Introduzca una cadena: ")

def contar_vocales():
    vocales = "aeiouAEIOU"  # Definimos un string con todas las vocales
    num_vocales = 0  # Inicializamos un contador de vocales a cero
    for letra in cadena:
        if letra in vocales:
            num_vocales += 1
    return num_vocales

num_vocales = contar_vocales()

print(f"La cadena '{cadena}' contiene {num_vocales} vocales")