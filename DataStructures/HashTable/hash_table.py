class HashTableNode:
    def __init__(self):
        self.key = None
        self.value = None
        self.next = None
        self.prev = None


class ChainingDict:
    def __init__(self, m, func):
        self.c_dict = [None for i in range(m)]
        self.func = func

    def find(self, key):
        node = self.c_dict[self.func(key)]
        while node:
            if node.key == key:
                return node.value
            node = node.next
        return None

    def set(self, key, value):
        node = self.c_dict[self.func(key)]
        if node is None:
            temp = HashTableNode()
            temp.key = key
            temp.value = value
            self.c_dict[self.func(key)] = temp
        else:
            while node.key != key and node.next:
                node = node.next
            if node.key == key:
                node.value = value
            else:
                temp = HashTableNode()
                temp.key = key
                temp.value = value
                temp.prev = node
                node.next = temp

    def delete(self, key):
        node = self.c_dict[self.func(key)]
        while node:
            if node.key == key:
                if node.prev:
                    node.prev.next = node.next
                if node.next:
                    node.next.prev = node.prev
                if node.next is None and node.prev is None:
                    self.c_dict[self.func(key)] = None
                node = None
            else:
                node = node.next

    def __str__(self):
        return str(self.c_dict)

