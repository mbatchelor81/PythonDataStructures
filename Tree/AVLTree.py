class TreeNode(object):
    """
    Description: A class representing a node in a binary tree.
    Attributes:
        - value: The value of the node.
        - left: A reference to the left child node.
        - right: A reference to the right child node.
        - height: The height of the node in the tree.
    """
    def __init__(self, key):
        self.value = key
        self.left = None
        self.right = None
        self.height = 1  # Height of the node is initially 1 (itself)

class AVLTree(object):
    def __init__(self):
        """
        Description: A class representing an AVL tree.
        Attributes:
            - root: The root node of the AVL tree.
            - inorder_arr: List to store the values in inorder traversal.
            - preorder_arr: List to store the values in preorder traversal.
            - postorder_arr: List to store the values in postorder traversal.
        """
        self.root = None
        self.height = 0
        self.balance = 0
        self.inorder_arr = []
        self.preorder_arr = []
        self.postorder_arr = []

    def insert(self, node, key):
        """
        Description: Insert a key into the AVL tree and balance it if necessary.
        This function recursively inserts a new key into the tree and updates the height and balance factor of each node.
        It performs rotations to maintain the AVL property (balance factor of -1, 0, or 1).

        Return:
        - If the tree is empty, create a new node and return it
        - If the key already exists, return the root
        """
        # Perform the normal insertion
        if not node:
            return TreeNode(key)
        if key < node.value:
            node.left = self.insert(node.left, key)
        elif key > node.value:
            node.right = self.insert(node.right, key)
        else:
            return node

        # Update the height of the ancestors of the inserted node
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        
        # Get the balance factor of this ancestor node to check whether this node became unbalanced
        balance = self.get_balance(node, key)

        # Check all four balancing cases
        # Left Left Case
        if balance > 1 and key < node.left.value:
            return self.rotate_right(node)
        # Right Right Case
        if balance < -1 and key > node.right.value:
            return self.rotate_left(node)
        # Left Right Case
        if balance > 1 and key > node.left.value:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        # Right Left Case
        if balance < -1 and key < node.right.value:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)
        
        return node

    def search(self, root, key):
        """
        Description: Search for a key in the tree.
        
        Return: 
         - If the key is found, return the node
         - If the key is not found, return None
        """
        if root is None or root.value == key:
            return root
        if root.value < key:
            return self.search(root.right, key)
        return self.search(root.left, key)
    
    def delete(self, root, key):
        """
        Description: Delete a key from the AVL tree and balance it if necessary
        
        This function recursively deletes a key from the tree and updates the height and balance factor of each node.
        It performs rotations to maintain the AVL property (balance factor of -1, 0, or 1).

        Return:
        - If the tree is empty, return None
        - If the key is not found, return the root
        - If the key is found, delete the node and return the new root
        """
        # Base case: if the tree is empty, return None
        if root is None:
            return root

        # If the key to be deleted is smaller than the root's key, it lies in the left subtree
        if key < root.value:
            root.left = self.delete(root.left, key)
        
        # If the key to be deleted is greater than the root's key, it lies in the right subtree
        elif key > root.value:
            root.right = self.delete(root.right, key)

        # If the key is the same as the root's key, this is the node to be deleted
        else:
            if root.left is None or root.right is None:
                temp = root.left if root.left else root.right

                # No child case
                if temp is None:
                    root = None
                else:
                    root = temp
            else:
                # Root with two children: get the inorder successor (smallest in the right subtree)
                temp = self.get_successor(root.right)
                root.value = temp.value
                root.right = self.delete(root.right, temp.value)
        
        # If the tree has only one node, return it
        if root is None:
            return root
        
        # Update height of the current node
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # Get the balance factor of this ancestor node to check whether this node became unbalanced
        balance = self.get_balance(root, key)

        # Check all four balancing cases
        # Left Left Case
        if balance > 1 and self.get_balance(root.left, key) >= 0:
            return self.rotate_right(root)
        # Left Right Case
        if balance > 1 and self.get_balance(root.left, key) < 0:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)
        # Right Right Case
        if balance < -1 and self.get_balance(root.right, key) <= 0:
            return self.rotate_left(root)
        # Right Left Case
        if balance < -1 and self.get_balance(root.right, key) > 0:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)
        return root

    def get_successor(node):
        """
        Description: Get the inorder successor of a node in the AVL tree.

        Return:
        - If the right subtree is empty, return None.
        - Otherwise, return the leftmost node in the right subtree
        """
        current = node

        # loop down to find the leftmost leaf
        while current.left is not None:
            current = current.left

    def rotate_left(self, x):
        """
        Description: Perform a left rotation on the given node x

        Return:
        - The new root of the subtree after rotation
        - The left child of x becomes the new root, and x becomes the right child of the new root
        """
        y = x.right
        t2 = y.left

        # Perform rotation
        # 1. New left child of y becomes x
        y.left = x
        # 2. New right child of x becomes left child of y
        x.right = t2

        # Update heights
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        # Return the new root
        return y
        
    def rotate_right(self, y):
        """
        Description: Perform a right rotation on the given node y

        Return:
        - The new root of the subtree after rotation
        - The right child of y becomes the new root, and y becomes the left child of the new root
        """
        x = y.right
        t2 = x.left

        # Perform rotation
        # 1. New right child of x becomes y
        x.right = y
        # 2. New left child of y becomes left child of x
        y.left = t2

        # Update heights
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))

        # Return the new root
        return x
        
    def get_balance(self, node, key):
        """
        Description: Get the balance factor of a node in the AVL tree.

        Return: 
            - If the node is None, return 0 (base case)
            - Otherwise, return the balance factor of the node
        """
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)
    
    def get_height(self, node):
        """
        Description: Get the height of a node in the AVL tree.

        The height of a node is defined as the number of edges on the longest path from the node to a leaf.
        Return:
         - If the node is None, return 0 (base case)
         - Otherwise, return the height of the node
        """
        if not node:
            return 0
        return node.height

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

    def levelorder(self, root):
        """
        Description: Perform a level order traversal of the binary search tree.
        The level order traversal visits each level of the tree from top to bottom and left to right.

        Return: List of values in level order
        """
        if not root:
            return []

        queue = [root]
        result = []

        while queue:
            current = queue.pop(0)
            result.append(current.value)

            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

        return result