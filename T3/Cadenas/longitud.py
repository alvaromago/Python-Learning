frase = input("Dame una frase: ")

def len_spaces():
    longitud = len(frase)
    return longitud

def len_no_spaces():
    longitud = len(frase.replace(" ", ""))
    return longitud

print(len_no_spaces())
print(len_spaces())