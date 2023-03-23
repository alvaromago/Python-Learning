pares = []
for i in range (1, 41):
    if i % 2 == 0:
        pares.append(i)
pares.reverse()
for i in range (1, len(pares)):
    print(pares[i])