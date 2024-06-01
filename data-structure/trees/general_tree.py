class NodeTree:
    
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None
        
    def add_child(self, new_node):
        if type(new_node) != NodeTree:
            new_node = NodeTree(new_node)
        self.children.append(new_node)
        new_node.parent = self
        
        
    def get_level(self):
        p = self.parent
        level = 0
        while p:
            level += 1
            p = p.parent
        return level
    
    def print_tree(self):
        space = '  ' * self.get_level()
        prefix = space + "|--" if self.parent else "|--"
        print(prefix , self.data)
        for child in self.children:
            child.print_tree()
            
    def height(self):
        if len(self.children) == 0:
            return 0
        else:
            max_height = -1
            for child in self.children:
                max_height = max(max_height, child.height())
            return max_height + 1
    
    
    def search(self, key):
        
        # found
        if self.data == key:
            return True
        
        # not found
        else:
            for child in self.children:
                found = child.search(key)
                if found:
                    return True
                
            return False
        
        
    def isbinary(self):
        if len(self.children) > 2:
            return False
        elif len(self.children) == 0:
            return True
        else:
            for child in self.children:
                if not child.isbinary():
                    return False
                
            return True
        
        
if __name__ == "__main__":
    
    ali = NodeTree("Ali")
    ali.add_child("Reza")
    ali.add_child("Hamed")
    ali.children[0].add_child("Arad")
    ali.children[0].add_child("Aras")
    
    print(ali.print_tree())
    print(ali.isbinary())
    print(ali.search("Ebrahim"))