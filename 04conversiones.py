# crear listas de datos
estudiantes=["Juan", "Pedro", "Luis", "Maria", "Sofía"]

#mostrar un elemento de la lista
print(estudiantes[1]) #pedro
print(estudiantes[4]) #sofia

#agregar un elemento a la lista
estudiantes.append("Ana")
print(estudiantes[5]) #ana

#eliminar un elemento de la lista
estudiantes.remove("Luis")

#mostrar el tamaño de la lista
print(len(estudiantes)) 

#mostrar todos los elementos de la lista
print("Lista de estudiantes:")
for item in estudiantes:
    print(item)