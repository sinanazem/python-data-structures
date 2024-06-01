class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None
        
    def add_child(self, data):
        if type(data) != BinaryTree:
            data = BinaryTree(data)
        
        if self.left_child == None:
            self.left_child = data
        
        elif self.right_child == None:
            self.right_child = data
        
        else:
            self.left_child.add_child(data)
            

if __name__ == "__main__":
    root = BinaryTree(1)
    root.add_child(5)
    root.add_child(12)
    root.add_child(3)
    root.add_child(6)

    
    print(root.left_child.left_child.data)
    
        
            
            
            