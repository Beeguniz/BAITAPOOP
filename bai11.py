import math

class Point:
    __x = int
    __y = int

    def __init__(self, x=0, y=1):
        self.__x = x
        self.__y = y

    def read(self):
        tmp = input("Nhập vào x, y:")
        self.__x = int(tmp.split()[0])
        self.__y = int(tmp.split()[1])

    def __str__(self):
        return f"({self.__x}, {self.__y})\n"

    def move(self, dx=0, dy=0):
        self.__x = self.__x + dx
        self.__y = self.__y + dy

    def getX(self):
        return self.__x
    def getY(self):
        return self.__y

    def distance(self, *args):
        if len(args)==0:
            return math.sqrt(self.__x**2 + self.__y**2)
        if len(args)==1 and isinstance(args[0], Point):
            return math.sqrt((self.__x-args[0].__x)**2 + (self.__y-args[0].__y)**2)