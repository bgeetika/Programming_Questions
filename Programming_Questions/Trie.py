class node:
    def __init__(self):
        self.children = {} 
        #link to value to link to node.
        self.end = False

def isnum(c):
    return c.isdigit()

class Trie:
    def __init__(self):
        self.root = node()
    
    def insert(self, v):
        current = self.root
        n = len(v)
        for i in range(len(v)) :
            c = v[i]
            current = current.children.setdefault(c, node())
            if i == n-1:
                current.end = True
                
                
    
    def check_char(self, c, current_node):
        if c in current_node.children:
            return True
        else:
            return False

        
    def find(self, word):
        current_node = self.root
        return self.find_word(word, current_node)
        
        
    def find_word(self, word, current_node):
        if word:
            if isnum(word[0]):
                print word
                number = int(word[0])
                if number == 0:
                        return self.find_word(word[1:], current_node)
                for key in current_node.children:
                    child_node = current_node.children[key]
                    result = self.find_word((str)(number-1) + word[1:], child_node)
                    if result:
                        return True
                return False
            else:
                return (self.check_char(word[0],current_node) and self.find_word(word[1:], current_node.children[word[0]]))
        else:
            return True
        
        
        
        
    def print_trie(self, root):
        ## should be careful with using same name for local and member variables.
        if root:
            for x in root.children:
                print x
                self.print_trie(root.children[x])
    


dict = ["cation", "catious"]            
trie = Trie()

for word in dict:
     trie.insert(word)
        
print trie.find("cat3s")
#trie.print_trie(trie.root)
