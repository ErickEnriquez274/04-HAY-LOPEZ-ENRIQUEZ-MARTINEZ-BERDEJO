import requests

nuevo_producto={
    "title": "Audífonos LITIID",
    "price": 123.45
    "category": "electronics"
}
url= "https://dummyjson.com/products/add"
respuesta=requests.post(url, json=nuevo_producto)
print(f"codigo de respuesta") #debe de ser 201 para que sea exitoso
print(respuesta.json()) #debe incluir la ID que se le asigno