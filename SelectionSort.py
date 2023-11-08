def Swap(a,b):
    tg=a
    a=b
    b=tg
    return a,b

# def SelectionSort(arr):
#     for i in range(0,len(arr)-1):
#         min=i
#         for j in range(i+1,len(arr)):
#             if arr[j]<arr[min]:
#                 min=j
#         if min!=i:
#             arr[min],arr[i] = Swap(arr[min],arr[i])

# A=[12,2,8,5,1]
# print('Mảng trước khi sắp xếp: ')
# for i in A:
#     print(i,end=" ")
# SelectionSort(A)
# print('\n\nMảng sau khi sắp xếp: ')
# for i in A:
#     print(i,end=" ")


# x="ab"
# def innguoc(x):
#     if x!="":
#         print(x[-1])
#         s=x[0:len(x)-1]
#         innguoc(s)

# def InsertionSort(a):
#     for i in range(len(a)-1):
#         pos = i
#         x = a[i+1]
#         while (pos>=0 and a[pos]>x):
#             a[pos+1] = a[pos]
#             pos-=1
#         a[pos+1] = x

# a = [2,12,8,5,1]
# InsertionSort(a) 
# for i in range(len(a)):
#     print(a[i],end="; ")    

# def BubbleSort(a):
#     for i in range(len(a)-1):
#         for j in range(len(a)-1,i,-1):
#             if a[j]<a[j-1]:
#                 a[j],a[j-1] = Swap(a[j],a[j-1])

# def Swap(a,b):
#     tg=a
#     a=b
#     b=tg
#     return a,b

# a = [2,12,8,5,1]
# BubbleSort(a)
# for i in range(len(a)):
#     print(a[i],end="; ")  

# 
# quick sort
def partition(A, start, end):
    i = start #left pointer
    pivot = A[(start+end)//2] # pivot
    j = end #right pointer
    while True:
        while (A[i] < pivot):
            i+=1 #move left pointer to right
        while (A[j]> pivot):
            j-=1 #move right pointer to left
        if i>=j:
            return j #stop, pivot moved to its correct position
        A[i], A[j] = A[j], A[i] 

def quickSort(A, start, end):
    if start < end:
        p = partition(A, start, end) # p is pivot, it is now at its correct position
        # sort elements to left and right of pivot separately
        quickSort(A, start, p)
        quickSort(A, p+1, end)
A = [24, 10, 30, 13, 20, 27]
print(f"Original array A: {A}")
quickSort(A, 0, len(A)-1)
print(f"Array A after quicksort: {A}")

