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
