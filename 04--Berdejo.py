with open("nombres.txt", "w") as archivo:

    for i in range(1, 6):
        nombre = input(f"Ingrese el nombre {i}: ")
        archivo.write(nombre + "\n")