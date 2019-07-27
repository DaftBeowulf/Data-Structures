class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # greater values become right child
        if self.value <= value:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BinarySearchTree(value)
        # less than or equal values become left child
        else:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BinarySearchTree(value)

    def contains(self, target):
        current_node = self
        while current_node:
            # case 1: value is at current node
            if current_node.value is target:
                return True
        # case 2: value is greater than or equal to current node value
            elif current_node.value <= target:
                current_node = current_node.right
        # case 3: value is less than current node value
            else:
                current_node = current_node.left

    def get_max(self):
        current_node = self
        while current_node.right:
            current_node = current_node.right
        return current_node.value

    def for_each(self, cb):
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)
        cb(self.value)


test = BinarySearchTree(2)
test.insert(3)
test.insert(7)
print(test.value)
