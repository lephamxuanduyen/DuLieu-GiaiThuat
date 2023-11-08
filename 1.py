
# n=int(input("n="))
# if n==2:
#     print(n)
# else:
#     for i in range(2,n+1):
#         couoc=False
#         for j in range(2,(i//2)+1):
#             if i%j==0:
#                 couoc=True
#                 break
#         if couoc==False:
#             print(i)

# --------------------------------------------------

# Bai 1: Tính tổng, hiệu, tích, thương của a và b

# a=int(input('a='))
# b=int(input('b='))
# print('a+b=',a+b)
# print('a-b=',a-b)
# print('a*b=',a*b)
# if b!=0:
#     print('a/b=',a/b)
# else:
#     print('phep tinh a/b khong thuc hien duoc')

# ------------------------------------------------------
# Bai 2: Giai phuong trinh bac 1

# a=int(input('a='))
# b=int(input('b='))
# if a==0:
#     if b==0:
#         print('Phuong trinh vo so nghiem')
#     else:
#         print('Phuong trinh vo nghiem')
# else:
#     print('phuong trinh co nghiem x=',-b/a)

# ------------------------------------------------------

# Bài 3:

# import math
# a=int(input('a='))
# b=int(input('b='))
# c=int(input('c='))
# d=b*b-(4*a*c)
# if a!=0:
#     if d<0:
#         print('Phuong trinh vo nghiem')
#     elif d==0:
#           print('x=',-b/(2*a))
#     else:
#           print('x1=',(-b+(math.sqrt(d)))/(2*a))
#           print('x2=',(-b-(math.sqrt(d)))/(2*a))
# else:
#     if b==0:
#         if c==0:
#             print('Phuong trinh co vo so nghiem')
#         else:
#             print('Phuong trinh vo ngiem')
#     else:
#         print("Phuong trinh co mot nghiem duy nhat:",-c/b)

# -------------------------------------------------------
# Bai 7:

# n=int(input('n='))
# giaithua=1
# if n>0:
#     for i in range(1,n+1):
#         giaithua=giaithua*i
#     print('n!=',giaithua)
# elif n==0:
#     print("n!=1")


# ---------------------------------------------------------

# Bai 5: So hoan hao

# n=int(input("N="))
# if n>=6:
#     for i in range(6,n+1):
#         s=0
#         for j in range(1,i):
#             if i%j==0:
#                 s=s+j
#         if s==i:
#             print(i)
# ----------------------------------------------------------

# Bai 8: tinh tong 2 phan so

# print("Tinh tong 2 phan so: (a/b) +(c/d)")
# print('Nhap cac phan tu cua hai phan so lan luot la a,b,c,d')
# a=int(input('a='))
# b=int(input('b='))
# c=int(input('c='))
# d=int(input('d='))
# if b==0 or d==0:
#     print('Khong thuc hien duoc phep tinh')
# else:
#     if b==d:
#         x=a+c
#         print(f'Phep cong phan so {a}/{b}+{c}/{d}={x}/{b}')
#     else:
#         x=a*d+c*b
#         y=b*d
#         print(f'Phep cong phan so {a}/{b}+{c}/{d}={x}/{y}')

# -------------------------------------------------------------------

# Bai 6

# n=int(input('n='))
# L=[]
# for i in range(n):
#     L=L+[int(input())]
# print("So lon nhat la:",max(L))
# -------------------------------------------------------------------

# Bài tập 1:


# n=int(input())
# A=[int(x) for x in input().split()]
# B=A.copy()
# # a=list(map(int,input().split()))
# # L=list(set(A))
# def demSl (A,a):
#     dem=0
#     for x in A:
#         if x==a:
#             dem+=1
#     return dem
# for x in A:
#     num=demSl(A,x)
#     while num>1:
#         A.remove(x)
#         num=num-1
# L=sorted(A)
# for a in L:
#     print(a,demSl(B,a))
# ------------------------------------------------------------
# Bài 7 _ Chuong ĐỆ quy _ Viết chương trình tính dãy Fibonaci ko đệ quy:

