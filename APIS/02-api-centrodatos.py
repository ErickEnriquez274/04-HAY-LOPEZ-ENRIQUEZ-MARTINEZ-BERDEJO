import requests

idReceta=input("Ingrese el id de la receta: ")
respuesta=requests.get(f"https://dummyjson.com/recipes/{idReceta}")

print(respuesta.status_code) #200
#IMPRIMIR UN DICCIONARIO DE PYTHON CON LA RECETA 1
print(respuesta.json())
receta=respuesta.json()
print("="*50)
print(receta['name'])
print("Ingredientes:")
print(receta['ingredients'])
for item in receta['ingredients']:
    print("-" + item)
print("="*50)
print(receta['rating'])