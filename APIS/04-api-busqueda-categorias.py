import requests

palabra=input("Ingrese la palabra a buscar: ")
url="https://dummyjson.com/products/search"
respuesta= requests.get(url, params={"q":palabra})
resultados=respuesta.json()['products']

#imprimo los resultados
for item in resultados:
    print(item["title"], "-", item["price"])

#lista de categorias
url_categoria="https://dummyjson.com/products/categories"
respuesta=requests.get(url_categoria)
categorias=respuesta.json()
print (categorias[:5])
for cat in categorias:
    print(cat["name"])

#productos por categoria
url_producto_categorias="https://dummyjson.com/products/category/laptops"
respuesta=requests.get(url_producto_categorias)
productos=respuesta.json()["products"]
print("="*50)
print("LISTA DE PRODUCTOS DE LA CATEGORIA LAPTOPS")

for item in productos:
    print(item["id"], "-->", item["title"])

                       