# n=int(input("n="))
# if (n<=2): print(1)
# else:
#     b=1
#     c=1
#     for i in range(3,n+1):
#         a=b+c
#         b=a
#         c=b
#     print(a)

# -------------------------------------------------------------------------
# Bài 8 _ Chương Đệ quy _ Viết chương trình in xâu đảo ngược không đệ quy

# l=list(input("Mời bạn nhập 1 câu kí tự bất kì: "))
# l.reverse()
# print("Xâu đảo ngược:")
# for a in l: print(a,end='')

# ----------------------------------------------------------------------------------
# Bài 9 _Chuong Đệ quy _ Cài đặt thuật toán Hà Nội có đệ quy (n=30)

# def HaNoi(A,n):
#     B=[]
#     for i in range(n):
#         B=[A[i]]+B
#     return B   
# n=int(input("n="))
# A=[int(x) for x in range(1,n+1)]
# B=HaNoi(A,n)
# C=HaNoi(B,n)
# print("A =",A)
# print("Trung gian B =",B)
# print("C =",C)

# n=int(input('n='))
# def tinh_tich(n):
#     tich_P = 1
#     if n>0:
#         for i in range(1,n+1):
#             tich_P = tich_P*i
#     return tich_P
# print('Tích của P là:',tinh_tich(n))

# def HaNoi(n, A, B, C):

#     if (n==1):

#         print(A,'->',C)
#     else:

#         HaNoi(n -1, A, C, B)
#         HaNoi(1, A, B, C)
#         HaNoi(n -1, B, A, C)
# n=int(input('n='))
# A= 'A'; B= 'B'; C= 'C'
# HaNoi(n, A, B, C)

# n=int(input('n='))
# A=[]
# def find(A,i):
#     for j in range(2):
#         A[i]=j
#         if i==n-1:
#             print(A)
#         else: find(A,i+1)
# for i in range(n):
#     A.append(0)
# find(A,0)

# n=int(input('n='))
# A=[]
# for i in range(n):
#     A.append(0)

# 1. Tìm con số 0 đầu tiên biến nó thành 0
# 2. Nếu đầu tiên không phải là số 0 thì tiếp tục tìm số 0 đầu tiên và biến nó thành 1 và biền tất cả những con số 1 sau nó thành số 0

# --------------------------------------------------------------------------------------------------------------------------------------
# l=[]
# for i in range(2000,3201):
#     if i%7==0 and i%5!=0:
#         l.append(i)
# for i in range(1,len(l)):
#     print(i,end=', ')
# print(', '.join(l))

# n=int(input('n='))
# D={}
# for i in range(1,n+1):
#     D[i]=i*i
# print(D)

# ============================================
#          BÀI TOÁN QUẢN LÝ SINH VIÊN
# ============================================ 

# SỬ DỤNG DICTIONARY

# l_students=[]
# l_id=[]
# kq=[]

# def add():
#     print('*** THÊM THÔNG TIN SINH VIÊN ***')
#     n=int(input('Nhập số học sinh cần thêm: '))
#     for i in range(1,n+1):
#         inf={
#         'id':'',
#         'name':'',
#         'class':'',
#         'mark1':0,
#         'mark2':0,
#         'average':0,
#         'grade':'',
#         }
#         id=input('ID: ')
#         if id in l_id:
#             print('ID này đã tồn tại!')
#         else:
#             l_id.append(id)
#             print('Nhập thông tin sinh viên.')
#             inf['id']=id
#             inf['name']=input('Họ và Tên: ')
#             inf['class']=input('Lớp: ')
#             inf['mark1']=float(input('Điểm môn 1: '))
#             inf['mark2']=float(input('Điểm môn 2: '))
#             l_students.append(inf)

# def delete():
#     print('*** XÓA THÔNG TIN SINH VIÊN ***')
#     id=input('Nhập ID sinh viên cần xóa: ')
#     if id in l_id:
#         l_students.remove(l_students[l_id.index(id)])
#         l_id.remove(id)
#         print('Xóa sinh viên thành công.')
#     else:
#         print('Không tìm thấy sinh viên cần xóa.')

