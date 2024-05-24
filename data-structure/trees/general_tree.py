

class NodeTree:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None
        
    def add_node(self, node):
        self.children.append(node)
        node.parent = self
        
    def print_tree(self):
        
        space = "\t"
        print(space * self.get_level(), self.data)
        for child in self.children:
            child.print_tree()
            
    def get_level(self):
        p = self.parent
        lvl = 1
        while p:
            lvl +=1
            p = p.parent
        return lvl
    
    def height(self):
        if len(self.children) == 0:
            return 0
        else:
            max_height = -1
            for child in self.children:
                max_height = max(max_height, child.height())
            return max_height + 1
        
        
if __name__ == "__main__":
    
    # Create a Node (root)
    root = NodeTree("Electronics")
    
    # Create Children for root
    ## first child
    laptop = NodeTree("Laptop")
    laptop.add_node(NodeTree("Acer"))
    laptop.add_node(NodeTree("Asus"))
    laptop.add_node(NodeTree("Mac"))
    
    root.add_node(laptop)
    
    ## second child   
    phone = NodeTree("Phone")
    phone.add_node(NodeTree("iPhone"))
    phone.add_node(NodeTree("Samsung"))
    phone.add_node(NodeTree("Xiaomi"))
    
    root.add_node(phone)
    
    ## third child   
    tv = NodeTree("TV")
    tv.add_node(NodeTree("Goldiran"))
    tv.add_node(NodeTree("LG"))
    tv.add_node(NodeTree("SONY"))
    
    root.add_node(tv)
    
    root.print_tree()
    print(root.height())