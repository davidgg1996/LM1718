import json

from pprint import pprint
#indica los aparcamientos no cubiertos con sus nombres .
with open('Aparcamientos.json') as data_file:    
    data = json.load(data_file)
for x in data['docs']:
	if x['TIPOLOGIA'] == 'Aire libre':
		print(x['NOMBRE'])
		print(x['TIPOLOGIA'])
