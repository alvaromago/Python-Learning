age = int(input("Dime tu edad: "))

def segundos_vividos():
    segundos = age * 365.25 * 24 * 60 * 60
    return segundos

print(f"Has vivido aproximadamente {segundos_vividos()} segundos")