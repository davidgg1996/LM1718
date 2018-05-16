import json
# No llego a solucionarlo entero.
#Aparcamientos que estan cubiertos en el centro de deportes .
from pprint import pprint

with open('Aparcamientos.json') as data_file:    
    data = json.load(data_file)
for x in data['docs']:
	if x['TIPOLOGIA'] == 'Cubierto':
		print(x['NOMBRE'])
	elif x['TIPOLOGIA'] == 'Pabellón de deportes':
		print(x['NOMBRE'])
		print(x['TIPOLOGIA'])



		
