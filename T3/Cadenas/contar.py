cadena = input("Introduzca una cadena: ")
num_letras = 0
num_digitos = 0

for caracter in cadena.replace(" ", ""):
    if caracter.isalpha():
        num_letras += 1
    elif caracter.isdigit():
        num_digitos += 1

print(f"La cadena '{cadena}' contiene {num_letras} letras y {num_digitos} dígitos")