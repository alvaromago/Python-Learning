import random
num = int(random.randint(1, 50))
intentos = 0
guess = int(input("Prueba un número: "))
while guess != num:
    if guess < num:
        guess = int(input("El número es mayor, prueba con otro número: "))
        intentos += 1
    elif guess > num:
        guess = int(input("El número es menor, prueba con otro número: "))
        intentos += 1
print(f"¡Has acertado! Intentos: {intentos}")