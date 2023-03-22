num1 = int(input("Dime un número: "))
num2 = int(input("Dime otro número: "))
aux = 0
print(f"El primer número vale {num1} y el segundo {num2}")
aux = num1
num1 = num2 
num2 = aux
print(f"Ahora el primer número vale {num1} y el segundo {num2}")