# def edit():
#     print('*** SỬA THÔNG TIN SINH VIÊN ***')
#     id=input('Nhập id sinh viên cần sửa: ')
#     if id in l_id:
#         idx=l_id.index(id)
#         print('Sửa lại thông tin.')
#         l_students[idx]['name']=input('Họ và Tên: ')
#         l_students[idx]['class']=input('Lớp : ')
#         l_students[idx]['mark1']=float(input('Điểm môn 1: '))
#         l_students[idx]['mark2']=float(input('Điểm môn 2: '))
#     else:
#         print('Không tìm thấy sinh viên cần sửa.')
# def show():
#     print('*** HIỂN THỊ DANH SÁCH SINH VIÊN ***')
#     for i in range(len(l_students)):
#         print('|',l_students[i]['id'],'|',l_students[i]['name'],'|',l_students[i]['class'],'|',l_students[i]['mark1'],'|',l_students[i]['mark2'])
# def aver():
#     print('*** ĐIỂM TRUNG BÌNH CỦA TỪNG SINH VIÊN ***')
#     for i in range(len(l_students)):
#         l_students[i]['average']=(l_students[i]['mark1']+l_students[i]['mark2'])/2
#         print('Điểm trung bình của sinh viên có ID ',l_students[i]['id'],'là:',l_students[i]['average'])

# def aver1():
#     print('*** ĐIỂM TRUNG BÌNH MÔN 1 CỦA TOÀN BỘ SINH VIÊN ***')
#     s=0
#     for i in range(len(l_students)):
#         s=s+l_students[i]['mark1']
#     print('Trung bình điểm môn 1:',round(s/len(l_students),2))

# def aver2():
#     print('*** ĐIỂM TRUNG BÌNH MÔN 2 CỦA TOÀN BỘ SINH VIÊN ***')
#     s=0
#     for i in range(len(l_students)):
#         s=s+l_students[i]['mark2']
#     print('Trung bình điểm môn 2:',round(s/len(l_students),2))

# def find_min():
#     tb=[]
#     for i in range(len(l_students)):
#         tb.append(l_students[i]['average'])
#     tb_min=min(tb)
#     print('Sinh viên có điểm trung bình thấp nhất:')
#     for i in range(len(l_students)):
#         if tb[i]==tb_min:
#             print('|',l_students[i]['id'],'|',l_students[i]['name'],'|',l_students[i]['class'],'|',l_students[i]['mark1'],'|',l_students[i]['mark2'],'|',l_students[i]['average'])  

# def find_max():
#     tb=[]
#     for i in range(len(l_students)):
#         tb.append(l_students[i]['average'])
#     tb_max=max(tb)
#     print('Sinh viên có điểm trung bình cao nhất:')
#     for i in range(len(l_students)):
#         if tb[i]==tb_max:
#             print('|',l_students[i]['id'],'|',l_students[i]['name'],'|',l_students[i]['class'],'|',l_students[i]['mark1'],'|',l_students[i]['mark2'],'|',l_students[i]['average'])

