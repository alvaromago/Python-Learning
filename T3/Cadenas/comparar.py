palabra1 = input("Ingrese la primera palabra: ")
palabra2 = input("Ingrese la segunda palabra: ")

def mayor_alfabeticamente():
    if palabra1 > palabra2:
        print(f"La palabra {palabra1} es mayor alfabéticamente que la palabra {palabra2}")
    elif palabra2 > palabra1:
        print(f"La palabra {palabra2} es mayor alfabéticamente que la palabra {palabra1}")
    else:
        print("Ambas palabras son iguales alfabéticamente")

mayor_alfabeticamente()