import requests

#Eliminar un productor
producto_eliminado={
    "id": 3
}

url= "https://dummyjson.com/products/3"
respuesta=requests.delete(url)
print(respuesta.status_code) #debe de ser 200 para que sea exitoso
print(respuesta.json())
