a = int(input("Dime un número: "))
b = int(input("Dime otro número: "))

def expo():
    exp = a ** b
    return exp
print(f"El resultado de elevar {a} a {b} es: {expo()}")