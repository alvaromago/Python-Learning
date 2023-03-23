numeros = []
for i in range(10):
    numeros.append(int(input("Ingrese un número: ")))

media = sum(numeros) / len(numeros)
maximo = max(numeros)
minimo = min(numeros)

print(f"La media es: {media}")
print(f"El máximo es: {maximo}")
print(f"El mínimo es: {minimo}")