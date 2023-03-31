### IF, ELIF & ELSE ###

condicion = False

if condicion: ## Es lo mismo que if condicion == True:
    print("Se cumple la condición del primer if")

condicion = 5 * 2

if condicion == 10:
    print("Se cumple la condición del segundo if")

if condicion == 11:
    print("Se cumple la condición del tercer if")

if condicion > 10:
    print("Es mayor que 10")
elif condicion < 10:
    print("Es menor que 10")
else:
    print("Es igual a 10")

if condicion > 10 and condicion < 20:
    print("Es mayor que 10 y menor que 20")
else:
    print("Es menor o igual que 10 o mayor o igual que 20")

condicion = "Cadena de texto"

if condicion:
    print("Mi cadena de texto no es vacía")

if not condicion == "Mi cadena de texto":
    print("Las cadenas de texto son iguales")

