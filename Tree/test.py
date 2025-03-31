from BinarySearchTree import BinarySearchTree

if __name__ == "__main__":
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

    print("All tests passed!")