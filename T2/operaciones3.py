num1 = int(input("Dime un número: "))
num2 = int(input("Dime otro número: "))
num3 = int(input("Dime un último número: "))

def suma():
    suma = num1 + num2 + num3
    return suma

def multiplicacion():
    multiplicacion = num1 * num2 * num3
    return multiplicacion

def media():
    media = (num1 + num2 + num3) / 3
    return media

print(suma())
print(multiplicacion())
print(media())