"""
Ejercicio3 – POO
Vamos a crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construye los
siguientes métodos para la clase:
 Un constructor, donde los datos pueden estar vacíos.
 Los setters y getters para cada uno de los atributos. Hay que validar las entradas de datos.
 mostrar(): Muestra los datos de la persona.
 esMayorDeEdad(): Devuelve un valor lógico indicando si es mayor de edad.,
"""

class Persona:
    def __init__(self, nombre=None, edad=None, dni=None):
        self.nombre=nombre
        if edad is not None and edad<0:
            self.edad=0

        self.dni=dni

    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre

    def getEdad(self):
        return self.edad

    def setEdad(self, edad):
        if edad>0:
            self.edad = edad
        else:
            edad=0

    def getDni(self):
        return self.dni

    def setDni(self, dni):
        self.dni = dni

    def mostrar(self):
        print("La persona se llama "+self.nombre+", tiene "+str(self.edad)+" años, y su DNI es: "+self.dni)

    def esMayorDeEdad(self):
        if self.edad>=18:
            return True
        else:
            return False





p=Persona("Antonio",-5,"76912255C")
p.mostrar()
print(p.esMayorDeEdad())
