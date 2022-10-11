
# constructor
class Animal:
    def __init__(self, nombre, color, edad):
        self.nombre = nombre
        self.color = color
        self.edad = edad

    def suFrase():
        pass


class Perro(Animal):
    def __init__(self, nombre, color, edad, tamanio):
        super().__init__(nombre, color, edad)
        self.tamanio = tamanio
        self.salioApasear = True

    def suFrase(self):
        print("¡Dejenme entrar al edificio!")


# super para hacer herencia
class Gato(Animal):
    def __init__(self, nombre, color, edad):
        super().__init__(nombre, color, edad)
        self.tieneHambre = True

    def suFrase(self):
        print("Miau, tengo hambre!")


gato1 = Gato("Kiro", "amarillo", 9)
gato2 = Gato("Neri", "negro", 9)
perro1 = Perro("Aquiles", "chocolate", 5, "grande")

gato1.suFrase()
perro1.suFrase()
