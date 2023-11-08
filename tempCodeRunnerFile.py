class Student:
    # def __init__(self, maSV):
    #     self.id=maSV,
    #     self.name='',
    #     self.Class='',
    #     self.mark1=0,
    #     self.mark2=0,
    #     self.average=0,
    #     self.grade=''
    def __init__(self, maSV,ten, lop, d1,d2):
        self.id=maSV,
        self.name=ten,
        self.Class=lop,
        self.mark1=d1,
        self.mark2=d2,
        self.average=0,
        self.grade=''

    def printStudent(self):
	    print('[',self.id,"]", "[", self.name,"]","[", self.mark1,"]","[", self.mark2,"]")





class ListStudent(Student):
    def __init__(self):
        self.ListOfStudent= []


    def addStudent(self, masv):
        newStudent = Student(masv)
        self.ListOfStudent.append(newStudent)

    
    def showListStudent(self):
        for i in self.ListOfStudent:
            i.printStudent()

    def average(self,tenmon):
        sum = 0
        for std in self.ListOfStudent:
            sum = sum + std.tenmon
        n = self.ListOfStudent.len()
        if n > 0:
            averag = sum/n
        else:
            averag = 0
        return tenmon, averag

sv=Student()

while True:
    print("CHỨC NĂNG")
    print('----------------------------------------------------------')
    print("Chọn chức năng muốn thực hiện:")
    print("Nhập 1: Thêm sinh viên")
    print("Nhập 2: Xóa sinh viên")
    print("Nhập 3: Sửa sinh viên")
    print("Nhập 4: Xem danh sách sinh viên")
    print("Nhập 5: Tính điểm trung bình học tập cho từng sinh viên (average)")
    print("Nhập 6: Tính điểm trung bình cho môn 1 của toàn bộ sinh viên")
    print("Nhập 7: Tính điểm trung bình cho môn 2 của toàn bộ sinh viên")
    print("Nhập 8: Tìm xem sinh viên nào có điểm trung bình học tập thấp nhất ")
    print("Nhập 9: Tìm xem sinh viên nào có điểm trung bình học tập cao nhất ")
    print("Nhập 10: Sắp xếp danh sách sinh viên theo lớp, nếu trong lớp có nhiều bạn thì sắp xếp từ thấp đến cao theo điểm trung bình học tập ")
    print("Nhập 11: Xếp loại học lực cho từng sinh viên theo công thức: Xuất sắc (TB>=9), Giỏi (TB>=8), Khá (TB>=6.5, Trung Bình (TB>=5), Yếu (TB<5) ")
    print("Nhập 0: Thoát khỏi chương trình")
    print('----------------------------------------------------------')
    cv=int(input('Mời bạn chọn chức năng: '))
    if cv==1: add()
    elif cv==2: delete()
    elif cv==3: edit()
    elif cv==4: show()
    elif cv==5: aver()
    elif cv==6: aver1()
    elif cv==7: aver2()
    elif cv==8: find_min()
    elif cv==9: find_max()
    elif cv==10: sx_class()
    elif cv==11: XepLoai()
    elif cv==0: break