import requests

# ---------- BÚSQUEDA POR PALABRA ----------
palabra = input("Ingrese la palabra a buscar: ")
url = "https://dummyjson.com/products/search"
respuesta = requests.get(url, params={"q": palabra})
resultados = respuesta.json()['products']

# Imprimo los resultados
print("RESULTADOS DE BUSQUEDA:")
for item in resultados:
    print(item["title"], "-", item["price"])

# ---------- LISTA DE CATEGORIAS ----------
url_categoria = "https://dummyjson.com/products/categories"
respuesta = requests.get(url_categoria)
categorias = respuesta.json()

print("")
print("CATEGORIAS DISPONIBLES:")

# Loop simple para mostrar las categorias con un numero
contador = 1
for cat in categorias:
    print(contador, "-", cat["name"])
    contador = contador + 1

# ---------- ELEGIR UNA CATEGORIA ----------
opcion = input("Elige el numero de la categoria: ")
opcion = int(opcion)

# Saco la categoria elegida usando el numero
posicion = opcion - 1
categoria_elegida = categorias[posicion]
slug = categoria_elegida["slug"]
nombre = categoria_elegida["name"]

# ---------- PRODUCTOS DE LA CATEGORIA ELEGIDA ----------
url_producto_categorias = "https://dummyjson.com/products/category/" + slug
respuesta = requests.get(url_producto_categorias)
productos = respuesta.json()["products"]

print("==================================================")
print("PRODUCTOS DE LA CATEGORIA:", nombre)
print("==================================================")

for item in productos:
    print(item["id"], "-->", item["title"])