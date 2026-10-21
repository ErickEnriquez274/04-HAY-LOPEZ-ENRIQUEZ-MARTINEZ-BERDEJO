class Animal:
    def __init__(self, nombre):
        self.nombre=nombre

    def hacerSonido(self):
        return f"Hola, soy {self.nombre} y hago un sonido genérico"

class Perro(Animal):
    def hacerSonido(self):
        return f"Hola soy {self.nombre} y hago Guauu!"

class Gallina(Animal):
    def hacerSonido(self):
        return f"Hola soy {self.nombre} y hago Kikiri kii!"

#Instanciar
perrito=Animal("Rocky")
print(perrito.hacerSonido())

#Perrito 2
perrito2=Perro("Bambi")
print(perrito2.hacerSonido())

#Gallina
gallina=Gallina("Karen")
print(gallina.hacerSonido())