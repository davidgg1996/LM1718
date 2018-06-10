import json

from pprint import pprint
#Cuales son los aparcamientos que estan en el centro comercial junto con su cordenadas y geocodigo.
with open('Aparcamientos.json') as data_file:    
    data = json.load(data_file)
for x in data['docs']:
	if x['NOMBRE'] == 'Centro Comercial Santa Cruz_1':
		print(x['NOMBRE'])
		print(x['GEOCODIGO'])
		print(x['GRAD_X'])
		print(x['GRAD_Y'])
	elif x['NOMBRE'] == 'Centro Comercial Santa Cruz_2':
		print(x['NOMBRE'])
		print(x['GEOCODIGO'])
		print(x['GRAD_X'])
		print(x['GRAD_Y'])
	elif x['NOMBRE'] == 'Centro Comercial La Ola':
		print(x['NOMBRE'])
		print(x['GEOCODIGO'])
		print(x['GRAD_X'])
		print(x['GRAD_Y'])
	elif x['NOMBRE'] == 'Centro Comercial Webhe':
		print(x['NOMBRE'])
		print(x['GEOCODIGO'])
		print(x['GRAD_X'])
		print(x['GRAD_Y'])
	elif x['NOMBRE'] == 'Centro Comercial Tres de Mayo':
		print(x['NOMBRE'])
		print(x['GEOCODIGO'])
		print(x['GRAD_X'])
		print(x['GRAD_Y'])
