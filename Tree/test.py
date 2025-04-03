from BinarySearchTree import BinarySearchTree
from AVLTree import AVLTree

def AVL_Test():
    # Create an AVLTree instance
    avl = AVLTree()
    root = avl.root
    
    # Test inserting elements
    root = avl.insert(root, 10)
    assert root.value == 10

    # Insert elements to trigger rotations
    root = avl.insert(root, 20)
    root = avl.insert(root, 30)
    root = avl.insert(root, 40)
    root = avl.insert(root, 50)
    root = avl.insert(root, 25)

    avl.inorder(root)
    avl.preorder(root)
    avl.postorder(root)
    assert avl.inorder_arr == [10, 20, 25, 30, 40, 50]
    assert avl.preorder_arr == [30, 20, 10, 25, 40, 50]
    assert avl.postorder_arr == [10, 25, 20, 50, 40, 30]

    # Assert tree structure is correct after insertions
    assert root.value == 30  # New root after rotations
    assert root.left.value == 20
    assert root.right.value == 40
    assert root.left.right.value == 25
    assert root.right.right.value == 50
    assert root.left.left == None
    assert root.right.left == None

    # Display the AVL tree
    print("AVL Tree Test Passed!:")
def BST_Test():

    bst = BinarySearchTree()
    root = bst.root
    root = bst.insert(root, 10)
    root = bst.insert(root, 5)
    root = bst.insert(root, 15)
    root = bst.insert(root, 3)
    root = bst.insert(root, 7)

    node = bst.search(root, 10)
    assert(node.value == 10)

    bst.inorder(root)
    bst.preorder(root)
    bst.postorder(root)

    assert(bst.inorder_arr == [3, 5, 7, 10, 15])
    assert(bst.preorder_arr == [10, 5, 3, 7, 15])
    assert(bst.postorder_arr == [3, 7, 5, 15, 10])

    root = bst.delete(root, 5)
    assert(bst.search(root, 5) == None)

    print("Binary Search Tree Test Passed!")

if __name__ == "__main__":
    BST_Test()
    AVL_Test()
    print("All tests passed!")
