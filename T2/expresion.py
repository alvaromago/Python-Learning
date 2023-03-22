a = int(input("Dame el valor de a: "))
b = int(input("Dame el valor de b: "))
c = int(input("Dame el valor de c: "))

def ecuacion():
    resultado = ((b**2) - (4*a*c)) / (2*a)
    return resultado
print(ecuacion())