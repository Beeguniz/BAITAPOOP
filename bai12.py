from bai11 import Point

class PointTest:
    def main(self):
        
        print("Yêu cầu 1:")
        diemA = Point(3,4)
        print(diemA)
        print("----------")

        print("Yêu cầu 2:")
        diemB = Point()
        diemB.read()
        print(diemB)
        print("----------")

        print("Yêu cầu 3:")
        diemC = Point(-diemB.getX(), -diemB.getY())
        print(diemC)
        print("----------")

        print("Yêu cầu 4:")
        print(diemB.distance())
        print("----------")

        print("Yêu cầu 5:")
        print(diemA.distance(diemB))
        print("----------")

PointTest().main()