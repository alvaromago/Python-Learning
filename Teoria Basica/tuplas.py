# Las tuplas son inmutables
# Una vez se definen no se pueden modficar

tuple1 = tuple()
tuple2 = ()

tuple1 = (21, 1.80, "Álvaro", "Martín")
print(tuple1) # type = tuple
print(tuple1[0])
print(tuple1[-2]) # Empezando por atrás
print(tuple1.index("Martín")) # Índice que tiene ese contenido

tuple2 = (21, 30, 24, 23, 24, 28)
print(tuple1 + tuple2) # Se pueden concatenar tuplas

