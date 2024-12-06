# iga sõlme jaoks jaoks
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

#Kahendpuu konstruktor
class BinaryTree:
    def __init__(self):
        self.root = None

# Sisetamine puusse. 
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(self.root, value)
            
# Kui pole juur, siis abifunktsioon korrektselt sisetamiseks
    def _insert(self, current_node, value):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self._insert(current_node.left, value)
        elif value > current_node.value:
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self._insert(current_node.right, value)
# Puust otsimine
    def search(self, value):
        return self._search(self.root, value)

    def _search(self, current_node, value):
        if current_node is None:
            return False
        if value == current_node.value:
            return True
        elif value < current_node.value:
            return self._search(current_node.left, value)
        else:
            return self._search(current_node.right, value)



# Testimiseks
if __name__ == "puu":
    # Loo binaarpuu
    puu = BinaryTree()

    # Lisa sõlmi
    puu.insert(10)
    puu.insert(5)
    puu.insert(15)


    # Otsi väärtust
    print("Otsingu tulemused:")
    print(tree.search(5))  
    print(tree.search(20))  

