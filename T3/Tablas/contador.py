num = None
positivos = []
negativos = []
while num != 0:
    num = int(input("Dime un número: "))
    if num > 0:
        positivos.append(num)
    elif num < 0:
        negativos.append(num)
print(f"Has escrito {len(positivos)} números positivos y {len(negativos)} números negativos")