import pandas as pd
from tabulate import tabulate
import os


class QLSV():
    def nhapthongtin(self):
        f = open("qlsv.txt", "a")
        diems = []
        i = 0
        tongdiem = 0
        ten = str(input("Nhập họ tên sinh viên thứ %d : " % (j+1)))
        tuoi = int(input("Nhập tuổi sinh viên thứ %d : " % (j+1)))
        for i in range(0, n):
            while True:
                diem = float(
                    input("Nhập điểm môn thứ %d của sinh viên thứ %d : " % ((i+1), (j+1))))
                if diem >= 0 and diem <= 10:
                    diems += [diem]
                    tongdiem += diem
                    break
        diemtb = tongdiem/len(diems)
        f.write("{:15}{:15}{:15}\n".format(
            ten, str(tuoi), str(diemtb)))
        f.close()

    def hienthi(self):
        try:
            r = open("qlsv.txt", "r")
            h = r.readlines()
            print("{:5}{:}".format((str("STT")), (h[0])), end="")
            for i in range(1, len(h)):
                print("{:5}{:}".format((str(i)), (h[i])), end="")
            r.close()
        except:
            print("không mở được file")

    def sua(self):
        r = open("qlsv.txt", "r")
        w = open("qlsv1.txt", "a")
        k = int(input("nhấp dòng cần sửa : "))
        r = open("qlsv.txt", "r")
        try:
            for i in range(0, len(r.readlines())):
                if i != k:
                    r.close()
                    r = open("qlsv.txt", "r")

                    a = (r.readlines())[i]
                    w.write(str(a))
                else:
                    ten = str(input("nhập tên cần sửa : "))
                    tuoi = int(input("nhập tuôi cần sửa : "))
                    diemtb = float(input("nhập điểm dtb cần sửa : "))
                    w.write("{:15}{:15}{:15}\n".format(
                        ten, str(tuoi), str(diemtb)))
            os.rename('qlsv1.txt', 'qlsv.txt')
            r.close()
            w.close()
        except:
            pass
# phần sửa và xoá dùng 2 cách khác nhau

    def xoa(self):
        f = open("qlsv.txt", "r+")
        d = f.readlines()
        k = int(input("Nhập dòng cần xoá : "))
        try:
            e = d[k]
            f.seek(0)
            for i in d:
                if i != e:
                    f.write(i)
            f.truncate()
        except:
            print("Quá số dòng")
        f.close()


QLSV = QLSV()
bang = {"chức năng": ["nhập", "hiển thị", "sửa", "xoá",
                      "thoát"], "Nhấn": ["0", "1", "2", "3", "số bất kì"]}
df1 = pd.DataFrame(bang)
while True:
    print(tabulate(df1, headers="keys", tablefmt="psql"))
    sochucnang = int(input("Nhập số để thực hiện chức năng : "))
    if sochucnang == 0:
        try:
            f = open("qlsv.txt", "r")
        except:
            f = open("qlsv.txt", "w")
            f.write("{:15}{:15}{:15}\n".format("ten", "tuoi", "diemtb"))
            f.close()
        m = int(input("Nhập số sinh viên cần nhập : "))
        n = int(input("Nhập số môn học : "))
        for j in range(0, m):
            QLSV.nhapthongtin()
    elif sochucnang == 1:
        QLSV.hienthi()
    elif sochucnang == 2:
        QLSV.hienthi()
        QLSV.sua()
    elif sochucnang == 3:
        QLSV.hienthi()
        QLSV.xoa()
    elif sochucnang != 1 or sochucnang != 2 or sochucnang != 3 or sochucnang != 0:
        break
    key = int(input("bạn muốn tiếp tục không(1 để thoát) : "))
    if key == 1:
        break
