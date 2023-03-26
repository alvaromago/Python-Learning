lista = []

for i in range (10):
    lista.append(input("Introduce un número: "))

for i in range(len(lista)):
    # Encontramos el índice del número mayor en el subconjunto no ordenado
    indice_mayor = i
    for j in range(i+1, len(lista)):
        if lista[j] > lista[indice_mayor]:
            indice_mayor = j
    
    # Intercambiamos el número en la posición actual con el número en el índice del número mayor
    lista[i], lista[indice_mayor] = lista[indice_mayor], lista[i]

print(f"Lista ordenada de mayor a menor: {lista}")
