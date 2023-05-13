from datetime import timedelta
from datetime import date
from datetime import time
import datetime

momento_actual = datetime.datetime.now()
print("Hora actual:", momento_actual.hour)
print("Mes actual", momento_actual.month)
print("Día actual:", momento_actual.day)

timestamp = momento_actual.timestamp()
print(timestamp)


tiempo_actual = time(19, 30, 0)
print(tiempo_actual.hour)
print(tiempo_actual.minute)
print(tiempo_actual.second)

fecha_actual = date.today()  # Actual
print(fecha_actual.year)
print(fecha_actual.month)
print(fecha_actual.day)

fecha_actual = date(2023, 8, 4)  # Definirlo tú
print(fecha_actual.year)
print(fecha_actual.month)
print(fecha_actual.day)

# Operaciones con dates (timedelta)

inicio_timedelta = timedelta(88, 33, 14, weeks=5)
final_timedelta = timedelta(100, 44, 53, weeks=14)
print(final_timedelta - inicio_timedelta)
print(final_timedelta + inicio_timedelta)
