import os
directorio=os.path.dirname(os.path.abspath(__file__))
ruta_documento=os.path.join(directorio, "lista_estudiantes_reprobados.txt")


#PARA LEER TODO EL ARCHIVO
with open ("lista-estudiantes_reprobados.txt", "r") as lista:
    contenido=lista.read()
    print(contenido)

archivo_aprobados=os.path.join(directorio)