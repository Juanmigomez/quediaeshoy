#!/usr/bin/python
import locale
from datetime import datetime, date

# Configuramos el locale a espanol
locale.setlocale(locale.LC_TIME, "es_ES.utf8")

# Asignamos a hoy la fecha actual
hoy = date.today()

# La imprimimos con formato
print(hoy.strftime("Hola, hoy es %A %d de %B de %Y"))

# TODO: Incorporar el santoral e imprimir el/los santos del dia

