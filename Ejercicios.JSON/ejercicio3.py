import json
#Cuales son los aparcamientos que estan en el media mark junto con su geocodigo y cordenadas
from pprint import pprint

with open('Aparcamientos.json') as data_file:    
    data = json.load(data_file)
for x in data['docs']:
	if x['NOMBRE'] == 'Media Markt_1':
		print(x['NOMBRE'])
		print(x['TIPOLOGIA'])
		print(x['GEOCODIGO'])
		print(x['GRAD_X'])
		print(x['GRAD_Y'])
	elif x['NOMBRE'] == 'Media Markt_2':
		print(x['NOMBRE'])
		print(x['TIPOLOGIA'])
		print(x['GEOCODIGO'])
		print(x['GRAD_X'])
		print(x['GRAD_Y'])
