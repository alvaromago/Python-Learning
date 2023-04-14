# Palabra reservada para definir una función 'class'

class Persona:
    def __init__(self, nombre, apellido): # Constructor de clase
        self.nombre = nombre
        self.apellido = apellido
        self.nombreCompleto = f"{nombre} {apellido}"
    def correr(self):
        print(f"{self.nombreCompleto} está corriendo")

persona = Persona("Alvaro", "Martin")
print(persona.nombreCompleto)
persona.correr()