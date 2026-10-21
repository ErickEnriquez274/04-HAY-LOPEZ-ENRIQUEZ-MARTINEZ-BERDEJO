datos_jugador = {
    "nombre": "Rafa Márquez",
    "club": "Atlas",
    "posicion": "Defensa",
    "sueldo": 1000000,
    "nacionalidad": "Mexicano"
}

datos_jugador["total_goles"] = 150

print("=" * 30)
print("Nombre del jugador: " + datos_jugador["nombre"])
print("Club: " + datos_jugador["club"])
print("Nacionalidad: " + datos_jugador["nacionalidad"])
print("=" * 30)

print("\nDatos del jugador:")
for clave, valor in datos_jugador.items():
    print(clave + ": " + str(valor))