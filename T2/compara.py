num1 = int(input("Dime un número: "))
num2 = int(input("Dime otro número: "))

if num1>num2:
    print(f"{num1} es mayor que {num2}")
elif num1<num2:
    print(f"{num2} es mayor que {num1}")
else:
    print(f"{num1} y {num2} son iguales")