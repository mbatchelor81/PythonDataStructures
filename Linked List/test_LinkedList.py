from LinkedList import LinkedList

def test_linked_list_append():
    # Create a LinkedList instance
    ll = LinkedList()

    # Test appending elements
    ll.append(10)
    ll.append(20)
    ll.append(30)

    # Display the linked list
    print("Linked List after appending elements:")
    ll.display()

    # Expected output: 10 -> 20 -> 30 -> None

def test_lined_list_remove():
    # Create a LinkedList instance
    ll = LinkedList()

    # Test appending elements
    ll.append(10)
    ll.append(20)
    ll.append(30)

    # Remove an element
    ll.remove(20)

    # Display the linked list
    print("Linked List after removing element 20:")
    ll.display()

    # Expected output: 10 -> 30 -> None

def test_linked_list_find():
    # Create a LinkedList instance
    ll = LinkedList()

    # Test appending elements
    ll.append(10)
    ll.append(20)
    ll.append(30)

    # Find an element
    found_node = ll.find(20)

    # Display the result
    if found_node:
        print("Found node with data:", found_node.data)
    else:
        print("Node not found")

    # Expected output: Found node with data: 20

def test_linked_list_insert():
    # Create a LinkedList instance
    ll = LinkedList()

    # Test appending elements
    ll.append(10)
    ll.append(30)

    # Insert an element at index 1
    ll.insert(20, 1)

    # Display the linked list
    print("Linked List after inserting element 20 at index 1:")
    ll.display()

    # Expected output: 10 -> 20 -> 30 -> None

if __name__ == "__main__":
    print("Unit Test 1:")
    test_linked_list_append()
    print("-----------------")

    print("Unit Test 2:")
    test_lined_list_remove()
    print("-----------------")
    
    print("Unit Test 3:")
    test_linked_list_find()
    print("-----------------")
    
    print("Unit Test 4:")
    test_linked_list_insert()
    print("-----------------") 