numeros = []
for i in range(10):
    numeros.append(int(input("Ingrese un número: ")))

# Calcular el máximo y su posición
maximo = max(numeros)
indices = [i for i, num in enumerate(numeros) if num == maximo] # ¿Como funciona esta línea?

print(f"El valor máximo es {maximo} y aparece en la(s) posición(es): {indices}")