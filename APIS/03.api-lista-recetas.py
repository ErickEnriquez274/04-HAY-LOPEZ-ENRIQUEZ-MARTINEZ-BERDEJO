import requests


respuesta=requests.get("https://dummyjson.com/recipes")
datos=respuesta.json()

#Imprimir
print(datos['total'])

#IMPRIMIR LA LISTA DE RECETAS
print(datos['recipes'])

#LISTA DE RECETAS CON PARAMETROS
print()

#Georgette Berdejo Salas
