# -*- coding: utf -8 -*-
from lxml import etree
doc = etree.parse('provinciasypoblaciones.xml')
# Obtenemos una lista donde cada elemento es una provincia
municipios=doc.findall("provincia/localidades/localidad")
for localidad in municipios:
	print (localidad.text)