class BinarySearchTree:
    
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def search(self, value):
        if self.data == value:
            return True
        if self.data > value:
            if self.left:
                return self.left.search(value)
            else:
                return False
            
        else:
            if self.right:
                return self.right.search(value)
            else:
                return False
        
        
    def add(self, value):
        
        if self.data == value:
            return     
        if self.data > value:
            if self.left == None:
                self.left = BinarySearchTree(value)
            
            else:
                self.left.add(value)   
        else:
            if self.right == None:
                self.right = BinarySearchTree(value)
            else:
                self.right.add(value)
                
    def inorder_traversal(self):
        # Left-Node-Right -> LNR
        elements = []
        if self.left:
            elements += self.left.inorder_traversal()
        elements.append(self.data)
        if self.right:
            elements += self.right.inorder_traversal()
        return elements
    
    def preorder_traversal(self):
        # Node-Left-Right -> NLR
        
        elements = []
        elements.append(self.data)
        if self.left:
            elements += self.left.preorder_traversal()
        
        if self.right:
            elements += self.right.preorder_traversal()
        return elements
    
    def postorder_traversal(self):
        # Left-Right-Node -> LRN
        
        elements = []
        
        if self.left:
            elements += self.left.postorder_traversal()
        if self.right:
            elements += self.right.postorder_traversal()
            
        elements.append(self.data)

        return elements
    
    def reverse(self):
        self.left, self.right = self.right, self.left
        if self.left:
            self.left.reverse()
        if self.right:
            self.right.reverse()
        
                
                
if __name__ == "__main__":
    elements = [15, 12, 27, 7, 14, 20, 88, 23]
    root = BinarySearchTree(15)
    for element in elements:
        root.add(element)
        
    # print(root.data)
    # print(root.left.data)
    # print(root.left.left.data)
    # print(root.left.right.data)
    # print(root.right.left.right.data)
    print(root.inorder_traversal())
    print(root.preorder_traversal())
    print(root.postorder_traversal())
    
    print(root.search(88))
    print(root.search(212))
    root.reverse()
    print(root.inorder_traversal())
    