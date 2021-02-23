class Node:
    def __init__(self, char, char_freq):
        self.char = char
        self.char_freq = char_freq
        self.right_child = None
        self.left_child = None

    def __eq__(self, next_node):
        if(next_node == None):
            return False
        if(not isinstance(next_node, Node)):
            return False
        if(self.char_freq == next_node.char_freq):
            return True
		

    
    def __lt__(self, next_node):
        if (self.char_freq < next_node.char_freq):
            return True
        else:
            return False
    
        
