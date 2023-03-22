num1 = int(input("Dime un número: "))
num2 = int(input("Dime otro número: "))

def suma():
    suma = num1 + num2
    return suma

def resta():
    resta = num1 - num2
    return resta

def division():
    division = num1 / num2
    return division

def multiplicacion():
    multiplicacion = num1 * num2
    return multiplicacion

print(suma())
print(resta())
print(division())
print(multiplicacion())