# # BÀI 1: ĐỊNH NGHĨA CÁC PHÉP TOÁN CHO STACK VÀ SỬ DỤNG NÓ ĐỂ CHUYỂN CƠ SỐ TỪ CƠ SỐ 10 SANG CƠ SỐ X

# from turtle import st


# class Stack:
#     def __init__(self):
#         self.stack=[]
#         self.size=0
#         self.top=-1
#     def pushs(self,x):
#         self.stack.append(x)
#         self.size+=1
#         self.top+=1
#     def isEmpty(self):
#         if self.size<=0:
#             return True
#         else:
#             return False
#     def pops(self):
#         if self.isEmpty()==True:
#             return ("No element in th Stack.")
#         else:
#             self.top-=1
#             self.size-=1
#             return self.stack.pop()

# n=int(input('n = '))
# x=int(input('Co so: '))
# AStack = Stack()
# while n>0:
#     AStack.pushs(n%x)
#     n=n//x
# while AStack.isEmpty()!=True:
#     print(AStack.pops(),end='')

# BÀI 2: ĐỊNH NGHĨA KIỂU DỮ LIỆU VÀ PHÉP TOÁN CHO QUEUE, SAU ĐÓ SỬ DỤNG ĐỂ NHẬP VÀO 1 DÃY SỐ, IN RA BÌNH PHƯƠNG CỦA TỪNG SỐ THEO THỨ TỰ NHẬP VÀO

# from operator import le


class Queue:
    def __init__(self):
        self.queue = list()

    def add(self,dataval):
        if dataval not in self.queue:
            self.queue.insert(0,dataval)
            return True
        return False
    
    def remove(self):
        if len(self.queue)>0:
            return self.queue.pop()
        return ("No elements in Queue!")

Q = Queue()
N=int(input('So luong so nhap vao: '))
for i in range(N):
    n=int(input())
    Q.add(n)
print('***IN KẾT QUẢ***')
for j in range(N):
    print(Q.remove()**2)