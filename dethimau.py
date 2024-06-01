import json
import pickle

class TuLanh:

    def __init__(self,*args):
        if len(args)==0:
            self.__nhanhieu = 'Elextrolux'
            self.__maso = 'UNKNOWN'
            self.__nuocsx = 'Việt Nam'
            self.__tkdien = True
            self.__dungtich = 256
            self.__gia = 7000000
        if len(args)==6:
            self.__nhanhieu = args[0]
            self.__maso = args[1]
            self.__nuocsx = args[2]
            self.__tkdien = args[3]
            self.__dungtich = args[4]
            self.__gia = args[5]
        if len(args)==1:
            self.__nhanhieu = args[0].__nhanhieu
            self.__maso = args[0].__maso
            self.__nuocsx = args[0].__nuocsx
            self.__tkdien = args[0].__tkdien
            self.__dungtich = args[0].__dungtich
            self.__gia = args[0].__gia

    def makeCopy(self,tl):
            self.__nhanhieu = tl.__nhanhieu
            self.__maso = tl.__maso
            self.__nuocsx = tl.__nuocsx
            self.__tkdien = tl.__tkdien
            self.__dungtich = tl.__dungtich
            self.__gia = tl.__gia

    def nhapThongTin(self):
            self.__nhanhieu = input("Nhập nhãn hiệu: ")
            self.__maso = input("Nhập mã số: ")
            self.__nuocsx = input("Nhập nước sx: ")
            self.__tkdien = input("Nhập tk điện: ")
            self.__dungtich = int(input("Nhập dung tích: "))
            self.__gia = int(input("Nhập giá: "))
    
    def hienThi(self):
        print("====================")
        print(f"Nhãn hiệu: {self.__nhanhieu}")
        print(f"Mã số: {self.__maso}")
        print(f"Nước sx: {self.__nuocsx}")
        print(f"Tk điện: {self.__tkdien}")
        print(f"Dung tích: {self.__dungtich}")
        print(f"Giá: {self.__gia}")

    def layNhanHieu(self):
        return self.__nhanhieu

    def layGia(self):
        return self.__gia    
    
    def soNguoiSD(self):
        return int(self.__dungtich/100)

    def cungNhanHieu(self,tl):
        return self.__nhanhieu == tl.__nhanhieu

    def nhHon(self,tl):
        return self.__dungtich < tl.__dungtich


class C002454:
    def testCase1():
        tl1 = TuLanh()
        tl1.nhapThongTin()
        tl2 = TuLanh('LG','LG-28382', 'Hàn Quốc', True, 600, 43000000)
        tl3 = TuLanh(tl1)
        # tl3 = TuLanh()
        # tl3.makeCopy(tl1)
        tl1.hienThi()
        tl2.hienThi()
        tl3.hienThi()

    def testCase2():

        n = int(input("Nhập số tủ lạnh: "))
        danhsach = []
        for i in range(n):
            tl = TuLanh()
            tl.nhapThongTin()
            danhsach.append(tl)
        
        for s in danhsach:
            s.hienThi()

        danhsach.reverse()
        for s in danhsach:
            s.hienThi()

    def testCase3():
        n = int(input("Nhập số tủ lạnh: "))
        danhsach = []
        for i in range(n):
            tl = TuLanh()
            tl.nhapThongTin()
            danhsach.append(tl)
        
        for s in danhsach:
            s.hienThi()

        danhsach.sort(key = lambda x: x.layGia())

        for s in danhsach:
            s.hienThi()

    def testCase4():
        n = int(input("Nhập số tủ lạnh: "))
        danhsach = []
        for i in range(n):
            tl = TuLanh()
            tl.nhapThongTin()
            danhsach.append(tl)

        json_string = json.dumps([ob.__dict__ for ob in danhsach], indent=4)
        print(json_string)
        with open("danhsach.json", "w") as outfile:
            outfile.write(json_string)

        
    def testCase5():
        n = int(input("So tu lanh: "))
        ds_tulanh = {}
        cnt = 1
        for i in range(0,n):
            tmp = TuLanh()
            tmp.nhapThongTin()
            if tmp.layNhanHieu() in ds_tulanh.keys():
                cnt+=1
                name = {tmp.layNhanHieu():cnt}
                ds_tulanh.update(name)
            else:
                cnt =1
                name = {tmp.layNhanHieu():cnt}
                ds_tulanh.update(name)
        for i in sorted(ds_tulanh.keys()):
            print(i,f'({ds_tulanh[i]})')


C002454.testCase5()