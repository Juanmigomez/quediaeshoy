#!/usr/bin/python
import locale
from datetime import datetime, date
import urllib2
from xml.dom import minidom

# Configuramos el locale a espanol
locale.setlocale(locale.LC_TIME, "es_ES.utf8")

# Asignamos a hoy la fecha actual
hoy = date.today()

# La imprimimos con formato
print(hoy.strftime("Hola,\nhoy es %A %d de %B de %Y"))

# TODO: Incorporar el santoral e imprimir el/los santos del dia
#		Leeremos el santo de la web 
#		http://es.catholic.net/rss/santoral.xml
#		Que nos devuelve un XML con los santos del dia
strXML = urllib2.urlopen("http://es.catholic.net/rss/santoral.xml").read()
# print strXML
docXML = minidom.parseString(strXML)
items = docXML.getElementsByTagName("item")
print ("\nSantoral, hoy se celebra:")
for item in items:
	nombre = item.getElementsByTagName("title")[0]
	print ("\t" + nombre.firstChild.data)
