import json

from pprint import pprint
# Indica los aparcamientos que son cubiertos y al aire libre 
with open('Aparcamientos.json') as data_file:    
    data = json.load(data_file)
for x in data['docs']:
	if x['TIPOLOGIA'] == 'Cubierto':
		print(x['NOMBRE'])
		print(x['TIPOLOGIA'])
	elif x['TIPOLOGIA'] == 'Aire libre':
		print(x['NOMBRE'])
		print(x['TIPOLOGIA'])
