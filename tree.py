class Node:
    def __init__ (self,data):
        self.data=data
        self.left=None
        self.right=None
    def search(self,target):
        if self.data==target:
            print("Found")
            print(self.data)
            return self
        if self.left and self.data > target:
            self.left.search(target)
        elif self.right and self.data < target:
            self.right.search(target)
        else :
            print("Not Found")
            return None

    # Preorder (Root, Left, Right) 
    # Inorder (Left, Root, Right)
    #Postorder (Left, Right, Root)
    def traversePreorder(self):
        print(self.data)
        if(self.left):
            self.left.traversePreorder()
        if(self.right):
            self.right.traversePreorder()
    def traversePostorder(self):
        if(self.left):
            self.left.traversePreorder()
        if(self.right):
            self.right.traversePreorder()
        print(self.data)
    def traverseInorder(self):
        if(self.left):
            self.left.traversePreorder()
        print(self.data)     
        if(self.right):
            self.right.traversePreorder()
    
    def height(self,h=0):#h is current level
        leftHeight=self.left.height(h+1) if self.left else h
        rightHeight=self.right.height(h+1) if self.right else h
        return max(leftHeight,rightHeight)
            


class Tree:
    def __init__(self,root,name="") -> None:
        self.root=root
        self.name=name
    def search(self,target):
        self.root.search(target)
    def traversePreorder(self):
        self.root.traversePreorder()
    def traversePostorder(self):
       self.root.traversePostorder()
    def traverseInorder(self):
        self.root.traverseInorder()



def searchTree(el,data):
    if el==None:
        return False
    if(el.data==data):
        return el
    elif(el.data>data):
        return searchTree(el.left,data)
    else:
        return searchTree(el.right,data)
        

tree=Tree(Node(50 ))
tree.root.left=Node(25)
tree.root.right=Node(75)
tree.root.left.left=Node(10)
tree.root.left.right=Node(35)
tree.root.right.left=Node(30)
tree.root.right.right=Node(42)
tree.root.left.left.left=Node(5)
tree.root.left.left.right=Node(13)

print("Traverse Post Order")
tree.traversePostorder()

print("\nTraverse In Order")
tree.traverseInorder()

print("\nTraverse Pre Order")
tree.traversePreorder()

#Every leaf to bottom means hegiht
