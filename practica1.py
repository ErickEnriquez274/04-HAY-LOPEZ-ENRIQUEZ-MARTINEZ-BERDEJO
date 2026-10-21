# Pilares de la POO: Herencia, Polimorfismo, Encapsulamiento, Abstracción.
class Persona: 
    # Constructor
    def __init__(self, nombre, edad):
        self.nombre=nombre   #atributo nombre
        self.edad=edad       #atributo edad

    #Metodo para mostrar la información
    def saludar(self):
        return f"Hola, mi nombre es {self.nombre} y tengo {self.edad} "

#Crear un objeto (INSTANCIA) de clase Persona (INSTANSACIÓN)
#Nombre del objeto= constructor de la clase
persona1= Persona("Juan", 20)
persona2= Persona("Maria", 19)

#Llamar al metodo del objeto e imprimimos el resultado
print(persona1.saludar())
print(persona2.saludar())