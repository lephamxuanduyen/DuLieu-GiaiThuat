# Tree Structure
#       10
#      /  \
#    34   89
#   / \
#  45 50

class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
    def addLeft(self,x):
        self.left=Node(x)
    def addRight(self,x):
        self.right=Node(x)
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
# a=Node(10)
# a.addLeft(34)
# a.addRight(89)
# a.left.addLeft(45)
# a.left.addRight(50)
a=Node(10)
b=Node(34)
a.left=b
a.addRight(89)
b.addLeft(45)
b.addRight(50)
print('Duyệt trước: ')
a.truoc(a)
print('\n')
print('Duyệt giữa: ')
a.giua(a)
print('\n')
print('Duyệt sau: ')
a.sau(a)