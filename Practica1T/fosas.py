fosas = ["Calipso", "Marianas", "Puerto Rico", "Aleutianas"]
profundidades = [5270, 11034, 8800, 7822]
mayor_profundidad = max(profundidades)
mayor_fosa = 0

for i in range (1, len(profundidades)):
    if mayor_profundidad == profundidades[i]:
        mayor_fosa = i

print(f"La mayor fosa es {fosas[mayor_fosa]} con una profundidad de {mayor_profundidad} metros")