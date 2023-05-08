# Palabra reservada para definir una función 'class'

class Persona:
    def __init__(self, nombre, apellido): # Constructor de clase
        self.nombreCompleto = f"{nombre} {apellido}" # public nombreCompleto
        self.__nombre = nombre # private nombre

    def get_nombre(self):
        return self.__nombre

    def correr(self):
        print(f"{self.nombreCompleto} está corriendo")

persona = Persona("Alvaro", "Martin")
print(persona.nombreCompleto)
persona.correr()