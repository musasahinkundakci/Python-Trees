from operator import le


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

    def traversePreorder(self):
        # Preorder (Root, Left, Right) 

        print(self.data)
        if(self.left):
            self.left.traversePreorder()
        if(self.right):
            self.right.traversePreorder()

    def traversePostorder(self):
        #Postorder (Left, Right, Root)

        if(self.left):
            self.left.traversePreorder()
        if(self.right):
            self.right.traversePreorder()
        print(self.data)

    def traverseInorder(self):
        # Inorder (Left, Root, Right)

        if(self.left):
            self.left.traversePreorder()
        print(self.data)     
        if(self.right):
            self.right.traversePreorder()
    
    #Height Of Binary Tree
    def height(self,h=0):
        leftHeight=self.left.height(h+1) if self.left else h
        rightHeight=self.right.height(h+1) if self.right else h
        return max(leftHeight,rightHeight)
            
    def getNodesAtDepth(self,depth,nodes=[]):
        if depth==0:
            nodes.append(self.data)
            return nodes
        if self.left:
            self.left.getNodesAtDepth(depth-1,nodes)
        else:
            nodes.extend([None]*2**(depth-1))#In every stage there are 2**depth nodes exist.
        if self.right:
            self.right.getNodesAtDepth(depth-1,nodes)
        else:
            nodes.extend([None]*2**(depth-1))
        return nodes



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

    def height(self):
        return self.root.height()
        
    def getNodesAtDepth(self,depth):
        return self.root.getNodesAtDepth(depth)

    def _nodeToChar(self, n, spacing):
        if n is None:
            return '_'+(' '*spacing)
        spacing = spacing-len(str(n))+1
        return str(n)+(' '*spacing)

    def print(self, label=''):
        print(self.name+' '+label)
        height = self.root.height()
        spacing = 3
        width = int((2**height-1) * (spacing+1) + 1)
        # Root offset
        offset = int((width-1)/2)
        for depth in range(0, height+1):
            if depth > 0:
                # print directional lines
                print(' '*(offset+1)  + (' '*(spacing+2)).join(['/' + (' '*(spacing-2)) + '\\']*(2**(depth-1))))
            row = self.root.getNodesAtDepth(depth, [])
            print((' '*offset)+''.join([self._nodeToChar(n, spacing) for n in row]))
            spacing = offset+1
            offset = int(offset/2) - 1
        print('')

def searchTree(el,data):

    if el==None:
        return False
    if(el.data==data):
        return el
    elif(el.data>data):
        return searchTree(el.left,data)
    else:
        return searchTree(el.right,data)
        
"""
      50
    /   \    
   25     75
   / \     / \
  13  37   55  103
 / \  / \  / \ / \ 
2  20             256
"""
tree=Tree(Node(50))
tree.root.left=Node(25)
tree.root.right=Node(75)
tree.root.left.left=Node(13)
tree.root.left.right=Node(37)
tree.root.right.left=Node(55)
tree.root.right.right=Node(103)
tree.root.left.left.left=Node(2)
tree.root.left.left.right=Node(20)
tree.root.right.right.right=Node(256)

print("Traverse Post Order")
tree.traversePostorder()

print("\nTraverse In Order")
tree.traverseInorder()

print("\nTraverse Pre Order")
tree.traversePreorder()

height=tree.height()
print("\nHeight of the tree => {}".format(height))
#Every leaf to bottom means hegiht

print("\nThe nodes at 3 depth of the tree => {}".format(tree.getNodesAtDepth(3)))

tree.print("Tree 1")
