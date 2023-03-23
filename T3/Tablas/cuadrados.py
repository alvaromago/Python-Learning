num = int(input("Dame un número: "))
cuadrados = []
for i in range (num+1, num+10):
    num += 1
    cuadrados.append(i * i)
print(cuadrados)