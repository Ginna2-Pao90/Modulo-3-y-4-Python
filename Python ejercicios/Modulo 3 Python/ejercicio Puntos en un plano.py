import math


class Puntos:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y =y

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    def devuelve(self, x, y):
        return math.hypot(abs(self.__x - x),abs(self.__y - y))

    def distance(self, Puntos):
        return self.devuelve(Puntos.getx(), Puntos.gety())


Punto1 = Puntos(0, 9)
Punto2 = Puntos(0, 1)
print(Punto1.distance(Punto2))
print(Punto2.devuelve(2, 0))