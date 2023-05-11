import datetime

fecha_actual = datetime.datetime.now()
print("Hora actual:", fecha_actual.hour)
print("Mes actual", fecha_actual.month)
print("Día actual:", fecha_actual.day)

timestamp = fecha_actual.timestamp()
print(timestamp)
