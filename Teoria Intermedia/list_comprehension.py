lista_original = [21, 30, 23, 24, 25, 24, 28]
print(lista_original)

rango = range(9)
print(list(rango))

list1 = [i for i in range(9)]
print(list1)

list1 = [i + 2 for i in range(9)]
print(list1)

list1 = [i * 2 for i in range(9)]
print(list1)

list1 = [i * i for i in range(9)]
print(list1)


def suma_cinco(num):  # Definimos función
    return num + 5


# Llamamos a la función para hacer el bucle
list1 = [suma_cinco(i) for i in range(9)]
print(list1)
