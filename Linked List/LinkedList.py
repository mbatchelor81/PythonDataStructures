class Node:
    """
    Linked List node class containing data and a pointer to the next node.

    These nodes are singly linked pointing only to the next node.
    """
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    """
    Linked List class storing the head node and providing methods to manipulate the list.

    Methods:
    - append(data): Adds a new node with the given data to the end of the list.
        - Time Complexity: O(n) where n is the number of nodes in the list, iterates through all nodes until the last one.
    - display(): Prints all elements in the linked list.
        - Time Complexity: O(n) where n is the number of nodes in the list, iterates through all nodes to print their data.
    - remove(data): Removes the first node with the given data.
        - Time Complexity: O(n) where n is the number of nodes in the list, iterates through all nodes until the target node is found.
    - find(data): Finds a node with the given data.
        - Time Complexity: O(n) where n is the number of nodes in the list, iterates through all nodes until the target node is found.
    - insert(data, index): Inserts a new node with the given data at the specified index.
        - Time Complexity: O(n) where n is the number of nodes in the list, iterates through all nodes until the target index is reached.
    """
    def __init__(self):
        self.head = None
        self.count = 0

    def append(self, data):
        """Add a new node with the given data to the end of the list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        self.count += 1

    def insert(self, data, index):
        """Insert a new node with the given data at the specified index."""
        if index < 0 or index > self.count:
            raise IndexError("Index out of bounds")
        new_node = Node(data)
        # if index is 0, insert at the head
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            self.count += 1
            return "Successfully inserted node at index {}".format(index)
        # if index is greater than 0, find the node at index - 1
        current = self.head
        for _ in range(index - 1):
            current = current.next
        # point new node to current nodes next value, point current node to new node
        new_node.next = current.next
        current.next = new_node
        self.count += 1
        return "Successfully inserted node at index {}".format(index)


    def remove(self, data):
        """Remove the first node with the given data."""
        current = self.head
        prev = None
        while current is not None:
            if current.data == data:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return
            prev = current
            current = current.next

    def find(self, data):
        """Find a node with the given data."""
        current = self.head
        while current != None:
            if current.data == data:
                return current
            current = current.next
        return "Node not found" 

    def display(self):
        """Print all elements in the linked list."""
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
