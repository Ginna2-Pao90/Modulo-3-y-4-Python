from datetime import datetime
dato = datetime(2022,11,2,17,50)
print(dato.strftime("%Y/%m/%d %H:%M:%S"))
print(dato.strftime("%y/%B/%d %H:%M:%S %p"))
print(dato.strftime("%a/%Y/%b %d"))
print(dato.strftime("%A/%Y/%B %d"))
print(dato.strftime("Dia de la semana: %w"))
print(dato.strftime("Dia del año: %j"))
print(dato.strftime("Número de semana en el año: %W"))