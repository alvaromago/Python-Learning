suma_pares = 0
producto_impares = 1
for i in range(1, 41):
    if i % 2 == 0:
        suma_pares += i
    else:
        producto_impares *= i
print(f"La suma de los veinte primeros números pares es: {suma_pares}")
print(f"El producto de los veinte primero números impares es: {producto_impares}")