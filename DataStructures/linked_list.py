# Basic class for a singly linked list

class LinkedListNode:
    # attributes:
    # next, of type LinkedListNode
    # data, of any type

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    # attributes:
    # head, of type LinkedListNode

    def __init__(self):
        self.head = None

    # Returns None if data is not found.
    def find(self, data):
        node = self.head
        while node:
            if node.data == data:
                return node
            node = node.next
        return None

    # Add to the head of the list
    def insert(self, data):
        new_node = LinkedListNode(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, node):
        iter_node = self.head
        if iter_node == node:
            self.head = self.head.next
        else:
            while (iter_node.next != node) and (iter_node.next is not None):
                iter_node = iter_node.next
            if iter_node.next is None:
                raise ValueError("node does not exist in linked list")
            else:
                iter_node.next = node.next

    def is_empty(self):
        return self.head is None

    def __str__(self):
        if self.is_empty():
            return "(empty)"
        node = self.head
        output = []
        while node:
            output.append(str(node.data))
            node = node.next
        return " -> ".join(output)


if __name__ == "__main__":
    ll = LinkedList()
    print(ll)
    for i in range(10):
        ll.insert(i)
        print(ll)
    ll.head = ll.head.next
    print(ll)
