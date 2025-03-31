class TreeNode(object):
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

class BinarySearchTree(object):
    def __init__(self):
        self.root = None
        self.inorder_arr = []
        self.preorder_arr = []
        self.postorder_arr = []

    def insert(self, root, key):
        if root is None:
            return TreeNode(key)
        if root.value == key:
            return root
        if root.value < key:
            root.right = self.insert(root.right, key)
        else:
            root.left = self.insert(root.left, key)
        return root
    
    def search(self, root, key):
        if root is None or root.value == key:
            return root
        if root.value < key:
            return self.search(root.right, key)
        return self.search(root.left, key)

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            self.inorder_arr.append(root.value)
            self.inorder(root.right)
            return self.inorder_arr

    def preorder(self, root):
        if root:
            self.preorder_arr.append(root.value)
            self.preorder(root.left)
            self.preorder(root.right)
            return self.preorder_arr

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            self.postorder_arr.append(root.value)
            return self.postorder_arr

    def delete(self, root, key):
        if root is None: 
            return root
        if root.value > key:
            root.left = self.delete(root.left, key)
        elif root.value < key:
            root.right = self.delete(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            temp = self.get_successor(root)
            root.value = temp.value
            root.right = self.delete(root.right, temp.value)

        return root
    
    def get_successor(self, curr):
        curr = curr.right
        while curr is not None and curr.left is not None:
            curr = curr.left
        return curr