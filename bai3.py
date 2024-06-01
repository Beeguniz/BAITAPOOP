from bai11 import Point
class ColorPoint(Point):

    def __init__(self, x=0, y=1, color="xanh"):
        super().__init__(x, y)
        self.__color = color

    def __init__(self):
        super().__init__()
        self.__color = "xanh"

    def __init__(self, x, y, color):
        super().__init__(x, y)
        self.__color = color

    def __init__(self, cp):
        super().__init__(cp.getX(), cp.getY())
        self.__color = cp.getColor()

    def read(self):
        super().read()
        self.__color = input().strip()

    def print(self):
        super().print()
        print(f": {self.__color}")

    def setColor(self, color):
        self.__color = color

    def getColor(self):
        return self.__color

class C002454:
    @staticmethod
    def testCase1():
        A = ColorPoint(5, 10, "trắng")
        A.print()

    @staticmethod
    def testCase2():
        B = ColorPoint()
        B.read()
        B.move(10, 8)
        B.print()

    @staticmethod
    def testCase3():
        C = ColorPoint(6, 3, "đen")
        D = ColorPoint(C)
        D.print()
        D.setColor("vàng")
        D.print()

    @staticmethod
    def main():
        C002454.testCase1()
        C002454.testCase2()
        C002454.testCase3()


if __name__ == "__main__":
    C002454.main()
