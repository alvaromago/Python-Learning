## Manejo de Errores ##

num1 = 5
num2 = "1"

# try except

try:
    print(num1 + num2)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")

# try except else

try:
    print(num1 + num2)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")
else: # Solo se ejecuta si no hay error
    print("La ejecución continúa correctamente")

# try except finally

try:
    print(num1 + num2)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")
finally: # Haya error o no, este bloque se ejecutará
    print("La ejecución continúa")

# Excepciones por tipo

try:
    print(num1 + num2)
    print("No se ha producido un error")
except TypeError: # Se ejecuta solo si es TypeError
    print("Se ha producido un TypeError")

# Captura de la información de la excepción

try:
    print(num1 + num2)
    print("No se ha producido un error")
except ValueError as error:
    print(error)
except Exception as error: # Se ejecuta solo si es TypeError
    print(error)