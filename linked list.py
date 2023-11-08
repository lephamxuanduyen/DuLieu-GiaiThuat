from ast import While
from tkinter import N, W
from unicodedata import name


class SinhVien:
    def __init__(self, MaSV, name, d1, d2):
        self.MaSV= MaSV
        self.HoTen= name
        self.Diem1= d1
        self.Diem2= d2
        self.TB= None
        self.Next= None
    
    def InSV(self):
        print('Hello', self.MaSV, self.HoTen, self.Diem1, self.Diem2, self.TB)

    def TinhTB(self):
        if (self.Diem1 is not None) and (self.Diem2 is not None):
            self.TB=(self.Diem1+self.Diem2)/2
        else:
            print('Chưa có điểm, nên chưa thể tính được điểm trung bình.')
    
    def TinhTBdiem1(self,s,dem):
        if (self.Diem1 is not None):
            s=s+self.Diem1
            dem=dem+1
            self.TB=s/dem
        else:
            print('Chưa có điểm, không thể tính được điểm trung bình.')
    
    def TinhTBdiem2(self,s,dem):
        if (self.Diem2 is not None):
            s=s+self.Diem2
            dem=dem+1
            self.TB=s/dem
        else:
            print('Chưa có điểm, không thể tính được điểm trung bình.')

    def CapNhapSV(self, HoTen=None, d1=None, d2=None):
        if HoTen is not None:
            self.HoTen=HoTen
        if d1 is not None:
            self.Diem1=d1
        if d2 is not None:
            self.Diem2=d2
    

class DSSV:
    def __init__(self):
        self.head=None
        self.last=None
    
    def InDSSV(self):
        sv=self.head
        while sv is not None:
            sv.InSV()
            sv=sv.Next

    def NhapDSSV(self):
        n=int(input('Số sinh viên cần nhập: '))
        for i in range(n):
            print('Vui lòng nhập thông tin sinh viên thứ',i+1)
            MaSV=input('Mã SV: ')
            name=input('Họ tên: ')
            d1=float(input('Điểm 1: '))
            d2=float(input('Điểm 2: '))
            newSV=SinhVien(MaSV, name, d1,d2)
            newSV.TinhTB()
            newSV.InSV()
            if self.head is None:
                self.head=newSV
            else:
                newSV.Next=self.head
                self.head=newSV
    
    def TinhTB1(self):
        sv=self.head
        s=0
        dem=0
        while sv is not None:
            sv.TinhTBdiem1(s,dem)
            sv.Next

    def TinhTB2(self):
        sv=self.head
        s=0
        dem=0
        while sv is not None:
            sv.TinhTBdiem2(s,dem)
            sv.Next

    def XoaSV(self):
        name=input('Nhập tên sinh viên cần xóa: ')
        sv=self.head
        truoc=None
        while sv is not None and sv.HoTen!=name:
            truoc= sv
            sv=sv.Next
        if sv is not None:
        # Đã tìm thấy vị trí
            if sv==self.head and sv==self.last:
            # Xóa phần tử duy nhất
                self.head=self.last=None
            elif sv==self.head and sv!=self.last:
                # Xóa phần tử đầu tiên, nhưng không phải là phần tử duy nhất
                self.head=sv.Next
            elif sv==self.last:
                # Xóa phần tử cuối, nhưng không phải là phần tử duy nhất
                truoc.Next=None
                self.last=truoc
            else:
                # Xóa phần tử ở giữa
                truoc.Next=sv.Next
            del sv

    def XoaDSSV(self):
        sv=self.head
        self.head=self.last=None
        while sv is not None:
            tam=sv
            sv=sv.Next
            del tam
l=DSSV()
l.NhapDSSV()
l.InDSSV()
print('Điểm trung bình của điểm 1:',l.TinhTB1)
print('Điểm trung bình của điểm 2:',l.TinhTB2)
l.XoaSV()
l.InDSSV()
l.XoaDSSV()
print("Danh sach da xoa")
l.InDSSV()