# def sx_class():
#     sx=[]
#     print('*** SẮP XẾP SINH VIÊN THEO LỚP VÀ ĐIỂM TRUNG BÌNH ***')
#     n_students=len(l_students)
#     lop_ChuaLoai=[]
#     for i in range(n_students):
#         lop_ChuaLoai.append(l_students[i]['class'])
#     lop_loai=list(set(lop_ChuaLoai))
#     n_lop=len(lop_loai)
#     for a in range(n_lop):
#         sv_ChungLop=[]
#         for i in range(n_students):
#             if l_students[i]['class']==lop_loai[a]:
#                 sv_ChungLop.append(l_students[i])
#         sx.append(sv_ChungLop)
#     for a in range(n_lop):
#         sv_1lop=len(sx[a])
#         if sv_1lop>1:
#             for i in range((sv_1lop-1)):
#                 for j in range(i+1,sv_1lop):
#                     if sx[a][i]['average']>sx[a][j]['average']:
#                         tg=sx[a][i]
#                         sx[a][i]=sx[a][j]
#                         sx[a][j]=tg
#     for i in range(len(sx)):
#         for j in range(len(sx[i])):
#             kq.append(sx[i][j])
#     print('Danh sách sinh viên đã sắp xếp:')
#     for i in range(len(kq)):
#         print('|',kq[i]['id'],'|',kq[i]['name'],'|',kq[i]['class'],'|',kq[i]['mark1'],'|',kq[i]['mark2'],'|',kq[i]['average'],'|',kq[i]['grade'])

    
# def XepLoai():
#     print('*** XẾP LOẠI SINH VIÊN ***')
#     for i in range(len(kq)):
#         if 9<=kq[i]['average']<=10:
#             kq[i]['grade']='Xuất sắc'
#         elif 8<=kq[i]['average']<9:
#             kq[i]['grade']='Giỏi'
#         elif 6.5<=kq[i]['average']<8:
#             kq[i]['grade']='Khá'
#         elif 5<=kq[i]['average']<6.5:
#             kq[i]['grade']='Trung bình'
#         elif 0<=kq[i]['average']<5:
#             kq[i]['grade']='Yếu'
#         print('|',kq[i]['id'],'|',kq[i]['name'],'|',kq[i]['class'],'|',kq[i]['mark1'],'|',kq[i]['mark2'],'|',kq[i]['average'],'|',kq[i]['grade'])

# while True:
#     print("CHỨC NĂNG")
#     print('----------------------------------------------------------')
#     print("Chọn chức năng muốn thực hiện:")
#     print("Nhập 1: Thêm sinh viên")
#     print("Nhập 2: Xóa sinh viên")
#     print("Nhập 3: Sửa sinh viên")
#     print("Nhập 4: Xem danh sách sinh viên")
#     print("Nhập 5: Tính điểm trung bình học tập cho từng sinh viên (average)")
#     print("Nhập 6: Tính điểm trung bình cho môn 1 của toàn bộ sinh viên")
#     print("Nhập 7: Tính điểm trung bình cho môn 2 của toàn bộ sinh viên")
#     print("Nhập 8: Tìm xem sinh viên nào có điểm trung bình học tập thấp nhất ")
#     print("Nhập 9: Tìm xem sinh viên nào có điểm trung bình học tập cao nhất ")
#     print("Nhập 10: Sắp xếp danh sách sinh viên theo lớp, nếu trong lớp có nhiều bạn thì sắp xếp từ thấp đến cao theo điểm trung bình học tập ")
#     print("Nhập 11: Xếp loại học lực cho từng sinh viên theo công thức: Xuất sắc (TB>=9), Giỏi (TB>=8), Khá (TB>=6.5, Trung Bình (TB>=5), Yếu (TB<5) ")
#     print("Nhập 0: Thoát khỏi chương trình")
#     print('----------------------------------------------------------')
#     cv=int(input('Mời bạn chọn chức năng: '))
#     if cv==1: add()
#     elif cv==2: delete()
#     elif cv==3: edit()
#     elif cv==4: show()
#     elif cv==5: aver()
#     elif cv==6: aver1()
#     elif cv==7: aver2()
#     elif cv==8: find_min()
#     elif cv==9: find_max()
#     elif cv==10: sx_class()
#     elif cv==11: XepLoai()
#     elif cv==0: break

# ----------------------------------------------------------------------------------------------------------------------------------------

# SỬ DỤNG OOP

# class Student:
#     # def __init__(self, maSV):
#     #     self.id=maSV,
#     #     self.name='',
#     #     self.Class='',
#     #     self.mark1=0,
#     #     self.mark2=0,
#     #     self.average=0,
#     #     self.grade=''
#     def __init__(self, maSV,ten, lop, d1,d2):
#         self.id=maSV,
#         self.name=ten,
#         self.Class=lop,
#         self.mark1=d1,
#         self.mark2=d2,
#         self.average=0,
#         self.grade=''

#     def printStudent(self):
# 	    print('[',self.id,"]", "[", self.name,"]","[", self.mark1,"]","[", self.mark2,"]")





