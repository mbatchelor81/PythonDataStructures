class TreeNode(object):
    """
    A class representing a node in a binary search tree.
    Each node contains a value, a left child, and a right child.
    """
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

class BinarySearchTree(object):
    """
    A class representing a binary search tree.
    It supports insertion, searching, deletion, and traversal (inorder, preorder, postorder).
    """
    def __init__(self):
        self.root = None
        self.inorder_arr = []
        self.preorder_arr = []
        self.postorder_arr = []

    def insert(self, root, key):
        """Insert a new key into the binary search tree.
        If the tree is empty, create a new node and return it.
        If the key already exists, return the root.
        If the key is less than the root's value, insert it into the left subtree.
        If the key is greater than the root's value, insert it into the right subtree.
        """
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
        """
        Description: Search for a key in the binary search tree.
        
        Return: 
         - If the key is found, return the node
         - If the key is not found, return None
        """
        if root is None or root.value == key:
            return root
        if root.value < key:
            return self.search(root.right, key)
        return self.search(root.left, key)

    def inorder(self, root):
        """
        Description: Perform an inorder traversal of the binary search tree.
        The inorder traversal visits the left subtree, the root, and then the right subtree.
        
        Return: List of values in sorted order
        """
        if root:
            self.inorder(root.left)
            self.inorder_arr.append(root.value)
            self.inorder(root.right)
            return self.inorder_arr

    def preorder(self, root):
        """
        Description: Perform a preorder traversal of the binary search tree.
        The preorder traversal visits the root, the left subtree, and then the right subtree.
        
        Return: List of values in the order they were visited
        """
        if root:
            self.preorder_arr.append(root.value)
            self.preorder(root.left)
            self.preorder(root.right)
            return self.preorder_arr

    def postorder(self, root):
        """
        Description: Perform a postorder traversal of the binary search tree.
        The postorder traversal visits the left subtree, the right subtree, and then the root.

        Return: List of values in the order they were visited
        """
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            self.postorder_arr.append(root.value)
            return self.postorder_arr

    def delete(self, root, key):
        """
        Description: Delete a key from the binary search tree.

        Return: 
        - If the key is found, remove the node and return the new root.
        - If the key is not found, return the root.
        """
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
        """
        Description: Get the inorder successor of a node in the binary search tree.
        The inorder successor is the smallest node in the right subtree.
        
        Return: 
        - If the right subtree is empty, return None.
        """
        curr = curr.right
        while curr is not None and curr.left is not None:
            curr = curr.left
        return curr