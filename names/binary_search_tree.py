class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # if no node, insert node
        if self.value is None:
            self.value = BinarySearchTree(value)
        else:
            # if value is greater than node, look right, insert node if none, otherwise recurse
            if value >= self.value:
                if self.right is None:
                    self.right = BinarySearchTree(value)
                else:
                    return self.right.insert(value)
            # if value is less than node, look left, insert node if none, otherwise recurse
            else:
                if self.left is None:
                    self.left = BinarySearchTree(value)
                else:
                    return self.left.insert(value)

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        if self.value is None:
            return False
        else:
            if target == self.value:
                return True
            elif target >= self.value and self.right is None:
                return False
            elif target >= self.value and self.right is not None:
                return self.right.contains(target)
            elif target < self.value and self.left is None:
                return False
            elif target < self.value and self.left is not None:
                return self.left.contains(target)

    # Return the maximum value found in the tree

    def get_max(self):
        if self.right:
            return self.right.get_max()
        else:
            return self.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.left is not None:
            self.left.for_each(cb)
        if self.right is not None:
            self.right.for_each(cb)
