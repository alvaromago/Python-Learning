import random

preguntas = [
    "¿Qué país del mundo produce más vino?",
    "¿Cúal es la capital de Canadá?",
    "¿En qué continente se encuentra Tailandia?",
    "Los colores primarios son rojo, amarillo y verde. ¿Verdadero o falso?",
    "¿Cuál es el 'Pais del Sol Naciente'?",
    "¿En qué provincia de España se encuentra el parque temático de Port Aventura?",
    "¿Cuál es la película más taquillera de la historia?",
    "¿Quién ganó el mundial de fútbol en 2014?",
    "¿Cómo se llama el proceso por el cual las plantas se alimentan?",
    "¿Qué elemento de la tabla periódica tiene como símbolo 'He'?"
]
respuestas = [
    "Italia",
    "Ottawa",
    "Asia",
    "Falso",
    "Japón",
    "Tarragona",
    "Avatar",
    "Alemania",
    "Fotosíntesis",
    "Helio"
]
respuesta = ""
aciertos = 0

for i in range (3):
    num_pregunta = random.randint(0, 9)
    respuesta = input(preguntas[num_pregunta] + " ")
    if respuesta.upper() == respuestas[num_pregunta].upper():
        aciertos += 1

print(f"Has acertado un total de {aciertos} preguntas")