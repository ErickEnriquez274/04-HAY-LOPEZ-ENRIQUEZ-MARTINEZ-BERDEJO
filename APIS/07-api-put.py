import requests

#Actualizar un productor
producto_modificado={
    "price": 123.80
}

url= "https://dummyjson.com/products/1"
respuesta=requests.put(url, json=producto_modificado)
print(respuesta.status_code) #debe de ser 200 para que sea exitoso
print(respuesta.json())
