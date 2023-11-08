def BinarySearch(a,left,right,x):
    mid=(left+right)//2
    while left<right:
        if x==a[mid]:
            return str(x)+" nằm ở vị trí thứ "+str(mid+1)+" trong mảng"
        if x<a[mid]:
            return BinarySearch(a,left,mid-1,x)
        else:
            return BinarySearch(a,mid+1,right,x)

a=[5,4,9,3,7]
n=len(a)-1
print(BinarySearch(a,0,n,4))