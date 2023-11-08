# def LinearSearch(A,x):
#     for i in range(len(A)):
#  if x==A[i]:
#             print("Vị trí của X là: ",i)
#             break
#     else:
#         print("Không tìm thấy X trong mảng.")

# A=[1,2,3,4,5,6]
# x=5 

# LinearSearch(A,x)


# def tktt(a,n,x):
#     i=0
#     a.append(x)
#     while x!=a[i]:
#         i=+1
#     if (i<n):
#         return i
#     return "Không tìm thấy"

# A=[1,2,3,4,5,6]
# x=4
# n=len(A)
# print(tktt(A,n,x))

# def LinearSearch(a,x):
#     i=0
#     a.append(x)
#     while a[i]!=x and (i<len(a)):
#         i=i+1
#     if i<len(a):
#         return i
#     else:
#         return "Không tìm thấy"

# A=[1,2,3,4,5,6]
# x=4
# print("Vị trí x cần tìm trong mảng:",LinearSearch(A,x))

# def BinarySearch(a,x):
#     left = 0
#     right = len(a)-1
#     while left<=right:
#         mid = (left+right)//2
#         if x == a[mid]:
#             return mid
#         if x < a[mid]:
#             right = mid-1
#         else:#if x > a[mid]:
#             left = mid+1
#     return "Không tìm thấy"

# A=[1,2,3,4,5,6]
# x=4
# print("Vị trí x cần tìm trong mảng:",BinarySearch(A,x))

def BinarySearch(a,left, right, x):
    mid = (left+right)//2
    while left<=right:
        if x == a[mid]:
            return mid
        if x<a[mid]:
            return BinarySearch(a,left,mid-1,x)
        else:
            return BinarySearch(a,mid+1, right,x)

A=[1,2,3,4,5,6]
x=4
print("Vị trí x cần tìm trong mảng:",BinarySearch(A,0,len(A),x)+1)

# def InterchangeSort(a):
#     for i in range(len(a)-1):
#         for j in range(i+1,len(a)):
#             if a[j]<a[i]:
#                 a[i],a[j]=a[j],a[i]

# a = [2,12,8,5,1]
# InterchangeSort(a) 
# for i in range(len(a)):
#     print(a[i],end="; ")  