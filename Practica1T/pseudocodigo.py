import random

n = random.randint(1, 10)
a = 0
b = 0

while b != 20:
    a = a + n
    b = b + 2

print(f"El resultado de dividir {a} entre {b} es: {a/b}")
print(f"El número aleatorio que se ha generado es: {n}")