# class ListStudent(Student):
#     def __init__(self):
#         self.ListOfStudent= []


#     def addStudent(self, masv):
#         newStudent = Student(masv)
#         self.ListOfStudent.append(newStudent)

    
#     def showListStudent(self):
#         for i in self.ListOfStudent:
#             i.printStudent()

#     def average(self,tenmon):
#         sum = 0
#         for std in self.ListOfStudent:
#             sum = sum + std.tenmon
#         n = self.ListOfStudent.len()
#         if n > 0:
#             averag = sum/n
#         else:
#             averag = 0
#         return tenmon, averag

# sv=Student()

# while True:
#     print("CHỨC NĂNG")
#     print('----------------------------------------------------------')
#     print("Chọn chức năng muốn thực hiện:")
#     print("Nhập 1: Thêm sinh viên")
#     print("Nhập 2: Xóa sinh viên")
#     print("Nhập 3: Sửa sinh viên")
#     print("Nhập 4: Xem danh sách sinh viên")
#     print("Nhập 5: Tính điểm trung bình học tập cho từng sinh viên (average)")
#     print("Nhập 6: Tính điểm trung bình cho môn 1 của toàn bộ sinh viên")
#     print("Nhập 7: Tính điểm trung bình cho môn 2 của toàn bộ sinh viên")
#     print("Nhập 8: Tìm xem sinh viên nào có điểm trung bình học tập thấp nhất ")
#     print("Nhập 9: Tìm xem sinh viên nào có điểm trung bình học tập cao nhất ")
#     print("Nhập 10: Sắp xếp danh sách sinh viên theo lớp, nếu trong lớp có nhiều bạn thì sắp xếp từ thấp đến cao theo điểm trung bình học tập ")
#     print("Nhập 11: Xếp loại học lực cho từng sinh viên theo công thức: Xuất sắc (TB>=9), Giỏi (TB>=8), Khá (TB>=6.5, Trung Bình (TB>=5), Yếu (TB<5) ")
#     print("Nhập 0: Thoát khỏi chương trình")
#     print('----------------------------------------------------------')
#     cv=int(input('Mời bạn chọn chức năng: '))
#     if cv==1: add()
#     elif cv==2: delete()
#     elif cv==3: edit()
#     elif cv==4: show()
#     elif cv==5: aver()
#     elif cv==6: aver1()
#     elif cv==7: aver2()
#     elif cv==8: find_min()
#     elif cv==9: find_max()
#     elif cv==10: sx_class()
#     elif cv==11: XepLoai()
#     elif cv==0: break
# --------------------------------------------------------------------------------------------------------------------------------------

# SỬ DỤNG OOP
# -----------

# # Tính giai thừa

# n=int(input('n='))
# def giaithua(n):
#     if n==1:
#         return 1
#     else:
#         return n*giaithua(n-1)
# print(giaithua(n))

# # Tinh tong

# def tong(n):
#     if n==1:
#         return 1
#     else:
#         return n+tong(n-1)

# n=int(input("n="))
# print(tong(n))

# def Binarysearch(a,n,x):
#     left=0
#     right=n-1
#     while (left<=right):
#         mid = (left+right)//2
#         if (x==a[mid]):
#             return mid
#         if (x<a[mid]):
#             right=mid-1
#         else:
#             left=mid+1
#     return -1

# A=[2,5,9,7,3,4]
# A.sort()
# x=5
# tim=Binarysearch(A,len(A),x)
# if (tim==-1):
#     print("Không tồn tại")
# else:
#     print("Vị trí của",x,"là:",tim+1)

# import math
# def insnt(n):
#     if n==2:
#         print(n)
#     else:
#         s=0
#         for j in range(2,int(math.sqrt(n))+1):
#             if n%j==0:
#                 s=+1
#         if s==0:
#             print(n)
#         insnt(n-1)
# n=int(input('n='))
# insnt(n)

def tong(n):
    if n==0:
        return 0
    else:
        return n+tong(n-1)

print(tong(0))