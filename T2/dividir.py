num1 = int(input("Dame un el dividendo: "))
num2 = int(input("Dame el divisor: "))

def dividir():
    resultado = num1 / num2
    return resultado

print(f"El resultado de dividir {num1} y {num2} es: {dividir()}")