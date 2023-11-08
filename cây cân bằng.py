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
    def getHeight(self, root) :
        if (root == None):
            return 0
        return 1 + max(getHeight(root->left), getHeight(root->right))
    