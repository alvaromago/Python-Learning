carac = input("Introduzca un carácter: ")
if len(carac) != 1:
    print("Error. Has escrito más de un carácter.")
elif carac.isdigit():
    print(f"Tu carácter {carac} es un número")
elif carac.isupper():
    print(f"Tu carácter {carac} es una masyúscula")
elif carac.islower():
    print(f"Tu carácter {carac} es una minúscula")
else:
    print(f"Tu carácter {carac} es un símbolo")