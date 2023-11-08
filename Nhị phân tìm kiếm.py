class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
    def truoc(self,root):
        if (root!=None):
            print(root.data,end=" ")
            self.truoc(root.left)
            self.truoc(root.right)
    def giua(self,root):
        if (root!=None):
            self.giua(root.left)
            print(root.data,end=" ")
            self.giua(root.right)
    def sau(self,root):
        if (root!=None):
            self.sau(root.left)
            self.sau(root.right)
            print(root.data,end=" ")
    
    def Insert(self,x):
        if self.data:
            if x<self.data:
                if self.left is None:
                    self.left=Node(x)
                else:
                    self.left.Insert(x)
            elif x>self.data:
                if self.right is None:
                    self.right = Node(x)
                else:
                    self.right.Insert(x)
            else:
                self.data=x
    def CreateTree(self):
        n=int(input('Số nút muốn nhập: '))
        for i in range(n):
            x=int(input('Nhãn của nút: '))
            self.Insert(x)
        # l=[37,10,18,29,50,3,1,6,5,12,20,35,13,32,41]
        # for i in l:
        #     self.Insert(i)
    def Detele(self, x):
        if self==None:
            return self
        if x<self.data:
            if self.left:
                self.left = self.left.Detele(x)
            return self
        if x>self.data:
            if self.right:
                self.right =self.right.Detele(x)
            return self
        if self.right == None: # chỉ có con trái
            return self.left
        if self.left == None: # chỉ có con phải
            return self.right

        min_larger_node = self.right
        while min_larger_node.left:
            min_larger_node = min_larger_node.left
        self.data = min_larger_node.data
        self.right = self.right.Detele(min_larger_node.data)
        return self
    def findval(self, val):
        if val < self.data:
            if self.left is None:
                return str(val)+" is not Found"
            return self.left.findval(val)
        elif val > self.data:
            if self.right is None:
                return str(val)+" is not Found"
            return self.right.findval(val)
        else:
            return str(self.data) + " is found"
root=Node(40)
root.CreateTree()
# print('Duyệt trước: ')
# root.truoc(root)
# print('\n')
print('Duyệt giữa: ')
root.giua(root)
# print('\n')
# print('Duyệt sau: ')
# root.sau(root)
# print('\n')
# print('Xóa nút 37, In cây duyệt giữa')
# root.Detele(37)
# root.giua(root)
# print('\n')
# print('Xóa nút 10, In cây duyệt giữa')
# root.Detele(10)
# root.giua(root)