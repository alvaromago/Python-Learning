num1 = int(input("Dime un número: "))
num2 = int(input("Dime otro número: "))
# Aseguramos que el primer número sea menor que el segundo número
if num1 > num2:
    num1, num2 = num2, num1
# Calculamos los números pares y los mostramos
print(f"Los números pares entre {num1} y {num2} son:")
for i in range(num1, num2+1):
    if i % 2 == 0:
        print(i)