frase = input("Dame una frase: ")
carac = input("Dame un carácter: ")
posicion = frase.replace(" ", "").find(carac)
if posicion == -1:
    print("El carácter no se encuentra en la frase")
else:
    print(f"El carácter aparece por primera vez en la posición {posicion}")