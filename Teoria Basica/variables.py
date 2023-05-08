# Los nombres de las variables solo admiten minúsculas y _ 
# No admiten -, @, $, ni empezar por números

variable_string = "Variable String"
print(variable_string)

variable_int = 5
print(variable_int)

variable_float = 2.5
print(variable_float)

variable_boolean = True
print(variable_boolean)

# Convertir int to String
variable_int_to_string = str(variable_int)

# Concatenación de variables en un print
print(variable_string, variable_int, variable_boolean)
print("El valor de mi variable String es:", variable_string, ". El valor de mi variable int es:", variable_int)

# Función .length
print(len(variable_string))

# Ejemplo input
nombre = input("¿Cómo te llamas? ")
edad = input("¿Cuántos años tienes? ")
print(nombre, edad)